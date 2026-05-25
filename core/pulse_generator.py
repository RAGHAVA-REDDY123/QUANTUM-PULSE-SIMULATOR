# core/pulse_generator.py
import numpy as np

def generate_pulse(kind,amplitude,frequency,phase,duration,samples):
    t=np.linspace(0,duration,samples)
    if kind=='Gaussian':
        center=duration/2
        sigma=duration/10
        wave=amplitude*np.exp(-((t-center)**2)/(2*sigma**2))
    elif kind=='Square':
        wave=amplitude*np.ones_like(t)
    elif kind=='Sine':
        wave=amplitude*np.sin(2*np.pi*frequency*t)
    else:
        wave=amplitude*np.sin(2*np.pi*frequency*t+np.deg2rad(phase))
    return t,wave

