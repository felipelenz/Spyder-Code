# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:22:46 2015

@author: lenz
"""
import numpy as np
import matplotlib.pyplot as plt

Diode1=np.arange(0,5000003,1.0)
Diode1=np.fromfile("/Volumes/Promise 12TB RAID5/2014 Data/081314/Diode1_UF1451_RS4.bin",dtype=float)

Diode2=np.arange(0,5000003,1.0)
Diode2=np.fromfile("/Volumes/Promise 12TB RAID5/2014 Data/081314/Diode2_UF1451_RS4.bin",dtype=float)

plt.plot(Diode1)
plt.show()