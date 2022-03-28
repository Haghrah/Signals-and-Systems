#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 20:52:30 2022

@author: arslan
"""

from numpy import (linspace, )
import matplotlib.pyplot as plt

def u(t):
	return (t > 0.) * 1.

def r(t):
	return (t > 0.) * t

x1 = lambda t : r(t) - 2 * r(t - 1.) + r(t - 2.)
x2 = lambda t : r(t + 2) - 2 * r(t + 1) + 2 * r(t) - r(t - 1)


t = linspace(-5., 5., 1000)

xl = -4.0
xr =  4.0
yl = -2.0
yr =  2.0


plt.figure(figsize=(8, 6))

ax1 = plt.subplot(211)
ax1.plot([0., 0., ], [yl, yr, ], color="r", linewidth=2)
ax1.plot([xl, xr, ], [0., 0., ], color="r", linewidth=2)
ax1.plot(t, x1(t), label=r"$x_{1}(t)$")
ax1.legend()
ax1.grid(True)
ax1.set_xlim(xl, xr)
ax1.set_ylim(yl, yr)

ax2 = plt.subplot(223)
ax2.plot([0., 0., ], [yl, yr, ], color="r", linewidth=2)
ax2.plot([xl, xr, ], [0., 0., ], color="r", linewidth=2)
ax2.plot(t, 0.5 * (x1(t) + x1(-t)), label=r"$x^{e}_{1}(t)$")
ax2.legend()
ax2.grid(True)
ax2.set_xlim(xl, xr)
ax2.set_ylim(yl, yr)

ax3 = plt.subplot(224)
ax3.plot([0., 0., ], [yl, yr, ], color="r", linewidth=2)
ax3.plot([xl, xr, ], [0., 0., ], color="r", linewidth=2)
ax3.plot(t, 0.5 * (x1(t) - x1(-t)), label=r"$x^{o}_{1}(t)$")
ax3.legend()
ax3.grid(True)
ax3.set_xlim(xl, xr)
ax3.set_ylim(yl, yr)

plt.show()



plt.figure(figsize=(8, 6))

ax1 = plt.subplot(211)
ax1.plot([0., 0., ], [yl, yr, ], color="r", linewidth=2)
ax1.plot([xl, xr, ], [0., 0., ], color="r", linewidth=2)
ax1.plot(t, x2(t), label=r"$x_{2}(t)$")
ax1.legend()
ax1.grid(True)
ax1.set_xlim(xl, xr)
ax1.set_ylim(yl, yr)

ax2 = plt.subplot(223)
ax2.plot([0., 0., ], [yl, yr, ], color="r", linewidth=2)
ax2.plot([xl, xr, ], [0., 0., ], color="r", linewidth=2)
ax2.plot(t, 0.5 * (x2(t) + x2(-t)), label=r"$x^{e}_{2}(t)$")
ax2.legend()
ax2.grid(True)
ax2.set_xlim(xl, xr)
ax2.set_ylim(yl, yr)

ax3 = plt.subplot(224)
ax3.plot([0., 0., ], [yl, yr, ], color="r", linewidth=2)
ax3.plot([xl, xr, ], [0., 0., ], color="r", linewidth=2)
ax3.plot(t, 0.5 * (x2(t) - x2(-t)), label=r"$x^{o}_{2}(t)$")
ax3.legend()
ax3.grid(True)
ax3.set_xlim(xl, xr)
ax3.set_ylim(yl, yr)

plt.show()
















