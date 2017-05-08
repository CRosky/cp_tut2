#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 08:07:57 2017

@author: rosky
"""

import numpy as np
import matplotlib.pyplot as plt

def gauss(x,x0,sig):
    I = np.complex(0,1)
    return np.exp(-0.5*I*(x-x0)**2/sig**2)

    
def corr(arr1,arr2):
    f=gauss(arr1,0,1)
    g=gauss(arr2,0,1)
    ftf=np.fft.fft(f)
    ftg=np.fft.fft(g)
    return np.fft.ifft(ftf*np.conj(ftg))


a = np.arange(-10,10,0.1)
y=corr(a,a)


plt.plot(y)