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

x = lambda t : - u(t + 2) + r(t + 2) - r(t + 1) + u(t + 1) + u(t) - u(t - 1) - r(t - 1) + r(t - 2)



t = linspace(-20., 20., 10000)

plt.figure(figsize=(10, 4))
xl = -8.0
xr =  8.0
yl = -2.0
yr =  4.0
ax2 = plt.subplot(111)
ax2.plot([0., 0., ], [yl, yr, ], color="r", linewidth=2)
ax2.plot([xl, xr, ], [0., 0., ], color="r", linewidth=2)
ax2.plot(t, x(2. - t), label=r"$x_{1}(t)$")
ax2.legend()
ax2.grid(True)
ax2.set_xlim(xl, xr)
ax2.set_ylim(yl, yr)
plt.show()


plt.figure(figsize=(10, 4))
xl = -2.0
xr = 14.0
yl = -2.0
yr =  4.0
ax3 = plt.subplot(111)
ax3.plot([0., 0., ], [yl, yr, ], color="r", linewidth=2)
ax3.plot([xl, xr, ], [0., 0., ], color="r", linewidth=2)
ax3.plot(t, x(4. - t / 2.), label=r"$x_{2}(t)$")
ax3.legend()
ax3.grid(True)
ax3.set_xlim(xl, xr)
ax3.set_ylim(yl, yr)
plt.show()


plt.figure(figsize=(10, 4))
xl = -4.0
xr =  4.0
yl = -1.0
yr =  1.0
ax4 = plt.subplot(111)
ax4.plot([0., 0., ], [yl, yr, ], color="r", linewidth=2)
ax4.plot([xl, xr, ], [0., 0., ], color="r", linewidth=2)
ax4.plot([-1.5, -1.5, ], [0., x(-1.5), ], color="C0")
ax4.plot([+1.5, +1.5, ], [0., x(+1.5), ], color="C0")
ax4.scatter([-1.5, ], [x(-1.5), ], marker="v", color="C0")
ax4.scatter([ 1.5, ], [x( 1.5), ], marker="^", color="C0", label=r"$x_{3}(t)$")
ax4.legend()
ax4.grid(True)
ax4.set_xlim(xl, xr)
ax4.set_ylim(yl, yr)
plt.show()


plt.figure(figsize=(10, 4))
xl = -8.0
xr =  8.0
yl = -2.0
yr =  4.0
ax5 = plt.subplot(111)
ax5.plot([0., 0., ], [yl, yr, ], color="r", linewidth=2)
ax5.plot([xl, xr, ], [0., 0., ], color="r", linewidth=2)
ax5.plot(t, (x(t) + x(-t)) * u(t), label=r"$x_{4}(t)$")
ax5.legend()
ax5.grid(True)
ax5.set_xlim(xl, xr)
ax5.set_ylim(yl, yr)
plt.show()



















