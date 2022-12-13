"""This file is for extracting phase angle i thing in rads."""
import numpy as np
import pandas as pd
from pathlib import Path
file_path = Path("/home/dtos_experiment/Documents/Potentiostat-arduino/putty.log")
if not file_path.exists():
    file_path = Path('D:/your/path/to/putty.log')

with open(file_path) as f:
    # f = f.readlines()
    df = pd.DataFrame([line.strip().split() for line in f.readlines()])
    # df = pd.DataFrame(f,
    #                   columns=['Volt', 'Ampere'])
print(df[1])
print(df.shape)
spectrum = np.fft.fft(df[1])
mag = np.abs(spectrum)
phase = np.angle(spectrum)
print(f"The mean phase across I (2nd column of data) is {phase.mean()*(2*np.pi)}")
