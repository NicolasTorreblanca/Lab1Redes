import winsound
import scipy.io.wavfile as waves
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fourier


nombre_ArchivoNico = "AudioNico_Redes.wav"

winsound.PlaySound(nombre_ArchivoNico,winsound.SND_FILENAME)

Fs,data = waves.read(nombre_ArchivoNico)
audio_m = data[:,0]

largo = len(audio_m)
t = 6/311040
arreglo = t*np.arange(0,largo)

fig,ax = plt.subplots()
plt.plot(arreglo,audio_m)
plt.xlabel('Tiempo(S)')
plt.ylabel('Audio')

gk = fourier.fft(audio_m)
m_gk = abs(gk)
m_gk = m_gk[0:largo//2]

F = (Fs/largo)*np.arange(0,largo//2)
fig,bx = plt.subplots()
plt.plot(F,m_gk)
plt.xlabel('Frecuencia')
plt.ylabel('Amplitud')

plt.show()

