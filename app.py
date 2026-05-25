# quantum_pulse_simulator/app.py
import streamlit as st
import matplotlib.pyplot as plt
from core.pulse_generator import generate_pulse
from core.noise import add_noise
from core.fft_analysis import compute_fft
from core.sequence_builder import build_sequence
from core.exporter import waveform_csv,config_json

st.set_page_config(page_title='Quantum Pulse Signal Generator Simulator',layout='wide')
st.title('Quantum Pulse Signal Generator Simulator')
st.caption('Microwave pulse waveform simulation for quantum control experimentation')

pulse_type=st.sidebar.selectbox('Pulse Type',['Gaussian','Square','Sine','Phase Shifted'])
amplitude=st.sidebar.slider('Amplitude',0.1,5.0,1.0)
frequency=st.sidebar.slider('Frequency (GHz simulated)',1.0,10.0,5.0)
phase=st.sidebar.slider('Phase (degrees)',0,360,90)
duration=st.sidebar.slider('Pulse Duration',1.0,20.0,5.0)
samples=st.sidebar.slider('Sampling Points',500,10000,2000)
noise_level=st.sidebar.slider('Noise Level',0.0,1.0,0.1)

if st.sidebar.button('Generate Simulation'):
    t,wave=generate_pulse(pulse_type,amplitude,frequency,phase,duration,samples)
    noisy_wave=add_noise(wave,noise_level)
    xf,yf=compute_fft(noisy_wave,samples/duration)
    sequence=build_sequence([pulse_type,'Gaussian','Sine'],amplitude,frequency,phase,duration,samples)

    tab1,tab2,tab3,tab4=st.tabs(['Waveform','FFT Analysis','Pulse Sequence','Export'])

    with tab1:
        fig=plt.figure(figsize=(10,4))
        plt.plot(t,wave,label='Clean Signal')
        plt.plot(t,noisy_wave,label='Noisy Signal')
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.legend()
        st.pyplot(fig)

    with tab2:
        fig=plt.figure(figsize=(10,4))
        plt.plot(xf,yf)
        plt.xlabel('Frequency')
        plt.ylabel('Magnitude')
        plt.title('FFT Spectrum')
        st.pyplot(fig)

    with tab3:
        fig=plt.figure(figsize=(10,4))
        plt.plot(sequence)
        plt.xlabel('Sample Index')
        plt.ylabel('Amplitude')
        plt.title('Multi-Pulse Sequence')
        st.pyplot(fig)

    with tab4:
        config={
            'pulse_type':pulse_type,
            'amplitude':amplitude,
            'frequency':frequency,
            'phase':phase,
            'duration':duration,
            'samples':samples,
            'noise_level':noise_level
        }
        st.download_button('Download Waveform CSV',waveform_csv(t,noisy_wave),'waveform.csv')
        st.download_button('Download Config JSON',config_json(config),'config.json')

else:
    st.info('Configure parameters and click Generate Simulation.')

