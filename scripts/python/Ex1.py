#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 18:45:56 2023

@author: arslan
"""


from numpy import (exp, cos, heaviside, linspace, arange, )
import matplotlib.pyplot as plt


class discreteSignal:
    
    def __init__(self, continuous, T):
        self.continuous = continuous
        self.T = T
        
    def __call__(self, n):
        return self.continuous(n * self.T)
    
    def __getitem__(self, n):
        return self(n)

def x(t):
    return exp(-0.2 * t) * cos(t) * heaviside(t, 1)

T = 0.5
y = discreteSignal(x, T)

l = -5
r = 20
p = (r - l) * 10
t = linspace(l, r, p)
n = arange(l / T, r / T + 1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
fig.suptitle("Sampling from a continuous signal")
ax1.plot(t, x(t), label="Contiuous")
ax1.legend()
ax1.grid(True)
ax2.stem(T * n, y[n], label="Discrete")
ax2.legend()
ax2.grid(True)
plt.show()











