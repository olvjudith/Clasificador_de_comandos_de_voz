# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 00:47:59 2020

@author: olvju
"""
'''
https://www.youtube.com/watch?v=F1TNkJMgMBE
https://www.youtube.com/watch?v=q-N6IcgCqCE&lc=UgyC6pgFvN9fOAlcMU14AaABAg.97vYT1608TL97vZ9L1LGKE
'''
import speech_recognition as sr
import time

comandos = []

for i in range(26):
        
    r = sr.Recognizer()
    '''
    Se crea una nueva instancia de la clase Recognizer
    '''

    with sr.AudioFile('C:\\Users\\olvju\\Documents\\8.Optativa profesionalizante II\\Audios\\grabacion'+str(i+1)+'.wav') as source:
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
            comandos.append(text)
            time.sleep(1)
            print(text)            
            
        except:
            print("I am sorry! I can not understand!")
            '''
            El bloque try - except es para controlar
            aquellos casos donde ocurra un error a la hora de
            capturar o de entender que hace el usurio
            '''
archivo="basededatos.csv"
csv=open(archivo,"w")
'''
En la variable archivo se pone el nombre del archivo .csv
y se abre, la w es para señalar que se va a escribir en él
'''
titulo="Lista de comandos\n"
csv.write(titulo)
'''
Se escribe el título en el archivo .csv
'''
for i in range(26):
    csv.write(comandos[i]+"\n") 
