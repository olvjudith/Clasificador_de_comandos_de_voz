# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 00:47:59 2020

@author: olvju
"""
import speech_recognition as sr
import time

r = sr.Recognizer()
'''
Se crea una nueva instancia de la clase Recognizer
'''

with sr.AudioFile('C:\\Users\\olvju\\Documents\\8.Optativa profesionalizante II\\Audios\\grabacion1.wav') as source:
    '''
    Para que el archivo .wav sea la fuente de
    datos que vaya a capturar las palabras a decir se ocupa la clase
    AudioFile
    '''
    audio = r.listen(source)
    
    '''
    Para capturar el audio se utiliza
    el método listen que está presente
    en la clase Recognizer, esto hasta que
    se detecte un silencio
    '''

    try:
        print("Reading audio file. Please, wait a moment...")
        text = r.recognize_google(audio, language='es-ES')
        time.sleep(1.5)
        print(text)
    except:
        print("I am sorry! I can not understand!")
        '''
    El bloque try - except es para controlar
    aquellos casos donde ocurra un error a la hora de
    capturar o de entender que hace el usurio
    '''

