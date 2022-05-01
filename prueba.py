from ast import For
from traceback import print_tb
import winsound
import scipy.io.wavfile as waves
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fourier

# nombre_ArchivoRodrigo = "AudioRodrigo_Redes.wav"
# nombre_ArchivoNico = "AudioNico_Redes.wav"
# # Reproducimos el sonido que vamos a cargar
# #winsound.PlaySound(nombre_ArchivoRodrigo, winsound.SND_FILENAME)
# #winsound.PlaySound(nombre_ArchivoNico, winsound.SND_FILENAME)

# # Leemos el archivo de audio del directorio
# FsRodrigo, dataRodrigo = waves.read(nombre_ArchivoRodrigo)
# AudioRodrigo = dataRodrigo[:,0]
# FsNico, dataNico = waves.read(nombre_ArchivoNico)
# AudioNico = dataNico[:,0]

# # Tomamos la longitud de la señal == NUMERO DE MUESTRAS
# largoAudioRodrigo = len(AudioRodrigo)
# largoAudioNico = len(AudioNico)

# # Definimos un vector de tiempo de la misma longitud de la señal
# arregloRodrigo = np.arange(0,largoAudioRodrigo)/FsRodrigo
# arregloNico = np.arange(0,largoAudioNico)/FsNico

# ---- Graficas Tiempo ----
# fig,ax = plt.subplots()
# plt.plot(arregloRodrigo,AudioRodrigo)
# plt.title('Audio Rodrigo')
# plt.xlabel('Tiempo(S)')
# plt.ylabel('Audio')
# fig,bx = plt.subplots()
# plt.plot(arregloNico,AudioNico)
# plt.title('Audio Nico')
# plt.xlabel('Tiempo(S)')
# plt.ylabel('Audio')

# # ---- Graficas Frecuencia ----
# transformadaR = fourier.fft(AudioRodrigo)
# print(transformadaR)
# absTransformadaR = abs(transformadaR)
# print('\n')
# print(absTransformadaR)
# absTransformadaR = absTransformadaR[0:largoAudioRodrigo//2]
# print('\n')
# print(absTransformadaR)
# arregloTransformadaR = (FsRodrigo/largoAudioRodrigo)*np.arange(0,largoAudioRodrigo//2)
# fig,afx = plt.subplots()
# plt.plot(arregloTransformadaR,absTransformadaR)
# plt.title('Transformada Rodrigo')
# plt.xlabel('Frecuencia')
# plt.ylabel('Amplitud')

# transformadaN = fourier.fft(AudioNico)
# absTransformadaN = abs(transformadaN)
# absTransformadaN = absTransformadaN[0:largoAudioNico//2]
# arregloTransformadaN = (FsNico/largoAudioNico)*np.arange(0,largoAudioNico//2)
# fig,bfx = plt.subplots()
# plt.plot(arregloTransformadaN,absTransformadaN)
# plt.title('Transformada Nico')
# plt.xlabel('Frecuencia')
# plt.ylabel('Amplitud')


# # ---- Inversa de Fourier ----
# inversa = fourier.ifft(absTransformadaR)
# inversa = inversa[0:largoAudioRodrigo//2]
# arregloInversa = (FsRodrigo/largoAudioRodrigo)*np.arange(0,largoAudioRodrigo//2)
# fig,iafx = plt.subplots()
# plt.plot(arregloInversa,inversa)
# plt.title('Inversa Rodrigo')

# # ---- Espectrograma ----
# N = largoAudioRodrigo #Numero de puntos de la fft
# from scipy import signal
# plt.specgram(arregloRodrigo, NFFT=N, Fs=FsRodrigo,window = signal.blackman(N),noverlap = 128)
# plt.title('Espectrograma con Matplotlib',size=16)
# plt.ylabel('Frecuencia [Hz]')
# plt.xlabel('Tiempo [Seg]')
# plt.colorbar()

# ---- Espectrograma FUNCIONA ----
# plt.rcParams["figure.figsize"] = (14,8)
# FsRodrigo, dataRodrigo = waves.read('AudioRodrigo_Redes.wav')
# FsNico, dataNico = waves.read('AudioNico_Redes.wav')
# AudioRodrigo = dataRodrigo[:,0]
# AudioNico = dataNico[:,0]
# fig, (ax3, ax4) = plt.subplots (nrows=2)
# ax3.set_title("Spectrogram of audioRodrigo")
# Pxx, freqs, bins, im = ax3.specgram (AudioRodrigo, NFFT=1024, Fs=FsRodrigo, noverlap=512)
# ax4.set_title("Spectrogram of audioNico")
# Pxx, freqs, bins, im = ax4.specgram(AudioNico, NFFT=1024, Fs=FsNico, noverlap=512)
# plt.show()


# # ---- RUIDO ----
# nombre_ArchivoRuido = "Ruido Marrón.wav"
# FsRuido, dataRuido = waves.read(nombre_ArchivoRuido)
# largoAudioRuido = len(dataRuido)
# arregloRuido = np.arange(0,largoAudioRuido)/FsRuido

# # ---- Graficas Tiempo ----
# fig,bx = plt.subplots()
# plt.plot(arregloRuido,dataRuido)
# plt.title('Audio Ruido')
# plt.xlabel('Tiempo(S)')
# plt.ylabel('Audio')

# FsRuido1, dataRuido1 = waves.read('Ruido Marrón.wav')
# copiaRuido = []
# i = 0
# while i < len(AudioRodrigo):
#     copiaRuido.append(dataRuido1[i])
#     i = i + 1
# suma = copiaRuido + AudioRodrigo
# largoSuma = len(suma)
# arregloSuma= np.arange(0,largoSuma)/FsRodrigo
# fig,cx = plt.subplots()
# plt.plot(arregloSuma,suma)
# plt.title('Audio Suma')
# plt.xlabel('Tiempo(S)')
# plt.ylabel('Audio')


# ---- Espectrograma RUIDO FUNCIONA  ----
# plt.rcParams["figure.figsize"] = (14,8)
# FsRodrigo, dataRodrigo = waves.read('AudioRodrigo_Redes.wav')
# AudioRodrigo = dataRodrigo[:,0]
# fig, ax3, = plt.subplots()
# ax3.set_title("Spectrogram of Suma")
# Pxx, freqs, bins, im = ax3.specgram (suma, NFFT=1024, Fs=FsRodrigo, noverlap=512)
# fig.colorbar(im)
# plt.show()









