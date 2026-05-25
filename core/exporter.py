# core/exporter.py
import pandas as pd
import json

def waveform_csv(time,waveform):
    df=pd.DataFrame({'time':time,'waveform':waveform})
    return df.to_csv(index=False)

def config_json(config):
    return json.dumps(config,indent=2)

