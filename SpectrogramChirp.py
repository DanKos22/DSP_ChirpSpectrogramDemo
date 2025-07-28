# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:31:25 2025

@author: G00397054@atu.ie
"""

# -*- coding: utf-8 -*-
"""
@author: Dan Koskiranta

https://en.wikipedia.org/wiki/Chirp
https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.signal.chirp.html
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp

# Make a 'chirp' signal
f0 = 1
f1 = 1000
t1 = 1
duration = 0.2

# Add code, f0 = 
# Add code, f1 =
#t1 = 1
# Add code, duration =
fs = 4096
n = np.arange(int(duration*fs))
t = np.linspace(0, duration, num=int(duration*fs), endpoint=True)
# Add code, x = sp....
x = sp.chirp(t, f0, t1, f1, method = 'linear', phi = 0, vertex_zero= True)

# Get spectrogram, using SciPy
freqsSp, timeSp, specSp = sp.spectrogram(x, fs, nfft= 20498, nperseg= 128, noverlap=28)
# Add code, freqsSp, timeSp, specSp = sp.spectrogram(...)
# Compute spectrogram magnitudes in decibels
specSp_db = 10*np.log10(specSp)
# Add code, specSp_db = ...(specSp)

# Plot original chirp signal & its spectrogram
fig = plt.figure(figsize=(16,14))
ax = fig.add_subplot(211)
ax.plot(n/fs, x, color='k')
ax.set_title("Signal", fontsize=20, pad=15)
ax.set_xlabel("Time (s)", fontsize=16, labelpad=5)
ax.set_ylabel("Amplitude", fontsize=16, labelpad=5)
ax.tick_params(axis='both', which='both', labelsize=14, length=3, pad=10)
ax = fig.add_subplot(212)
ax.set_title("Spectrogram", fontsize=20, pad=15)
# Add code plt.pcolormesh(..., ..., ..., cmap=plt.cm.gist_yarg, vmin=-30, shading='auto')
plt.pcolormesh(timeSp, freqsSp, specSp_db, cmap=plt.cm.gist_yarg, vmin=-30, shading='auto')
ax.set_ylim([0, fs/2])
ax.set_ylim([0, 500])
ax.set_xlabel("Time (s)", fontsize=16, labelpad=5)
ax.set_ylabel("Frequency (Hz)", fontsize=16, labelpad=5)
ax.tick_params(axis='both', which='both', labelsize=14, length=3, pad=10)
cb = plt.colorbar(orientation="horizontal")
cb.set_label("Amplitude (dB)", fontsize=16, labelpad=10)
fig.subplots_adjust(hspace=0.5)
plt.tight_layout()
plt.show()