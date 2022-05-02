import winsound
import scipy.io.wavfile as waves
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fourier

#nombre_ArchivoNico = "AudioNico_Redes.wav"
#winsound.PlaySound(nombre_ArchivoNico,winsound.SND_FILENAME)

nombre_ArchivoRodrigo = "AudioRodrigo_Redes.wav"
winsound.PlaySound(nombre_ArchivoRodrigo,winsound.SND_FILENAME)

#FsNico,dataNico = waves.read(nombre_ArchivoNico)
#audio_Nico = data[:,0]

FsRodrigo,dataRodrigo = waves.read(nombre_ArchivoRodrigo)
audio_Rodrigo = dataRodrigo[:,0]

#largoAudioNico = len(audio_Nico)
largoAudioRodrigo = len(audio_Rodrigo)
#t = 6/311040
#arreglo = t*np.arange(0,largo)
arregloRodrigo = np.arange(0,1)/FsRodrigo

fig,ax = plt.subplots()
plt.plot(arregloRodrigo,audio_Rodrigo)
plt.xlabel('Tiempo(S)')
plt.ylabel('Audio')
plt.show()

'''
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
'''

