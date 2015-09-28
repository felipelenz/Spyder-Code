#!/usr/bin/python

# Program to read and process Yokogawa DL850 ".HDR" and ".WVF" files
#
# This is a Python port of the MATLAB code developed by Jason Jerauld, PhD
# and later modified by Joe Howard, PhD.
#
# Author: Jaime Caicedo, PhD Student, ILCRT
# Last Updated: 03/07/2014

import numpy as np
import math
import struct


class Yoko850File(object):
    """
    This class implements an object for a Yokogawa DL850 file, which contains
    a header and traces.
    """

    def __init__(self, fileName):
        if fileName[-3:].lower() == 'hdr' or fileName[-3:].lower() == 'wvf':
            filename = fileName[:-4]

        self.filename = fileName

    def get_header(self):
        """
        This function processes the '.HDR' file and returns
        a YokoHeader object.
        """
        try:
            try:
                f = open(self.filename + '.hdr')
            except IOError:
                try:
                    f = open(self.filename + '.HDR')
                except IOError:
                    raise

            try:
                # Get the number of groups
                for i in range(3):
                    f.readline()        # Move cursor to line 8 by reading 7
                                        # dummy lines
                L=f.readline()
                if L[0]=='F':
                    [f.readline() for x in range(3)]
                else:
                    [f.readline() for x in range(4)]

                groupLine = f.readline().split()
                numGroups = eval(groupLine[1])

                # Get the number of traces
                traceLine = f.readline().split()
                numTraces = eval(traceLine[1])

                # Compute the number of full 4-trace groups
                numFullGroups = int(numTraces/4)
                if numFullGroups == 0:
                    numFullGroups = 1

                # Compute how many traces there are in the non-full group
                remainingTraces = numTraces - 4 * numFullGroups

                # Get the data offset, which causes the problems between 750
                # and 716 (getting this line also gives uniformity for later)
                dataOffsetLine = f.readline().split()
                dataOffset = eval(dataOffsetLine[1])

                traceID = []
                VResolution = []
                VOffset = []

                for j in range(numFullGroups): #range(1):

                    # Get traces names in group
                    for i in range(4):
                        f.readline()    # Read 4 dummy lines

                    traceIDString = f.readline().split()[1:]

                    for tid in traceIDString:
                        traceID.append(tid)
                    
                    # Without loop
                    #~ traceID.append(traceIDString[1])
                    #~ traceID.append(traceIDString[2])
                    #~ traceID.append(traceIDString[3])
                    #~ traceID.append(traceIDString[4])

                    # Determine block size (number of samples) from the first
                    # trace entry
                    blockSizeString = f.readline().split()
                    blockSize = eval(blockSizeString[1])

                    # Determine the vertical resolution of the each channel
                    VResolutionString = f.readline().split()[1:]

                    for vres in VResolutionString:
                        VResolution.append(eval(vres))
                        
                    # Without loop
                    #~ VResolution.append(eval(VResolutionString[1]))
                    #~ VResolution.append(eval(VResolutionString[2]))
                    #~ VResolution.append(eval(VResolutionString[3]))
                    #~ VResolution.append(eval(VResolutionString[4]))

                    # Determine the vertical offset of each channel
                    VOffsetString = f.readline().split()[1:]

                    for voff in VOffsetString:
                        VOffset.append(eval(voff))
                    
                    # Without loop
                    #~ VOffset.append(eval(VOffsetString[1]))
                    #~ VOffset.append(eval(VOffsetString[2]))
                    #~ VOffset.append(eval(VOffsetString[3]))
                    #~ VOffset.append(eval(VOffsetString[4]))

                    # Determine horizontal resolution (sampling rate) from the
                    # first trace entry
                    for i in range(7):
                        f.readline() # Read 7 dummy lines

                    HResolutionString = f.readline().split()

                    HResolution = eval(HResolutionString[1])

                    # Determine horizontal offset (pretrigger) from the first
                    # trace entry
                    HOffsetString = f.readline().split()
                    HOffset = eval(HOffsetString[1])

                    # Determine the file date from the first trace entry
                    f.readline()    # Read dummy line

                    dateString = f.readline().split()
                    Date = dateString[1]

                    # Determine the file time from the first trace entry
                    timeString = f.readline().split()
                    Time = timeString[1]

                # Get the info for the remaining traces that are not in a full
                # group

#                if (remainingTraces > 0):
#                    # Get traces names in group
#                    for i in range(4):
#                        f.readline()    # Read 4 dummy lines
#
#                    traceIDString = f.readline().split()
#
#                    # Get the trace ID names from the one-line string
#                    for i in range(remainingTraces):
#                        traceID.append(traceIDString[i+1])
#
#                    # Determine the block size (number of samples) from the
#                    # first trace entry
#                    blockSizeString = f.readline().split()
#                    blockSize = eval(blockSizeString[1])
#
#                    # Determine the vertical resolution of each channel
#                    VResolutionString = f.readline().split()
#                    for i in range(remainingTraces):
#                        VResolution.append(eval(VResolutionString[i+1]))
#
#                    # Determine the vertical offset of each channel
#                    VOffsetString = f.readline().split()
#                    for i in range(remainingTraces):
#                        VOffset.append(eval(VOffsetString[i+1]))
#
#                    # Determine the horizontal resolution (sampling rate) from
#                    # the first trace entry
#                    for i in range(7):
#                        f.readline()    # Read 7 dummy lines
#
#                    HResolutionString = f.readline().split()
#                    HResolution = eval(HResolutionString[1])
#
#                    # Determine the horizontal offset (pretrigger) from the
#                    # first trace entry
#                    HOffsetString = f.readline().split()
#                    HOffset = eval(HOffsetString[1])

                result = YokoHeader(traceID, Date, Time, dataOffset, \
                                    blockSize, HResolution, HOffset, \
                                    VResolution, VOffset)

            finally:
                f.close()

        except IOError:
            raise

        return result

    def get_trace_data(self, header, traceNumber, timeStart, timeStop, \
                       calFactor=1, wantOffset='n'):
        """
        This function processes the '.WVF' file and returns
        a YokoTrace object.
        """

        traceID = header.traces
        dataOffset = header.dataOffset
        blockSize = header.blockSize
        HResolution = header.HResolution
        HOffset = header.HOffset
        VResolution = header.VResolution
        VOffset = header.VOffset
        Date = header.Date
        GPSTime = header.Time

        # Process the binary Data

        # Window the timebase and data
        if (timeStart < HOffset):       # This segment of code was added
            offset = HOffset            # because the time range goes from
        else:                           # 0 + |HOffset| to end + |HOffset|
            offset = 0                  # (In a 2 sec file, end = 2).
                                        # So, when looking at a file in df32,
                                        # which does not get rid of HOffset,
                                        # the times one will pick already
                                        # include the offset.

        startIndex = round((timeStart - offset) / HResolution)
        stopIndex = round((timeStop - offset) / HResolution)

        # Open the actual waveform file using read-only and big endian binary
        # format
        try:
            with open(self.filename + '.wvf', 'rb') as f:
                # Rewind the file to the beginning
                f.seek(0,0)

                # Move to the position of the desired trace
                f.seek(2 * (blockSize * (traceNumber - 1) + startIndex) + \
                       dataOffset, 0)

                # Read a trace from the data file (remember that we have 16-bit
                # (2-byte) data)
                data = np.zeros(stopIndex - startIndex + 1)

                d_s=f.read(2*len(data))
                data=np.fromstring(d_s, dtype=np.dtype('>h'))

#               for i in xrange(data.shape[0]):
#                   data[i], = struct.unpack('>h',f.read(2))   # Read 2 bytes
#                                                              # of data at
#                                                              # a time
#                                                              # (big-endian)

                # Scale the raw ADC values
                data = calFactor * (VResolution[traceNumber-1] * data + VOffset[traceNumber-1])

                # Calculate the timebase
                dataTime = np.arange(0,data.shape[0])*HResolution + timeStart

                # Calculate the vertical offset based on the first 1000 samples

                if wantOffset==True or (hasattr(wantOffset,'lower') and wantOffset.lower() == 'y'):
#                   f.seek(0,0)
#                   f.seek(2 * (blockSize*(traceNumber - 1) + dataOffset),0)
#
#                   thousandSamples = np.zeros(1000)
#                   for i in xrange(thousandSamples.shape[0]):
#                       thousandSamples[i], = struct.unpack('>h',f.read(2))
#                    thousandSampleOffset = np.mean(calFactor * (thousandSamples * \
#                                                  VResolution[traceNumber-1] + \
#                                                  VOffset[traceNumber-1]))
#                   data = data - thousandSampleOffset

                    """
                    Average first or last 1000 points to remove offset
                    """
                    #~ data-=np.mean(data[0:1000])  # First
                    data-=np.mean(data[-1000:]) # Last

                # Get the trace label
                traceLabel = traceID[traceNumber-1]

                result = YokoTrace(data, dataTime, traceLabel, HResolution,\
                                   HOffset, Date, GPSTime)

        except IOError as e:
            print(str(e))

        return result


class YokoHeader(object):
    """
    This class implements an object for the header information contained
    in the '.HDR' file.
    """
    def __init__(self, traces, Date, Time, dataOffset, blockSize, \
                 HResolution, HOffset, VResolution, VOffset):
        """
        Args:
            traces (list): A list of all the traces labels (usually channel
                           IDs) available in the file
            Date (str): The date of the Yokogawa file
            Time (str): The time of the Yokogawa file
            dataOffset (int): The data offset
            blockSize (int): The block size
            HResolution (int): The horizontal resolution
            HOffset (int): The horizontal offset
            VResolution (list): The vertical resolution for each trace
            VOffset (list): The vertical offset for each trace
        """

        self.traces = traces
        self.Date = Date
        self.Time = Time
        self.dataOffset = dataOffset
        self.blockSize = blockSize
        self.HResolution = HResolution
        self.HOffset = HOffset
        self.VResolution = VResolution
        self.VOffset = VOffset

    def __str__(self):
        s = '\nTraces:\n  %s' % self.traces
        s += '\nDate:\n  %s' % self.Date
        s += '\nTime:\n  %s' % self.Time
        s += '\nData Offset:\n  %s' % self.dataOffset
        s += '\nBlock Size:\n  %s' % self.blockSize
        s += '\nHResolution:\n  %s' % self.HResolution
        s += '\nHOffset:\n  %s' % self.HOffset
        s += '\nVResolution:\n  %s' % self.VResolution
        s += '\nVOffset:\n  %s' % self.VOffset

        return s

class YokoTrace(object):
    """
    This class implements an object for the information contained
    in the '.WVF' file.
    """
    def __init__(self, data, dataTime, traceLabel, HResolution,\
                 HOffset, Date, GPSTime):
        """
        Args:
            data (numpy array): The vertical data
            dataTime (numpy array): The horizontal data. This array is the
                                    same length as the data array. This array
                                    begins at 'timeStart' and ends at
                                    'timeStop' and each value is separated by
                                    the sampling interval of the data
                                    (determined from the header)
            traceLabel (str): The trace label of the exported data, as
                              determined from the header. This is mostly used
                              to verify that the desired channel has been
                              exported. This is a string in the form 'CHX',
                              where 'X' is the scope channel number.
            HResolution (int): The horizontal resolution (sampling interval) of
                               the data. This is the same for all time windows
                               and channels.
            HOffset (int): The horizontal offset (pre-trigger) of the data.
                           This is the same for all time windows and channels.
            Date (str): The date of the Yokogawa file, as stored in the header.
            GPSTime (str): The time of the Yokogawa file, as stored in the
                           header.
        """
        self.data = data
        self.dataTime = dataTime
        self.traceLabel = traceLabel
        self.HResolution = HResolution
        self.HOffset = HOffset
        self.Date = Date
        self.GPSTime = GPSTime

    def __str__(self):
        s = '\nTrace Label:\n  %s' % self.traceLabel
        s += '\nDate:\n  %s' % self.Date
        s += '\nGPS Time:\n  %s' % self.GPSTime
        s += '\nHResolution:\n  %s' % self.HResolution
        s += '\nHOffset:\n  %s' % self.HOffset
        s += '\nData Time:\n  %s' % self.dataTime
        s += '\nData:\n  %s' % self.data

        return s
