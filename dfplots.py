#!/usr/bin/env python
"""
The SpanSelector is a mouse widget to select a xmin/xmax range and plot the
detail view of the selected region in the lower axes
"""
import matplotlib as mpl
mpl.use('TkAgg') # 'TkAgg', GtkAgg

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
from scipy.signal import decimate


class syncdf(object):
    """
    class to synchronize dfplots (when you zoom in on one graph, all of
    them do)
    """

    def __init__(self, plotdfs):
        self.plots = plotdfs
        
        for plot in self.plots:
            plot.synced = True
        
    def onselect(self, xmin, xmax):
        for plot in self.plots:
            plot.onselect(xmin, xmax)
            
    def plot_all(self):
        self.spans = []
        self.cids = []
        
        for plot in self.plots:
            self.spans.append(SpanSelector(plot.ax, self.onselect, 'horizontal', useblit=True,
                        rectprops=dict(alpha=0.5, facecolor='red') ))
                    
            self.cids.append(plot.fig.canvas.mpl_connect(\
                            'button_release_event', plot.onclick))
            
            plot.fig.canvas.mpl_connect('key_press_event', plot.onkeypress)
            
            

def plot_simple2D(X,Y, title=None):
    """
    generic plotter (written by Brian Hare)
    """
    fig = plt.figure()
    if title is not None:
        fig.suptitle(title)

    ax = fig.add_subplot(111)
    ax.plot(X, Y)
    plotter = plotdf(fig, ax)
    plotter.plot()
    plt.show()    


class pickerPlot(object):  
    """
    This class enables the picker attribute of lines and sets up the
    environment to enable the movement of lines in the canvas.
    (written by Jaime Caicedo)
    """

    mpl.rcParams['keymap.fullscreen'] = ''
    mpl.rcParams['keymap.back'] = 'b'
    mpl.rcParams['keymap.forward'] = 'f'
      
    def __init__(self, fig, ax):
        self.fig = fig
        self.ax = ax
        self.lines = ax.get_lines()
        self.move_flag = False
        self.selected_line = None
        #~ self.x = []
        #~ self.y = []
                
        for line in self.lines:
            #~ self.x.append(line.get_xdata())
            #~ self.y.append(line.get_ydata())
            line.set_picker(5)
            
        self.ax.set_picker(5)
        
    def onpick(self, event):
        if event.artist == self.ax:
            pass
            
        if event.artist in self.lines:
            #~ print('Selected')
            self.move_flag = True
            self.selected_line = event.artist
            self.line_width = self.selected_line.get_linewidth()
            self.selected_line.set_linewidth(2*self.line_width)
            
        else:
            #~ print('De-Selected')
            self.move_flag = False
            
            if self.selected_line:
                self.selected_line.set_linewidth(self.line_width)
                self.selected_line = None
        
        self.fig.canvas.draw()
            
    def onkeypress(self, event):
        #~ print(self.move_flag)
        #~ print(event.key)
        line = self.selected_line
        
        if line:
            dt = abs(np.diff(line.get_xdata())[0]/2)
            dy = (np.max(line.get_ydata()) - np.min(line.get_ydata()))/len(line.get_xdata())
            
            if event.key == 'ctrl+left' and self.move_flag:
                #~ print('Moving left...')
                line.set_xdata(line.get_xdata() - 10*dt)
                
            elif event.key == 'left' and self.move_flag:
                #~ print('Moving left...')
                line.set_xdata(line.get_xdata() - dt)
                
            elif event.key == 'ctrl+right' and self.move_flag:
                #~ print('Moving right...')
                line.set_xdata(line.get_xdata() + 10*dt)
                
            elif event.key == 'right' and self.move_flag:
                #~ print('Moving right...')
                line.set_xdata(line.get_xdata() + dt)
                
            elif event.key == 'up' and self.move_flag:
                #~ print('Moving up...')
                line.set_ydata(line.get_ydata() + dy)
            
            elif event.key == 'ctrl+up' and self.move_flag:
                #~ print('Moving up...')
                line.set_ydata(line.get_ydata() + 10*dy)
            
            elif event.key == 'alt+up' and self.move_flag:
                #~ print('Moving up...')
                line.set_ydata(line.get_ydata() + 100*dy)
                
            elif event.key == 'down' and self.move_flag:
                #~ print('Moving down...')
                line.set_ydata(line.get_ydata() - dy)
            
            elif event.key == 'ctrl+down' and self.move_flag:
                #~ print('Moving down...')
                line.set_ydata(line.get_ydata() - 10*dy)
            
            elif event.key == 'alt+down' and self.move_flag:
                #~ print('Moving down...')
                line.set_ydata(line.get_ydata() - 100*dy)
                
            self.fig.canvas.draw()
        
        if event.key == ' ' or event.key == 'escape':
            plt.close(self.fig)
        
    def plot(self):
        self.fig.canvas.mpl_connect('pick_event', self.onpick)
        self.fig.canvas.mpl_connect('key_press_event', self.onkeypress)


class plotdf(object):
    """
    Plot graphs to mimic df32 program (written by Jaime Caicedo and Brian
    Hare)
    """
    def __init__(self, figure, ax, synced=False, max_points=1E9):
        self.fig = figure
        self.ax = ax
        self.x = []
        self.y = []
        self.max_points = max_points
        self.set_offset = False
        self.lines = ax.get_lines()        
        
        for line in self.lines:
            self.x = line.get_xdata()
            self.y.append(line.get_ydata())
            
            thisx = line.get_xdata()
            thisy = line.get_ydata()
            
            # Down sample
            ds_rate = int(thisy.shape[0]/self.max_points)
            
            if ds_rate == 0:
                ds_rate = 1
                
            thisy = thisy[::ds_rate]
            thisx = thisx[::ds_rate]
            
            # Set line       
            line.set_data(thisx, thisy)
        
        self.x_stack = []
        self.x_bounds = [self.x[0], self.x[-1]]
        self.synced = synced    
        
    def onselect(self, xmin, xmax):
        if xmin == xmax:
            return True
            
        # Save the current graph's limits
        xmin_old = self.ax.get_xlim()[0]
        xmax_old = self.ax.get_xlim()[1]
        
        # Get new limits and redraw
        indmin, indmax = np.searchsorted(self.x, (xmin, xmax))
        indmax = min(len(self.x)-1, indmax)
        
        if (indmax - indmin) < 2:
            return True
        
        self.x_stack.append([xmin_old, xmax_old])
        
        thisx = self.x[indmin:indmax]
        self.ax.set_xlim(thisx[0], thisx[-1])
        self.x_bounds = [thisx[0], thisx[-1]]
        
        max_y = -np.inf
        min_y = np.inf
        
        for j in range(len(self.lines)):

            if len(self.y) > 1:
                thisy = self.y[j][indmin:indmax]
            else:
                thisy = self.y[0][indmin:indmax]
                
            # Down sample            
            ds_rate = int(thisy.shape[0]/self.max_points)
            
            if ds_rate == 0:
                ds_rate = 1
                
            thisy = thisy[::ds_rate]
            thisx = thisx[::ds_rate]
            
            # Set line
            self.lines[j].set_data(thisx, thisy)
               
            mx_y = thisy.max()
            mn_y = thisy.min()   
                    
            if mx_y > max_y:
                max_y = mx_y
            
            if mn_y < min_y:
                min_y = mn_y
        
        
        max_y = max_y + (max_y - min_y)*.1
        min_y = min_y - (max_y - min_y)*.1
        
        self.ax.set_ylim(min_y, max_y)
        
        self.fig.canvas.draw()
        
    def onclick(self, event):
        if event.button == 3 and (event.inaxes is self.ax or self.synced):
            
            if self.x_stack:
                # Get old limits from stacks
                xmin = self.x_stack[-1][0]
                xmax = self.x_stack[-1][1]
            
                self.x_stack = self.x_stack[:-1]
            
                # Set new limits and redraw
                indmin, indmax = np.searchsorted(self.x, (xmin, xmax))
                indmax = min(len(self.x)-1, indmax)

                thisx = self.x[indmin:indmax]
                self.ax.set_xlim(thisx[0], thisx[-1])
                self.x_bounds = [thisx[0], thisx[-1]]
                
                max_y = -np.inf
                min_y = np.inf
                
                for j in range(len(self.lines)):
                    if len(self.y) > 1:
                        thisy = self.y[j][indmin:indmax]
                    else:
                        thisy = self.y[0][indmin:indmax]
                    
                    
                    # Down sample            
                    ds_rate = int(thisy.shape[0]/self.max_points)
            
                    if ds_rate == 0:
                        ds_rate = 1
                
                    thisy = thisy[::ds_rate]
                    thisx = thisx[::ds_rate]
                    
                    # Set line
                    self.lines[j].set_data(thisx, thisy)
               
                    mx_y = thisy.max()
                    mn_y = thisy.min()   
                    
                    if mx_y > max_y:
                        max_y = mx_y
            
                    if mn_y < min_y:
                        min_y = mn_y
                        
                max_y = max_y + (max_y - min_y)*.1
                min_y = min_y - (max_y - min_y)*.1
            
                self.ax.set_ylim(min_y, max_y)
                self.fig.canvas.draw()
                
        elif event.button == 2 and (event.inaxes is self.ax or self.synced):
            """
            On a Mac, event.button == 2 is a right-click
            """
            
            if self.x_stack:
                # Get old limits from stacks
                xmin = self.x_stack[-1][0]
                xmax = self.x_stack[-1][1]
            
                self.x_stack = self.x_stack[:-1]
            
                # Set new limits and redraw
                indmin, indmax = np.searchsorted(self.x, (xmin, xmax))
                indmax = min(len(self.x)-1, indmax)

                thisx = self.x[indmin:indmax]
                self.ax.set_xlim(thisx[0], thisx[-1])
                self.x_bounds = [thisx[0], thisx[-1]]
                
                max_y = -np.inf
                min_y = np.inf
                
                for j in range(len(self.lines)):
                    if len(self.y) > 1:
                        thisy = self.y[j][indmin:indmax]
                    else:
                        thisy = self.y[0][indmin:indmax]
                    
                    # Down sample            
                    ds_rate = int(thisy.shape[0]/self.max_points)
            
                    if ds_rate == 0:
                        ds_rate = 1
                
                    thisy = thisy[::ds_rate]
                    thisx = thisx[::ds_rate]
                    
                    # Set line                    
                    self.lines[j].set_data(thisx, thisy)
               
                    mx_y = thisy.max()
                    mn_y = thisy.min()   
                    
                    if mx_y > max_y:
                        max_y = mx_y
            
                    if mn_y < min_y:
                        min_y = mn_y
            
                max_y = max_y + (max_y - min_y)*.1
                min_y = min_y - (max_y - min_y)*.1
        
                self.ax.set_ylim(min_y, max_y)
                self.fig.canvas.draw()
 
    def onkeypress(self,event):
        if event.key == 'r':
            if self.x_stack:
                # Get initial limits from stacks
                xmin = self.x_stack[0][0]
                xmax = self.x_stack[0][1]
            
                self.x_stack = []
            
                # Set new limits and redraw
                indmin, indmax = np.searchsorted(self.x, (xmin, xmax))
                indmax = min(len(self.x)-1, indmax)

                thisx = self.x[indmin:indmax]
                self.ax.set_xlim(thisx[0], thisx[-1])
                self.x_bounds = [thisx[0], thisx[-1]]
                
                max_y = -np.inf
                min_y = np.inf
                
                for j in range(len(self.lines)):
                    if len(self.y) > 1:
                        thisy = self.y[j][indmin:indmax]
                    else:
                        thisy = self.y[0][indmin:indmax]
                    
                    # Down sample            
                    ds_rate = int(thisy.shape[0]/self.max_points)
            
                    if ds_rate == 0:
                        ds_rate = 1
                
                    thisy = thisy[::ds_rate]
                    thisx = thisx[::ds_rate]
                    
                    # Set line
                    self.lines[j].set_data(thisx, thisy)
               
                    mx_y = thisy.max()
                    mn_y = thisy.min()   
                    
                    if mx_y > max_y:
                        max_y = mx_y
            
                    if mn_y < min_y:
                        min_y = mn_y
                        
                max_y = max_y + (max_y - min_y)*.1
                min_y = min_y - (max_y - min_y)*.1
                           
                self.ax.set_ylim(min_y, max_y)
                self.fig.canvas.draw()
        elif event.key == ' ' or event.key == 'escape':
            plt.close(self.fig)
        
    def plot(self):
        
        self.span = SpanSelector(self.ax, self.onselect, 'horizontal', \
                                 useblit=True, rectprops=dict(alpha=0.5, \
                                 facecolor='red') )
                    
        self.cid = self.fig.canvas.mpl_connect('button_release_event', \
                                               self.onclick)

        self.kp = self.fig.canvas.mpl_connect('key_press_event', self.onkeypress)


class RelativeTimePlot(object):
    """
    Plotter to generate graphs with relative time axes (written by Jaime
    Caicedo)
    """

    def __init__(self, x, y, max_points=10000, draw=True):    
        self.delta_t = np.diff(x)[0]
        self.zero_time = (x[-1] - x[0])/2
        self.zero_ind = int(self.zero_time/self.delta_t)
        self.max_points = max_points
        
        self.x = x
        self.y = y
        
        self.x_stack = []
        self.draw = draw
        
        if self.draw:
            self.fig = plt.figure()
            self.fig.suptitle('Please select the time zero (Press down \'n\' and left click).')
            self.ax = self.fig.add_subplot(111)
            self.data_line = self.ax.plot(x,y)[0]
            self.zero_line = self.ax.plot([self.zero_time, self.zero_time], [self.ax.get_ylim()[0], self.ax.get_ylim()[1]], 'r')[0]
        
            self.y_bounds = [self.ax.get_ylim()[0], self.ax.get_ylim()[1]]
        
            self.set_zero = False
                  
            # Down sample
            ds_rate = int(self.y.shape[0]/self.max_points)
        
            if ds_rate == 0:
                ds_rate = 1
            
            thisy = self.y[::ds_rate]
            thisx = self.x[::ds_rate]
        
            # Set line                    
            self.data_line.set_data(thisx, thisy)
            
        self.x_bounds = [x[0], x[-1]]     
        
    def onselect(self,xmin, xmax):
        if xmin == xmax:
            return True
            
        # Save the current graph's limits
        xmin_old = self.ax.get_xlim()[0]
        xmax_old = self.ax.get_xlim()[1]
        
        # Get new limits and redraw
        indmin, indmax = np.searchsorted(self.x, (xmin, xmax))
        indmax = min(len(self.x)-1, indmax)
        
        if (indmax - indmin) < 2:
            return True
        
        self.x_stack.append([xmin_old, xmax_old])
        
        thisx = self.x[indmin:indmax]
        self.ax.set_xlim(thisx[0], thisx[-1])
        self.x_bounds = [thisx[0], thisx[-1]]
        
        max_y = -np.inf
        min_y = np.inf
        
        thisy = self.y[indmin:indmax]
            
        # Down sample            
        ds_rate = int(thisy.shape[0]/self.max_points)
        
        if ds_rate == 0:
            ds_rate = 1
            
        thisy = thisy[::ds_rate]
        thisx = thisx[::ds_rate]
        
        # Set line
        self.data_line.set_data(thisx, thisy)
           
        mx_y = thisy.max()
        mn_y = thisy.min()   
                
        if mx_y > max_y:
            max_y = mx_y
        
        if mn_y < min_y:
            min_y = mn_y
        
        
        max_y = max_y + (max_y - min_y)*.1
        min_y = min_y - (max_y - min_y)*.1
        
        self.ax.set_ylim(min_y, max_y)
        
        self.fig.canvas.draw()

    def onclick(self, event):
        if event.button == 1 and (event.inaxes is self.ax):
            if self.set_zero:
                self.zero_time = event.xdata
                self.zero_ind = int((self.zero_time - self.x[0])/self.delta_t)

                ##redraw
                zero_x = [self.zero_time, self.zero_time]
                self.zero_line.set_data(zero_x, self.y_bounds)
                
                self.fig.canvas.draw()

        if event.button == 3 and (event.inaxes is self.ax):

            if self.x_stack:
                # Get old limits from stacks
                xmin = self.x_stack[-1][0]
                xmax = self.x_stack[-1][1]

                self.x_stack = self.x_stack[:-1]

                # Set new limits and redraw
                indmin, indmax = np.searchsorted(self.x, (xmin, xmax))
                indmax = min(len(self.x)-1, indmax)

                thisx = self.x[indmin:indmax]
                self.ax.set_xlim(thisx[0], thisx[-1])
                self.x_bounds = [thisx[0], thisx[-1]]

                ##set the data y
                thisy = self.y[indmin:indmax]

                # Down sample            
                ds_rate = int(thisy.shape[0]/self.max_points)
        
                if ds_rate == 0:
                    ds_rate = 1
            
                thisy = thisy[::ds_rate]
                thisx = thisx[::ds_rate]
        
                # Set line
                self.data_line.set_data(thisx, thisy)
                ##self.data_line.set_data(thisx, data_y)

                max_y = thisy.max()
                min_y = thisy.min()

                ##set the offset y
                ##offset_y = np.ones(len(thisx))*self.dc_offset
                ##self.offset_line.set_data(thisx, offset_y)

#~                 max_y = max(max_y, self.dc_offset)
#~                 min_y = min(min_y, self.dc_offset)

                ##draw
                self.ax.set_ylim(min_y-0.1*(max_y-min_y), max_y+0.1*(max_y-min_y))
                self.fig.canvas.draw()
        
        if event.button == 2 and (event.inaxes is self.ax):
            """
            On a Mac, event.button == 2 is a right-click
            """
            if self.x_stack:
                # Get old limits from stacks
                xmin = self.x_stack[-1][0]
                xmax = self.x_stack[-1][1]

                self.x_stack = self.x_stack[:-1]

                # Set new limits and redraw
                indmin, indmax = np.searchsorted(self.x, (xmin, xmax))
                indmax = min(len(self.x)-1, indmax)

                thisx = self.x[indmin:indmax]
                self.ax.set_xlim(thisx[0], thisx[-1])
                self.x_bounds = [thisx[0], thisx[-1]]

                ##set the data y
                thisy = self.y[indmin:indmax]

                # Down sample            
                ds_rate = int(thisy.shape[0]/self.max_points)
        
                if ds_rate == 0:
                    ds_rate = 1
            
                thisy = thisy[::ds_rate]
                thisx = thisx[::ds_rate]
        
                # Set line
                self.data_line.set_data(thisx, thisy)
                
                ##self.data_line.set_data(thisx, data_y)

                max_y = thisy.max()
                min_y = thisy.min()

                ##set the offset y
                ##offset_y = np.ones(len(thisx))*self.dc_offset
                ##self.offset_line.set_data(thisx, offset_y)

              #~   max_y = max(max_y, self.dc_offset)
#~                 min_y = min(min_y, self.dc_offset)

                ##draw
                self.ax.set_ylim(min_y-0.1*(max_y-min_y), max_y+0.1*(max_y-min_y))
                self.fig.canvas.draw()
    
    def onkeypress(self,event):
        if event.key == 'n':
            self.set_zero = True
            
        elif event.key == 'r':
            if self.x_stack:
                # Get initial limits from stacks
                xmin = self.x_stack[0][0]
                xmax = self.x_stack[0][1]
            
                self.x_stack = []
            
                # Set new limits and redraw
                indmin, indmax = np.searchsorted(self.x, (xmin, xmax))
                indmax = min(len(self.x)-1, indmax)

                thisx = self.x[indmin:indmax]
                self.ax.set_xlim(thisx[0], thisx[-1])
                self.x_bounds = [thisx[0], thisx[-1]]
                
                max_y = -np.inf
                min_y = np.inf
                
                thisy = self.y[indmin:indmax]
                
                # Down sample            
                ds_rate = int(thisy.shape[0]/self.max_points)
        
                if ds_rate == 0:
                    ds_rate = 1
            
                thisy = thisy[::ds_rate]
                thisx = thisx[::ds_rate]
                
                # Set line
                self.data_line.set_data(thisx, thisy)
           
                mx_y = thisy.max()
                mn_y = thisy.min()   
                
                if mx_y > max_y:
                    max_y = mx_y
        
                if mn_y < min_y:
                    min_y = mn_y
                        
                max_y = max_y + (max_y - min_y)*.1
                min_y = min_y - (max_y - min_y)*.1
                           
                self.ax.set_ylim(min_y, max_y)
                self.fig.canvas.draw()
        
        elif event.key == ' ' or event.key == 'escape':
            plt.close(self.fig)
        #~ else:
            #~ print(event.key)
    
    def onkeyrelease(self,event):
        if event.key == 'n':
            self.set_zero = False
    
    def relative_plot(self, mult, bounds=None, offset=False):
        delta_t = self.delta_t
        
        if bounds:
            lbound = self.zero_time - bounds[0]
            rbound = self.zero_time + bounds[-1]
        else:
            lbound = self.x_bounds[0]
            rbound = self.x_bounds[-1]

        t = np.arange(-self.zero_time+lbound, rbound-self.zero_time, delta_t) # seconds
        
        s = self.y[int((lbound - self.x[0])/delta_t):int((rbound - self.x[0])/delta_t)].shape[0]
        
        if t.shape[0] > s:
            t = t[0:s]
        #~ elif s > t.shape[0]:
            #~ s = s[0:t.shape[0]]
                
        fig = plt.figure()
        ax = fig.add_subplot(111)
        
        if offset:
            ax.plot(t*mult, self.y[int((lbound - self.x[0])/delta_t):int((rbound - self.x[0])/delta_t)] - self.y[self.zero_ind])
        else:
            ax.plot(t*mult, self.y[int((lbound - self.x[0])/delta_t):int((rbound - self.x[0])/delta_t)])
        
        ax.set_xlim(t[0]*mult, t[-1]*mult)
        
        return fig, ax
    
    def plot(self):
    
        if self.draw:

            self.span = SpanSelector(self.ax, self.onselect, 'horizontal', \
                                     useblit=True, rectprops=dict(alpha=0.5, \
                                     facecolor='red') )

            self.cid = self.fig.canvas.mpl_connect('button_release_event', \
                                                   self.onclick)
        
            self.kp = self.fig.canvas.mpl_connect('key_press_event', \
                                                  self.onkeypress)
        
            self.kr = self.fig.canvas.mpl_connect('key_release_event', \
                                                  self.onkeyrelease)


# class Waveform_Parameters(object):
#     """
#     Class to find waveform parameters (DC offset, risetime, etc.)
#     """
#     def __init__(self, x, y, max_points=np.inf):
#
#         self.x = x
#         self.y = y
#         self.max_points = max_points
#
#     def find_dc_offset(self):
#
#         fig = plt.figure()
#         fig.suptitle('Please select the region to find the offset')
#         ax = fig.add_subplot(111)
#         ax.plot(self.x, self.y, 'b')
#
#         p = plotdf(fig, ax, self.max_points)
#         p.plot()
#         plt.show()
#
#         temp_y = p.y
#         dc_offset = np.mean(temp_y)[0]
#         sigma = np.std(temp_y)[0]
#
#         fig = plt.figure()
#         fig.suptitle(r'DC Offset %0.2f -- $\sigma$ %0.2f' %
#                      (dc_offset, sigma))
#         ax = fig.add_subplot(111)
#         ax.plot(self.x, self.y, 'b')
#         ax.plot([self.x[0], self.x[-1]],
#                 [dc_offset, dc_offset],
#                 'r')
#         ax.plot([self.x[0], self.x[-1]],
#                 [dc_offset + sigma, dc_offset + sigma],
#                 '-r')
#         ax.plot([self.x[0], self.x[-1]],
#                 [dc_offset - sigma, dc_offset - sigma],
#                 '-r')
#
#         return dc_offset, sigma
#
#     def find_rise_time(self, x=self.x, y=self.y, dc_offset=False):
#
#         offset = 0.0
#         sigma = 0.0
#
#         if dc_offset:
#             offset, sigma = find_dc_offset()
#
#         y -= offset
#
#         fig, ax = plt.subplots(1, 1)
#         ax.plot(x, y)
#         plt.title('Calculate Risetime')
#
#         p = plotdf(fig, ax)
#         p.plot()
#         plt.show()
#
#         y = p.ax.get_lines()[0].get_ydata()
#         time = p.ax.get_lines()[0].get_xdata()
#
#         amp = np.max(y)
#
#         t_start = np.argmax(np.abs(1.0/(0.1*amp - y)))
#         t_end = np.argmax(np.abs(1.0/(0.9*amp - y)))
#
#         rise_time = (time[t_end] - time[t_start])
#
#         time *= 1E9
#
#         plt.plot(time, y, '-x')
#         plt.plot(time[t_start], y[t_start], 'ro')
#         plt.plot(time[t_end], y[t_end], 'ro')
#         plt.title('Peak and Risetime')
#
#         ylims = plt.gca().get_ylim()
#         plt.plot([time[t_start], time[t_start]], [ylims[0], ylims[1]], 'r')
#         plt.plot([time[t_end], time[t_end]], [ylims[0], ylims[1]], 'r')
#
#         xlims = plt.gca().get_xlim()
#         plt.plot([xlims[0],xlims[1]], [y[t_start],y[t_start]], 'r')
#         plt.plot([xlims[0],xlims[1]], [y[t_end],y[t_end]], 'r')
#         plt.text((xlims[-1] - xlims[0])/2 + xlims[0],
#                  (ylims[-1] - ylims[0])/2 + ylims[0]+1000,
#                  'Peak = %0.2f kA' % (amp*1.0E-3))
#         plt.text((xlims[-1] - xlims[0])/2 + xlims[0],
#                  (ylims[-1] - ylims[0])/2 + ylims[0],
#                  'Risetime = %0.2f ns' % rise_time)
#
#         plt.show()
#
#         print('RS # %d => %s: %0.2f kA %0.2f ns' % (r_s, meass, amp,
#                                                     rise_time*1.0E9))
    
def main():
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111, axisbg='#FFFFCC')

    x = np.arange(0.0, 5.0, 0.01)
    y = np.sin(2*np.pi*x) + 0.5*np.random.randn(len(x))

    ax.plot(x, y, '-')
    ax.set_ylim(-2,2)
    ax.set_title('Press left mouse button and drag to test')
    
    p=plotdf(fig, ax)
    p.plot()
    
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111, axisbg='#FFFFCC')

    x = np.arange(0.0, 5.0, 0.01)
    y = np.sin(2*np.pi*x) + 0.5*np.random.randn(len(x))

    line = ax.plot(x, y, '-')
    ax.set_ylim(-2,2)
    ax.set_title('Press left mouse button and drag to test')
    
    p1=plotdf(fig, ax)
    p1.plot()

    plt.show()
    

if __name__ == "__main__":
    main()
