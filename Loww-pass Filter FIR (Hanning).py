import numpy as np
import scipy.signal as signal
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

# Fungsi untuk membuat filter lowpass FIR
def design_lowpass_fir(numtaps, cutoff, fs):
    nyquist = 0.5 * fs
    norm_cutoff = cutoff / nyquist
    taps = signal.firwin(numtaps, norm_cutoff, window='hann', pass_zero=True)
    return taps

# Baca file WAV
input_wav_path = r'C:\Users\T530 ThinkPad\Documents\VS CODE\UAS PSD\Input.wav'
output_wav_path = r'C:\Users\T530 ThinkPad\Documents\VS CODE\UAS PSD\Output\Output_Hanning.wav'
fs, data = wavfile.read(input_wav_path)

# Pastikan data adalah array 1D
if data.ndim > 1:
    data = data[:, 0]

# Desain filter
numtaps = 101  # Panjang filter
cutoff_freq = 1000  # Frekuensi cutoff dalam Hz
taps = design_lowpass_fir(numtaps, cutoff_freq, fs)

# Terapkan filter ke sinyal
filtered_data = signal.lfilter(taps, 1.0, data)

# Simpan hasil sinyal terfilter ke file WAV
wavfile.write(output_wav_path, fs, filtered_data.astype(np.int16))

# Plot sinyal asli dan hasil filter
plt.figure(figsize=(14, 10))

plt.subplot(4, 1, 1)
plt.plot(data)
plt.title('Sinyal Asli')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

plt.subplot(4, 1, 2)
plt.plot(filtered_data)
plt.title('Sinyal Setelah Filter')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

# Plot impulse response
plt.subplot(4, 1, 3)
plt.plot(taps)
plt.title('Impulse Response')
plt.xlabel('Tap')
plt.ylabel('Amplitude')

# Plot frequency response
w, h = signal.freqz(taps, worN=8000)
plt.subplot(4, 1, 4)
plt.plot(0.5*fs*w/np.pi, np.abs(h))
plt.title('Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')

plt.tight_layout()
plt.show()
