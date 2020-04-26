# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 22:48:47 2020

@author: olvju
"""
'''
https://programacionpython80889555.wordpress.com/2018/10/16/grabacion-de-sonido-con-pyaudio-ejercicio-basico-en-python/
'''
import pyaudio
import wave

FORMAT=pyaudio.paInt16
'''
Formato de las muestras
'''
CHANNELS=2
'''
Número de canales
'''
CHUNK=1024
'''
Descomposición en 1024 frames, para evitar colapso en el procesado de la muestra
Unidades de memoria.
'''
RATE=44100
'''
44100 frames por segundo
'''
duracion=10
'''
Tiempo que  durará el archivo en segundos
'''
archivo="grabacion.wav"
'''
Asignación del nombre que tendrá el archivo
'''

audio=pyaudio.PyAudio()
'''
Se crea una nueva instancia de la clase py.Audio
'''


stream=audio.open(format=FORMAT,channels=CHANNELS,rate=RATE, input=True,frames_per_buffer=CHUNK)
'''
Se inicia pyAudio con el método, se empieza la grabación
'''

print("grabando...")
'''
Permanecerá el mensaje en pantalla durante la ejecución
del ciclo de lecura y procesamiento de lectura
'''
frames=[]

for i in range(0, int(RATE/CHUNK*duracion)):
    data=stream.read(CHUNK)
    frames.append(data)
    
'''
Ciclo de lectura de sonido
'''
print("grabación terminada")


stream.stop_stream()
'''
Ordena finalizar el procesado de la información
'''
stream.close()
'''
Cierra el procesado de la información
'''
audio.terminate()
'''
Finaliza la ejeción del programa
'''

waveFile = wave.open(archivo, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
'''
Se crea un archivo de audio a partir de la información
recolectada en el ciclo for  anterior
'''

