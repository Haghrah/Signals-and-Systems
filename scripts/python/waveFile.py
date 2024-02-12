#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 15:22:29 2023

@author: arslan
"""

from scipy.io.wavfile import (read, write, )
from scipy.signal import (butter, lfilter, )
from numpy.random import (random, )
from numpy import (int16, float32)
import matplotlib.pyplot as plt

def butter_lowpass(cutoff, fs, order=5):
    return butter(order, cutoff, fs=fs, btype="low", analog=False)

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

if __name__ == "__main__":
    wave = read("1.wav")
    freq = wave[0]
    audio = wave[1]
    
    noise = (40000 * (random(audio.shape) - 0.5)).astype(int16)
    newAudio = audio + noise
    write("2.wav", freq, newAudio)
    
    denoised = butter_lowpass_filter(newAudio.astype(float32), 2.2e4, freq, 10)
    write("3.wav", freq, denoised.astype(int16))
    
    
    
    
























