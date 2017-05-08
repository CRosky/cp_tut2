#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 11:37:28 2017

@author: rosky
"""

import numpy as np
import matplotlib.pyplot as plt

def gauss(x,x0,sig):
    I = np.complex(0,1)
    return np.exp(-0.5*I*(x-x0)**2/sig**2)

def conv(array, key):
    f=gauss(array,0,1)
    g=0*array; g[key]=1
    ft1=np.fft.fft(f)
    ft2=np.fft.fft(g)
    return (np.fft.ifft(ft1*ft2))

def corr(arr1,arr2,key):
    f=gauss(arr1,0,1)
    g=conv(arr1,key)
    ftf=np.fft.fft(f)
    ftg=np.fft.fft(g)
    return np.fft.ifft(ftf*np.conj(ftg))

a = np.arange(-10,10,0.1)
k = len(a)/2

y=gauss(a,0,1)
z=conv(a,k)

y_corr=corr(a,a,k)


plt.plot(y_corr)

