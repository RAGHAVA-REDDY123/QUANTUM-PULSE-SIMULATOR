# core/fft_analysis.py
import numpy as np

def compute_fft(waveform,sampling_frequency):
    fft_values=np.abs(np.fft.fft(waveform))
    fft_freq=np.fft.fftfreq(len(waveform),1/sampling_frequency)
    mask=fft_freq>=0
    return fft_freq[mask],fft_values[mask]
