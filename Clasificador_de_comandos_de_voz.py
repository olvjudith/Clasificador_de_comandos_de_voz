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
import speech_recognition as sr
import time
import pandas as pd
import TextClassificationNN

comandos = []

def Recepcion_comando():
    FORMAT=pyaudio.paInt16
    CHANNELS=2
    CHUNK=1024
    RATE=44100
    duracion=4
    archivo="grabacion0.wav"
    audio=pyaudio.PyAudio()
    stream=audio.open(format=FORMAT,channels=CHANNELS,rate=RATE, input=True,frames_per_buffer=CHUNK)
    print("Dictar comando...")
    frames=[]
    for i in range(0, int(RATE/CHUNK*duracion)):
        data=stream.read(CHUNK)
        frames.append(data)
    
    print("Comando capturado")
    print("------------------------------------------------------")
    stream.stop_stream()
    stream.close()
    audio.terminate()
    waveFile = wave.open(archivo, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    
Recepcion_comando()

def Comando_a_texto():
    r = sr.Recognizer()
    with sr.AudioFile('grabacion0.wav') as source:
        audio = r.listen(source)
        try:
            print("Espera un momento...")
            text = r.recognize_google(audio, language='es-ES')
            comandos.append(text)
            time.sleep(1)
            print("El comando que se capturó fue "+text)
            print("------------------------------------------------------")
            
        except:
            print("I am sorry! I can not understand!")
    return text

auxiliar=Comando_a_texto()
    
if auxiliar.lower() == "agregar comando":
    print("A continuación podrá dictar el nuevo comando")
    Recepcion_comando()
    auxiliar=Comando_a_texto()
    comando_agregado =[auxiliar]
    my_df = pd.DataFrame(comando_agregado) 
    my_df.to_csv('basededatos.csv', mode='a', index=False, header=False,sep=';',decimal=',')
else:
    print("Clasificando comando...")
    TextClassificationNN.classify(auxiliar, show_details=True)
