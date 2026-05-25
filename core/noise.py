# core/noise.py
import numpy as np

def add_noise(waveform,noise_level):
    noise=np.random.normal(0,noise_level,len(waveform))
    return waveform+noise


