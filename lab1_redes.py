#Laboratorio 1 Redes de Computadores
#Date : 02-05-2022

#Authors :
#       -Rodrigo Escobar Z.
#       -Nicolás Torreblanca M.

# ---- Librarys ----
from ast import For
from math import pi
from traceback import print_tb
import winsound
import scipy.io.wavfile as waves
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
import scipy.signal as segnal

# ---- Item 1 ---

# Define the file Names that are going to be read

fileName_Rodrigo = "AudioRodrigo_Redes.wav"
fileName_Nico = "AudioNico_Redes.wav"

# Play the audio

#winsound.PlaySound(nombre_ArchivoRodrigo, winsound.SND_FILENAME)
#winsound.PlaySound(nombre_ArchivoNico, winsound.SND_FILENAME)

# ---- Item 2 ----

# We read the files previously defined

FsRodrigo, dataRodrigo = waves.read(fileName_Rodrigo)
AudioRodrigo = dataRodrigo[:,0]
FsNico, dataNico = waves.read(fileName_Nico)
AudioNico = dataNico[:,0]

# Then, we take the length of the signal

lengthAudioRodrigo = len(AudioRodrigo)
lengthAudioNico = len(AudioNico)

# The, we define a vector of the same length of time

timeArrayRodrigo = np.arange(0,lengthAudioRodrigo)/FsRodrigo
timeArrayNico = np.arange(0,lengthAudioNico)/FsNico

# ---- Item 3 ----

# ---- Time Graphs ----

# We plot a graph for each audio

fig,timeRodrigo = plt.subplots()
plt.plot(timeArrayRodrigo,AudioRodrigo)
plt.title('Audio Rodrigo')
plt.xlabel('Time(S)')
plt.ylabel('Audio')
fig,timeNico = plt.subplots()
plt.plot(timeArrayNico,AudioNico)
plt.title('Audio Nicolás')
plt.xlabel('Time(S)')
plt.ylabel('Audio')

# ---- Item 4 ----

# ---- Fourier Transforms ----

# Transform for Audio Rodrigo
# Apply the Transform Using FFT(Fourier Fast Transform)
# Then, we compute the absolute value of the transform
# Also we create an array to Store to plot the Frequency

transformR = fourier.fft(AudioRodrigo)
preInverseR = transformR
abstransformR = abs(transformR)
abstransformR = abstransformR[0:lengthAudioRodrigo//2]
arraytransformR = (FsRodrigo/lengthAudioRodrigo)*np.arange(0,lengthAudioRodrigo//2)
fig,frequencyRodrigo = plt.subplots()
plt.plot(arraytransformR,abstransformR)
plt.title('Fourier Transform of Audio Rodrigo')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')

# We repeat the same Process For Nicolas

transformN = fourier.fft(AudioNico)
preInverseN = transformN 
abstransformN  = abs(transformN)
abstransformN = abstransformN[0:lengthAudioNico//2]
arraytransformN  = (FsNico/lengthAudioNico)*np.arange(0,lengthAudioNico//2)
fig,frequencyNico = plt.subplots()
plt.plot(arraytransformN ,abstransformN)
plt.title('Fourier Transform of Audio Nicolás')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')

# ---- Fourier Inverses ----

# We compute the fourier inverse for audio Rodrigo 
# In this case, we call the function ifft to make the inverse

inverseRodrigo = fourier.ifft(preInverseR, len(preInverseR))
fig,timeInverseRodrigo = plt.subplots()
plt.plot(timeArrayRodrigo,inverseRodrigo)
plt.title('Fourier Inverse of Audio Rodrigo')
plt.xlabel('Time(S)')
plt.ylabel('Audio')

# Then, We do the same for audio Nicolas 

inverseNico = fourier.ifft(preInverseN, len(preInverseN))
fig,timeInverseNico = plt.subplots()
plt.plot(timeArrayNico,inverseNico)
plt.title('Fourier Inverse of Audio de Nicolás')
plt.xlabel('Time(S)')
plt.ylabel('Audio')

# ---- Item 5 ----

# ---- Spectogram ----

# Plotting an spectogram for each audio

# One for rodrigo

fig, spectrogramR = plt.subplots()
spectrogramR.set_title("Spectrogram of Audio Rodrigo")
Pxx, freqs, bins, imR = spectrogramR.specgram (AudioRodrigo, NFFT=1024, Fs=FsRodrigo, noverlap=512)
fig.colorbar(imR)
plt.xlabel('Time(S)')
plt.ylabel('Frequency(Hz)')

# Another one for Nicolas 

fig, spectrogramN = plt.subplots()
spectrogramN.set_title("Spectrogram of Audio Nicolás")
Pxx, freqs, bins, imN = spectrogramN.specgram(AudioNico, NFFT=1024, Fs=FsNico, noverlap=512)
fig.colorbar(imN)
plt.xlabel('Time(S)')
plt.ylabel('Frequency(Hz)')


# ---- Item 7 ----

# We select an violet Noice for the experiment
# This noice is going to be added to audio Rodrigo
# In order to create a noisy Signal

# ---- Noise ----

# First, we read the signal 

fileName_Noise = "Ruido Violeta.wav"
FsNoise, dataNoise = waves.read(fileName_Noise)
lengthAudioNoise = len(dataNoise)
timeArrayNoise = np.arange(0,lengthAudioNoise)/FsNoise

# ----Plotting the noise signal In time----
fig,tiempoRuido = plt.subplots()
plt.plot(timeArrayNoise,dataNoise)
plt.title('Audio of Noise')
plt.xlabel('Time(S)')
plt.ylabel('Audio')

# ---- Fourier Transform of Noice ----

# Repeat the execution we made for audio rodrigo
# But for the Noice previously read

transformNoise = fourier.fft(dataNoise)
preInverseNoise = transformNoise
abstransformNoise = abs(transformNoise)
abstransformNoise = abstransformNoise[0:lengthAudioNoise//2]
arraytransformNoise = (FsNoise/lengthAudioNoise)*np.arange(0,lengthAudioNoise//2)
fig,frecuenciaRuido = plt.subplots()
plt.plot(arraytransformNoise,abstransformNoise)
plt.title('Fourier Transform of Noise Audio')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')

# ---- Inverse Fourier Transform of Noise----

inverseNoise = fourier.ifft(preInverseNoise, len(preInverseNoise))
fig,tiempoInversaRuido = plt.subplots()
plt.plot(timeArrayNoise,inverseNoise)
plt.title('Fourier Inverse of Noise Audio')
plt.xlabel('Time(S)')
plt.ylabel('Audio')

# ---- Spectogram of Noise ----
fig, spectrogramNoise = plt.subplots()
spectrogramNoise.set_title("Spectrogram of Noise Audio")
Pxx, freqs, bins, imNoise = spectrogramNoise.specgram(dataNoise, NFFT=1024, Fs=FsNoise, noverlap=512)
fig.colorbar(imNoise)
plt.xlabel('Time(S)')
plt.ylabel('Frequency(Hz)')

# ---- Generación Señal Ruidosa ----

# A task given is to create a signal that contains
# the noise and one of the audios readed.

# In order to achieve this, we create an array
# an store every element of the noise in order
# to create an array that has the same length of
# the array of audio.


cuttedNoise = []
i = 0
while i < len(AudioRodrigo):
    cuttedNoise.append(dataNoise[i])
    i = i + 1

# With this achieved, we can create the noisySignal
# A signal that contains both Audio of one Author and
# The Noise

noisySignal = cuttedNoise + AudioRodrigo
lengthNoisySignal = len(noisySignal)
arrayNoisySignal= np.arange(0,lengthNoisySignal)/FsRodrigo

# ---- Plotting the Noisy Signal----

fig,timeNoisySignal = plt.subplots()
plt.plot(arrayNoisySignal,noisySignal)
plt.title('Noisy Signal')
plt.xlabel('Time(S)')
plt.ylabel('Audio')

# We repeat the execution made with the others audios.
# To be more accurate, we make an Fourier Transform
# Fourier Inverse and Spectogram of the Noisy Signal

# ---- Fourier Transform of Noisy Signal----

transformNoisySignal = fourier.fft(noisySignal)
preInverseNoisySignal = transformNoisySignal 
absTransformNoisySignal = abs(transformNoisySignal)
absTransformNoisySignal = absTransformNoisySignal[0:lengthNoisySignal//2]
arrayTransformNoisySignal= (FsRodrigo/lengthNoisySignal)*np.arange(0,lengthNoisySignal//2)
fig,bfx = plt.subplots()
plt.plot(arrayTransformNoisySignal,absTransformNoisySignal)
plt.title('Fourier Transform of Noisy Signal')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')

# ---- Fourier Inverse Noisy Signal ----

inverseNoisySignal = fourier.ifft(preInverseNoisySignal, len(preInverseNoisySignal))
fig,tiempoInversaRuidosa = plt.subplots()
plt.plot(arrayNoisySignal,inverseNoisySignal)
plt.title('Fourier Inverse of Noisy Signal')
plt.xlabel('Time(S)')
plt.ylabel('Audio')

# ---- Spectrogram Noisy Signal ----

fig, spectrogramnoisySignal = plt.subplots()
spectrogramnoisySignal.set_title("Spectogram of Noisy Signal")
Pxx, freqs, bins, imnoisySignal = spectrogramnoisySignal.specgram(noisySignal, NFFT=1024, Fs=FsRodrigo, noverlap=512)
fig.colorbar(imnoisySignal)
plt.xlabel('Time(S)')
plt.ylabel('Frequency(Hz)')

# ---- Item 8 ----

# We utilize an filter Fir to find a new signal that filters the violet Noice

# To apply the filter, we need to define this filter

# ---- Filter Definition ----

# We compute a number of Coeficientes and a frequency Cut
# For the filter
number_Coeficients = 1000
frequencyCut = 2000
frequencyNormalized = 2*frequencyCut/FsRodrigo

# Given this parameters, we can create our filter FIR

lengthFilter = segnal.firwin(number_Coeficients,frequencyNormalized)
[frequencyFilter,amplitudeFilter] = segnal.freqz(lengthFilter, worN = 118967)
frequencyFilter = FsRodrigo*frequencyFilter/(2*pi)

# ---- Plotting our Filter----

plt.figure()
plt.plot(frequencyFilter, abs(amplitudeFilter))
plt.title('FIR Filter')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')

# ---- Using the filter in the NoisySignal-----

# Its important to know that the filter is created previously
# is an Fourier Transform. Then we can apply the convolution
# property of a the fourier transform of aconvolution is the result of multiply 2 
# Fourier Transform. To create the filter we are basically making a convolution

[frequencyFilterComplete,amplitudeFilterComplete] = segnal.freqz(lengthFilter, worN = 237935)
filterComplete = amplitudeFilterComplete * transformNoisySignal
filterHalf = abs(amplitudeFilter) * absTransformNoisySignal

# absFiltrado = abs(filtrado)

# We plot the fourier transform obtained from the filter

# ---- Fourier Transform of filtered Signal----

fig,frequencyNoisySignal = plt.subplots()
plt.plot(arrayTransformNoisySignal,filterHalf)
plt.title('Fourier Transform of Filtered Signal')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')

#  Then we can apply the inverse, to get an playable audio.
# ---- Fourier Inverse of filtered Signal----

inverseFiltered = fourier.ifft(filterComplete, len(filterComplete))
fig,timeFiltered = plt.subplots()
plt.plot(timeArrayRodrigo,inverseFiltered)
plt.title('Fourier Inverse of Filtered Signal')
plt.xlabel('Time(S)')
plt.ylabel('Audio')

# With the inverse, we can calculate the Spectogram
# ---- Spectogram of Filtered Signal ----


fig, spectrogramFiltered = plt.subplots()
spectrogramFiltered.set_title("Spectogram of Filtered Signal")
Pxx, freqs, bins, imFiltrada = spectrogramFiltered.specgram(inverseFiltered, NFFT=1024, Fs=FsRodrigo, noverlap=512)
fig.colorbar(imFiltrada)
plt.xlabel('Time(S)')
plt.ylabel('Frequency(Hz)')

# ---- Item 9 ----

# Also with the inverse, we have an audio that is playable for the user.

waves.write("audioFiltrado.wav", FsRodrigo, inverseFiltered.astype(np.int16))

# Finally we show every graph made during the evaluation.
plt.show()
