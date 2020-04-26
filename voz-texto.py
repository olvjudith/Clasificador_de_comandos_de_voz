# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:24:35 2020

@author: olvju
"""

import speech_recognition as sr

r = sr.Recognizer()
'''
Se crea una nueva instancia de la clase Recognizer
'''

with sr.Microphone() as source:
    '''
    Para que el micrófono por defecto del sistema sea la fuente de
    datos que vaya a capturar las palabras a decir se ocupa la clase
    Microphone
    '''
    print("Say something...")
    '''
    Mensaje para avisar al usuario que se empieza a
    capturar el audio
    '''
    audio = r.listen(source)
    '''
    Para capturar el audio se utiliza
    el método listen que está presente
    en la clase Recognizer, esto hasta que
    se detecte un silencio
    '''
    
    try:
        text = r.recognize_google(audio, language='es-Es')
        print("What did you say_ {}".format(text))
    except:
        print("I am sorry! I can't understand!")
    '''
    El bloque try - except es para controlar
    aquellos casos donde ocurra un error a la hora de
    capturar o de entender que hace el usurio
    '''

'https://www.youtube.com/watch?v=KcjHfnCteZg'