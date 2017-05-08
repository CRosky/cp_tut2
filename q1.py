#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 07:26:10 2017

@author: rosky
"""

from numpy import arange, exp, real, abs
from numpy.fft import fft,ifft
from matplotlib import pyplot as plt

def gauss(x,x0,sig):
    return exp(-0.5*(x-x0)**2/sig**2)

def conv(array, key):
    f=gauss(array,0,1)
    g=0*array; g[key]=1
    ft1=fft(f)
    ft2=fft(g)
    return real(ifft(ft1*ft2))

x = arange(-10,10,0.1)
k = len(x)/2

y = gauss(x,0,1)
y_conv = conv(x,k)

plt.plot(x,y,'r')
plt.plot(x,abs(y_conv),'k')
plt.show()

