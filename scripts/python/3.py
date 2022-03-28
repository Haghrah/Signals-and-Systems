#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 20:52:30 2022

@author: arslan
"""

from numpy import (arange, array, abs, )
import matplotlib.pyplot as plt


u = lambda n : (n >= 0) * 1.0


d = {-4:-1., 
	 -3:-0.5, 
	 -2: 0.5, 
	 -1: 1.0, 
	  0: 1.0, 
	  1: 1.0, 
	  2: 1.0, 
	  3: 0.5}

d_ = lambda n : d[n] if n in d.keys() else 0.
x = lambda n : array(list(map(d_, n)))




n = arange(-10, 10)


plt.figure()
xl = -8.0
xr =  8.0
yl = -2.0
yr =  2.0
ax = plt.subplot(111)
ax.stem(n, x(n), use_line_collection=True, label=r"$x[n]$")
ax.legend()
ax.grid(True)
ax.set_xlim(xl, xr)
ax.set_ylim(yl, yr)
plt.show()

plt.figure()
xl = -8.0
xr =  8.0
yl = -2.0
yr =  2.0
ax = plt.subplot(111)
ax.stem(n, x(n) * u(3 - n), use_line_collection=True, label=r"$x_{1}[n]$")
ax.legend()
ax.grid(True)
ax.set_xlim(xl, xr)
ax.set_ylim(yl, yr)
plt.show()



plt.figure()
xl = -8.0
xr =  8.0
yl = -2.0
yr =  2.0
ax = plt.subplot(111)
ax.stem(n, 0.5 * x(n) + 0.5 * (-1) ** abs(n) * x(n), use_line_collection=True, label=r"$x_{2}[n]$")
ax.legend()
ax.grid(True)
ax.set_xlim(xl, xr)
ax.set_ylim(yl, yr)
plt.show()



plt.figure()
xl = -8.0
xr =  8.0
yl = -2.0
yr =  2.0
ax = plt.subplot(111)
ax.stem(n, x((n - 1) ** 2.), use_line_collection=True, label=r"$x_{3}[n]$")
ax.legend()
ax.grid(True)
ax.set_xlim(xl, xr)
ax.set_ylim(yl, yr)
plt.show()











