#Laboratorio 1 Redes de Computadores
#Fecha de Entrega : 02-05-2022

#Autores :
#       -Rodrigo Escobar Z.
#       -Nicolás Torreblanca M.

# ---- Librerias ----
from ast import For
from math import pi
from traceback import print_tb
import winsound
import scipy.io.wavfile as waves
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
import scipy.signal as segnal

# ---- Item 1 ----
# Se definen los nombres de las notas de voz que se desean leer
nombre_ArchivoRodrigo = "AudioRodrigo_Redes.wav"
nombre_ArchivoNico = "AudioNico_Redes.wav"
# Reproducimos el sonido que vamos a cargar
#winsound.PlaySound(nombre_ArchivoRodrigo, winsound.SND_FILENAME)
#winsound.PlaySound(nombre_ArchivoNico, winsound.SND_FILENAME)

# ---- Item 2 ----
# Leemos el archivo de audio del directorio
FsRodrigo, dataRodrigo = waves.read(nombre_ArchivoRodrigo)
AudioRodrigo = dataRodrigo[:,0]
FsNico, dataNico = waves.read(nombre_ArchivoNico)
AudioNico = dataNico[:,0]

# Tomamos la longitud de la señal
largoAudioRodrigo = len(AudioRodrigo)
largoAudioNico = len(AudioNico)

# Definimos un vector de tiempo de la misma longitud de la señal
arregloRodrigo = np.arange(0,largoAudioRodrigo)/FsRodrigo
arregloNico = np.arange(0,largoAudioNico)/FsNico

# ---- Item 3 ----
# ---- Graficas Tiempo ----
fig,tiempoRodrigo = plt.subplots()
plt.plot(arregloRodrigo,AudioRodrigo)
plt.title('Audio Rodrigo')
plt.xlabel('Tiempo(S)')
plt.ylabel('Audio')
fig,tiempoNico = plt.subplots()
plt.plot(arregloNico,AudioNico)
plt.title('Audio Nicolás')
plt.xlabel('Tiempo(S)')
plt.ylabel('Audio')

# ---- Item 4 ----
# ---- Transformadas de Fourier ----
# Audio Rodrigo
transformadaR = fourier.fft(AudioRodrigo)
preInversaR = transformadaR
absTransformadaR = abs(transformadaR)
absTransformadaR = absTransformadaR[0:largoAudioRodrigo//2]
arregloTransformadaR = (FsRodrigo/largoAudioRodrigo)*np.arange(0,largoAudioRodrigo//2)
fig,frecuenciaRodrigo = plt.subplots()
plt.plot(arregloTransformadaR,absTransformadaR)
plt.title('Transformada de Audio Rodrigo')
plt.xlabel('Frecuencia(Hz)')
plt.ylabel('Amplitud')

# Audio Nicolás
transformadaN = fourier.fft(AudioNico)
preInversaN = transformadaN
absTransformadaN = abs(transformadaN)
absTransformadaN = absTransformadaN[0:largoAudioNico//2]
arregloTransformadaN = (FsNico/largoAudioNico)*np.arange(0,largoAudioNico//2)
fig,frecuenciaNico = plt.subplots()
plt.plot(arregloTransformadaN,absTransformadaN)
plt.title('Transformada de Audio Nicolás')
plt.xlabel('Frecuencia(Hz)')
plt.ylabel('Amplitud')

# ---- Transformadas de Fourier Inversa ----
# Inversa Rodrigo
inversaRodrigo = fourier.ifft(preInversaR, len(preInversaR))
fig,tiempoInversaRodrigo = plt.subplots()
plt.plot(arregloRodrigo,inversaRodrigo)
plt.title('Fourier Inversa de Rodrigo')
plt.xlabel('Tiempo(S)')
plt.ylabel('Audio')

# Inversa Nicolás
inversaNico = fourier.ifft(preInversaN, len(preInversaN))
fig,tiempoInversaNico = plt.subplots()
plt.plot(arregloNico,inversaNico)
plt.title('Fourier Inversa de Nicolás')
plt.xlabel('Tiempo(S)')
plt.ylabel('Audio')

# ---- Item 5 ----
# ---- Espectrograma ----
fig, espectrogramaR = plt.subplots()
espectrogramaR.set_title("Espectrograma de Audio Rodrigo")
Pxx, freqs, bins, imR = espectrogramaR.specgram (AudioRodrigo, NFFT=1024, Fs=FsRodrigo, noverlap=512)
fig.colorbar(imR)
plt.xlabel('Tiempo(S)')
plt.ylabel('Frecuencia(Hz)')
fig, espectrogramaN = plt.subplots()
espectrogramaN.set_title("Espectrograma de Audio Nicolás")
Pxx, freqs, bins, imN = espectrogramaN.specgram(AudioNico, NFFT=1024, Fs=FsNico, noverlap=512)
fig.colorbar(imN)
plt.xlabel('Tiempo(S)')
plt.ylabel('Frecuencia(Hz)')


# ---- Item 7 ----
# Se selecciona la señal de Ruido Violeta y la señal de audio de Rodrigo
# ---- Lectura de Ruido ----
nombre_ArchivoRuido = "Ruido Violeta.wav"
FsRuido, dataRuido = waves.read(nombre_ArchivoRuido)
largoAudioRuido = len(dataRuido)
arregloRuido = np.arange(0,largoAudioRuido)/FsRuido

# ---- Grafica Tiempo Ruido ----
fig,tiempoRuido = plt.subplots()
plt.plot(arregloRuido,dataRuido)
plt.title('Audio Ruido')
plt.xlabel('Tiempo(S)')
plt.ylabel('Audio')

# ---- Transformada de Fourier Ruido ----
transformadaRuido = fourier.fft(dataRuido)
preInversaRuido = transformadaRuido
absTransformadaRuido = abs(transformadaRuido)
absTransformadaRuido = absTransformadaRuido[0:largoAudioRuido//2]
arregloTransformadaRuido = (FsRuido/largoAudioRuido)*np.arange(0,largoAudioRuido//2)
fig,frecuenciaRuido = plt.subplots()
plt.plot(arregloTransformadaRuido,absTransformadaRuido)
plt.title('Transformada de Ruido')
plt.xlabel('Frecuencia(Hz)')
plt.ylabel('Amplitud')

# ---- Transformada de Fourier Inversa Ruido ----
inversaRuido = fourier.ifft(preInversaRuido, len(preInversaRuido))
fig,tiempoInversaRuido = plt.subplots()
plt.plot(arregloRuido,inversaRuido)
plt.title('Fourier Inversa de Ruido')
plt.xlabel('Tiempo(S)')
plt.ylabel('Audio')

# ---- Espectrograma Ruido ----
fig, espectrogramaRuido = plt.subplots()
espectrogramaRuido.set_title("Espectrograma de Ruido")
Pxx, freqs, bins, imRuido = espectrogramaRuido.specgram(dataRuido, NFFT=1024, Fs=FsRuido, noverlap=512)
fig.colorbar(imRuido)
plt.xlabel('Tiempo(S)')
plt.ylabel('Frecuencia(Hz)')

# ---- Generación Señal Ruidosa ----
ruidoRecortado = []
i = 0
while i < len(AudioRodrigo):
    ruidoRecortado.append(dataRuido[i])
    i = i + 1
senalRuidosa = ruidoRecortado + AudioRodrigo
largoSenalRuidosa = len(senalRuidosa)
arregloSenalRuidosa= np.arange(0,largoSenalRuidosa)/FsRodrigo

# ---- Grafica Tiempo Señal Ruidosa ----
fig,tiempoSenalRuidosa = plt.subplots()
plt.plot(arregloSenalRuidosa,senalRuidosa)
plt.title('Audio Señal Ruidosa')
plt.xlabel('Tiempo(S)')
plt.ylabel('Audio')

# ---- Transformada de Fourier Señal Ruidosa ----
transformadaRuidosa = fourier.fft(senalRuidosa)
preInversaRuidosa = transformadaRuidosa
absTransformadaRuidosa = abs(transformadaRuidosa)
absTransformadaRuidosa = absTransformadaRuidosa[0:largoSenalRuidosa//2]
arregloTransformadaRuidosa= (FsRodrigo/largoSenalRuidosa)*np.arange(0,largoSenalRuidosa//2)
fig,bfx = plt.subplots()
plt.plot(arregloTransformadaRuidosa,absTransformadaRuidosa)
plt.title('Transformada de Señal Ruidosa')
plt.xlabel('Frecuencia(Hz)')
plt.ylabel('Amplitud')

# ---- Transformada de Fourier Inversa Señal Ruidosa ----
inversaRuidosa = fourier.ifft(preInversaRuidosa, len(preInversaRuidosa))
fig,tiempoInversaRuidosa = plt.subplots()
plt.plot(arregloSenalRuidosa,inversaRuidosa)
plt.title('Fourier Inversa de Señal Ruidosa')
plt.xlabel('Tiempo(S)')
plt.ylabel('Audio')

# ---- Espectrograma Señal Ruidosa ----
fig, espectrogramaRuidosa = plt.subplots()
espectrogramaRuidosa.set_title("Espectrograma de Señal Ruidosa")
Pxx, freqs, bins, imRuidosa = espectrogramaRuidosa.specgram(senalRuidosa, NFFT=1024, Fs=FsRodrigo, noverlap=512)
fig.colorbar(imRuidosa)
plt.xlabel('Tiempo(S)')
plt.ylabel('Frecuencia(Hz)')

# ---- Item 8 ----
# ---- Filtro ----
cantCoeficientes = 1000
frecuenciaCorte = 2000
frecuenciaNormalizada = 2*frecuenciaCorte/FsRodrigo
largoFiltro = segnal.firwin(cantCoeficientes,frecuenciaNormalizada)
[frecuencia,amplitud] = segnal.freqz(largoFiltro, worN = 118967)
frecuencia = FsRodrigo*frecuencia/(2*pi)

# ---- Filtro en Frecuencias----
plt.figure()
plt.plot(frecuencia, abs(amplitud))
plt.title('Filtro FIR')
plt.xlabel('Frecuencia(Hz)')
plt.ylabel('Amplitud')

# ---- Filtro Aplicado a Señal Ruidosa ----
[frecuencia1,amplitud1] = segnal.freqz(largoFiltro, worN = 237935)
filtradoCompleto = amplitud1 * transformadaRuidosa
filtrado = abs(amplitud) * absTransformadaRuidosa
# absFiltrado = abs(filtrado)

# ---- Transformada de Fourier Señal Filtrada ----
fig,frecuenciaSenalFiltrada = plt.subplots()
plt.plot(arregloTransformadaRuidosa,filtrado)
plt.title('Transformada de Fourier de Señal Filtrada')
plt.xlabel('Frecuencia(Hz)')
plt.ylabel('Amplitud')

# ---- Transformada de Fourier Inversa de Señal Filtrada ----
inversaFiltrada = fourier.ifft(filtradoCompleto, len(filtradoCompleto))
fig,tiempoFiltrada = plt.subplots()
plt.plot(arregloRodrigo,inversaFiltrada)
plt.title('Fourier Inversa de Señal Filtrada')
plt.xlabel('Tiempo(S)')
plt.ylabel('Audio')

# ---- Espectrograma de Señal Filtrada ----
fig, espectrogramaFiltrada = plt.subplots()
espectrogramaFiltrada.set_title("Espectrograma de Señal Filtrada")
Pxx, freqs, bins, imFiltrada = espectrogramaFiltrada.specgram(inversaFiltrada, NFFT=1024, Fs=FsRodrigo, noverlap=512)
fig.colorbar(imFiltrada)
plt.xlabel('Tiempo(S)')
plt.ylabel('Frecuencia(Hz)')

# ---- Item 9 ----
waves.write("audioFiltrado.wav", FsRodrigo, inversaFiltrada.astype(np.int16))
