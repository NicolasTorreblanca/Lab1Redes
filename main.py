from ast import For
from math import pi
from traceback import print_tb
import winsound
import scipy.io.wavfile as waves
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
import scipy.signal as segnal


nombre_ArchivoRodrigo = "AudioRodrigo_Redes.wav"
# nombre_ArchivoNico = "AudioNico_Redes.wav"
# # Reproducimos el sonido que vamos a cargar
# #winsound.PlaySound(nombre_ArchivoRodrigo, winsound.SND_FILENAME)
# #winsound.PlaySound(nombre_ArchivoNico, winsound.SND_FILENAME)

# # Leemos el archivo de audio del directorio
FsRodrigo, dataRodrigo = waves.read(nombre_ArchivoRodrigo)
AudioRodrigo = dataRodrigo[:,0]
# FsNico, dataNico = waves.read(nombre_ArchivoNico)
# AudioNico = dataNico[:,0]

# # Tomamos la longitud de la señal == NUMERO DE MUESTRAS
largoAudioRodrigo = len(AudioRodrigo)
# largoAudioNico = len(AudioNico)

# # Definimos un vector de tiempo de la misma longitud de la señal
arregloRodrigo = np.arange(0,largoAudioRodrigo)/FsRodrigo
# arregloNico = np.arange(0,largoAudioNico)/FsNico

# # ---- Graficas Tiempo ----
fig,ax = plt.subplots()
plt.plot(arregloRodrigo,AudioRodrigo)
plt.title('Audio Rodrigo')
plt.xlabel('Tiempo(S)')
plt.ylabel('Audio')
# fig,bx = plt.subplots()
# plt.plot(arregloNico,AudioNico)
# plt.title('Audio Nico')
# plt.xlabel('Tiempo(S)')
# plt.ylabel('Audio')

# # ---- Graficas Frecuencia ----
transformadaR = fourier.fft(AudioRodrigo)
#print(transformadaR)
absTransformadaR = abs(transformadaR)

copiaTransformadaR = transformadaR

#print('\n')
#print(absTransformadaR)
absTransformadaR = absTransformadaR[0:largoAudioRodrigo//2]
# print('\n')
#print(absTransformadaR)
arregloTransformadaR = (FsRodrigo/largoAudioRodrigo)*np.arange(0,largoAudioRodrigo//2)
fig,afx = plt.subplots()
plt.plot(arregloTransformadaR,absTransformadaR)
plt.title('Transformada Rodrigo')
plt.xlabel('Frecuencia')
plt.ylabel('Amplitud')

# INVERSA
inversa = fourier.ifft(copiaTransformadaR, len(copiaTransformadaR))
fig,jx = plt.subplots()
plt.plot(arregloRodrigo,inversa)
plt.title('Audio Rodrigo DE INVERSA')
plt.xlabel('Tiempo(S)')
plt.ylabel('Audio')
# plt.show()

# transformadaN = fourier.fft(AudioNico)
# absTransformadaN = abs(transformadaN)
# absTransformadaN = absTransformadaN[0:largoAudioNico//2]
# arregloTransformadaN = (FsNico/largoAudioNico)*np.arange(0,largoAudioNico//2)
# fig,bfx = plt.subplots()
# plt.plot(arregloTransformadaN,absTransformadaN)
# plt.title('Transformada Nico')
# plt.xlabel('Frecuencia')
# plt.ylabel('Amplitud')
# plt.show()


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
# nombre_ArchivoRuido = "Ruido Violeta.wav"
# FsRuido, dataRuido = waves.read(nombre_ArchivoRuido)
# largoAudioRuido = len(dataRuido)
# arregloRuido = np.arange(0,largoAudioRuido)/FsRuido

# transformadaRuido = fourier.fft(dataRuido)
# absTransformadaRuido = abs(transformadaRuido)
# absTransformadaRuido = absTransformadaRuido[0:largoAudioRuido//2]
# arregloTransformadaRuido = (FsRuido/largoAudioRuido)*np.arange(0,largoAudioRuido//2)
# fig,bfx = plt.subplots()
# plt.plot(arregloTransformadaRuido,absTransformadaRuido)
# plt.title('Transformada Ruido')
# plt.xlabel('Frecuencia')
# plt.ylabel('Amplitud')




# # ---- Graficas Tiempo ----
# fig,bx = plt.subplots()
# plt.plot(arregloRuido,dataRuido)
# plt.title('Audio Ruido')
# plt.xlabel('Tiempo(S)')
# plt.ylabel('Audio')

FsRuido1, dataRuido1 = waves.read('Ruido Violeta.wav')
copiaRuido = []
i = 0
while i < len(AudioRodrigo):
    copiaRuido.append(dataRuido1[i])
    i = i + 1
suma = copiaRuido + AudioRodrigo
largoSuma = len(suma)
arregloSuma= np.arange(0,largoSuma)/FsRodrigo
fig,cx = plt.subplots()
plt.plot(arregloSuma,suma)
plt.title('Audio Suma')
plt.xlabel('Tiempo(S)')
plt.ylabel('Audio')

# ---- Espectrograma RUIDO FUNCIONA  ----
# plt.rcParams["figure.figsize"] = (14,8)
# FsRodrigo, dataRodrigo = waves.read('AudioRodrigo_Redes.wav')
# AudioRodrigo = dataRodrigo[:,0]
# fig, ax3, = plt.subplots()
# ax3.set_title("Spectrogram of Suma")
# Pxx, freqs, bins, im = ax3.specgram (suma, NFFT=1024, Fs=FsRodrigo, noverlap=512)
# fig.colorbar(im)
# plt.show()

transformadaSuma = fourier.fft(suma)
copiaTransformadaSuma = transformadaSuma
absTransformadaSuma = abs(transformadaSuma)
absTransformadaSuma = absTransformadaSuma[0:largoSuma//2]
arregloTransformadaSuma = (FsRodrigo/largoSuma)*np.arange(0,largoSuma//2)
fig,bfx = plt.subplots()
plt.plot(arregloTransformadaSuma,absTransformadaSuma)
plt.title('Transformada Suma')
plt.xlabel('Frecuencia')
plt.ylabel('Amplitud')
#plt.show()

# ---- Filtro ----
# segnal.firwin(numtaps, f, pass_zero=False)
 # Design IIR butterworth filter
# newFs = FsRodrigo
# n = 5
# fc = 2000
# w_c= 2*fc/newFs

# [b,a] = segnal.butter(n,w_c)
# # Frequency response
# [w,h] = segnal.freqz (b,a,worN = 512)
# w = newFs*w/(2*pi)

# h_db = 20*np.log10(abs(h))
# plt.figure()
# plt.plot(w, h_db); plt.xlabel('Frequency (Hz)')
# plt.ylabel('Magnitude (dB)')
# plt.show()

newFs = FsRodrigo
N = 1000
fc = 2000
w_c = 2*fc/newFs
t = segnal.firwin(N,w_c)

[w,h] = segnal.freqz(t, worN = 118967)
[w1,h1] = segnal.freqz(t, worN = 237935)
w = newFs*w/(2*pi)
h_db = 20*np.log10(abs(h))
plt.figure()
plt.plot(w, abs(h))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')

# print(len(abs(h)))
# # plt.show()

filtradoCompleto = h1 * transformadaSuma
filtrado = abs(h) * absTransformadaSuma
# absFiltrado = abs(filtrado)
fig,zfx = plt.subplots()
plt.plot(arregloTransformadaSuma,filtrado)
plt.title('Transformada Filtrado')
plt.xlabel('Frecuencia')
plt.ylabel('Amplitud')


# INVERSA FILTRADO
inversaFiltrado = fourier.ifft(filtradoCompleto, len(filtradoCompleto))
fig,jx = plt.subplots()
plt.plot(arregloRodrigo,inversaFiltrado)

plt.title('Audio Filtrado DE INVERSA')
plt.xlabel('Tiempo(S)')
plt.ylabel('Audio')
# plt.show()

#237935
#118967



samplerate = 48000
fs = FsRodrigo
t = np.linspace(0., 1., samplerate)
# amplitude = np.iinfo(np.int16).max
# data = amplitude * np.sin(2. * np.pi * fs * t)
waves.write("prueba1.wav", samplerate, inversaFiltrado.astype(np.int16))


