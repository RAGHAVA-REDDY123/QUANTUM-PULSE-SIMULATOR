# core/sequence_builder.py
import numpy as np
from core.pulse_generator import generate_pulse

def build_sequence(pulses,amplitude,frequency,phase,duration,samples):
    sequence=[]
    segment_duration=duration/len(pulses)
    segment_samples=samples//len(pulses)
    for pulse in pulses:
        _,wave=generate_pulse(pulse,amplitude,frequency,phase,segment_duration,segment_samples)
        sequence.extend(wave)
    return np.array(sequence)

