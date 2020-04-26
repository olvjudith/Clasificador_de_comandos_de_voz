# -*- coding: utf-8 -*-
#https://chatbotslife.com/text-classification-using-algorithms-e4d50dcba45
"""
Created on Sat Mar 14 01:25:08 2020

@author: Judith
"""
# usa el kit de herramientas de lenguaje natural
import nltk
#nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
# word stemmer
stemmer = LancasterStemmer()

# 4 clases de datos de entrenamiento
training_data = [] #datos de entrenamiento
training_data.append({"class":"activar", "sentence":"activar modo fiesta"})
training_data.append({"class":"activar", "sentence":"activar acondicionador"})
training_data.append({"class":"activar", "sentence":"activar modo relajacion"})
training_data.append({"class":"activar", "sentence":"prender aspersores"})
training_data.append({"class":"activar", "sentence":"activar encendedor"})
training_data.append({"class":"activar", "sentence":"prender luces"})

training_data.append({"class":"apagar", "sentence":"Apagar modo fiesta"})
training_data.append({"class":"apagar", "sentence":"Apagar acondicionador"})
training_data.append({"class":"apagar", "sentence":"Apagar modo relajacion"})
training_data.append({"class":"apagar", "sentence":"Apagar aspersores"})
training_data.append({"class":"apagar", "sentence":"Apagar encendedor"})
training_data.append({"class":"apagar", "sentence":"Apagar luces"})

training_data.append({"class":"aumentar", "sentence":"sube la velocidad"})
training_data.append({"class":"aumentar", "sentence":"sube el vidrio"})
training_data.append({"class":"aumentar", "sentence":"aumenta el volumen"})
training_data.append({"class":"aumentar", "sentence":"aumenta la temperatura"})
training_data.append({"class":"aumentar", "sentence":"sube el asiento"})
training_data.append({"class":"aumentar", "sentence":"sube la llanta"})

training_data.append({"class":"disminuir", "sentence":"disminuye la velocidad"})
training_data.append({"class":"disminuir", "sentence":"baja el vidrio"})
training_data.append({"class":"disminuir", "sentence":"baja el volumen"})
training_data.append({"class":"disminuir", "sentence":"disminuye la temperatura"})
training_data.append({"class":"disminuir", "sentence":"baja el asiento"})
training_data.append({"class":"disminuir", "sentence":"baja la llanta"})

#print ("%s sentences of training data" % len(training_data))
#salida 24 sentences of training data
#--------------------------------------------------------------------
#organizacion de datose estructuras para trabajar algoritmicamente

# captura palabras derivadas únicas en el corpus de entrenamiento
corpus_words = {}
class_words = {}
# convierte una lista en un conjunto (de elementos únicos) y luego una lista nuevamente (esto elimina los duplicados)
classes = list(set([a['class'] for a in training_data]))
for c in classes:
    # prepara una lista de palabras dentro de cada clase
    class_words[c] = []

# recorrer cada oración en nuestros datos de entrenamiento
for data in training_data:
    # tokenizar/dividir cada oración en palabras
    for word in nltk.word_tokenize(data['sentence']):
        # ignorar algunos caracteres
        if word not in ["?", "'s"]:
            # raiz y minúsculas cada palabra
            stemmed_word = stemmer.stem(word.lower())
             # ¿No hemos visto esta palabra ya?
            if stemmed_word not in corpus_words:
                corpus_words[stemmed_word] = 1
            else:
                corpus_words[stemmed_word] += 1

            # agrega la palabra a nuestras palabras en la lista de clase
            class_words[data['class']].extend([stemmed_word])

## ahora tenemos cada palabra derivada y el número de ocurrencias de la palabra en nuestro corpus de entrenamiento (la comunalidad de la palabra)
#print ("Corpus words and counts: %s \n" % corpus_words)
#corpus_words cuantas veces se repite la raiz de la palabra
# también tenemos todas las palabras en cada clase
#print ("Class words: %s" % class_words)
#class_words cada clase y la lista de palabras derivadas que contiene 
#--------------------------------------------------------------------
# calcular una puntuación para una clase determinada
# def calculate_class_score(sentence, class_name, show_details=True):
#     score = 0
#     # tokenizar cada palabra en nuestra nueva oración
#     for word in nltk.word_tokenize(sentence):
#         # verifica si la raíz de la palabra está en alguna de nuestras clases
#         if stemmer.stem(word.lower()) in class_words[class_name]:
#             # trata cada palabra con el mismo peso
#             score += 1
            
#             if show_details:
#                 print ("   match: %s" % stemmer.stem(word.lower() ))
#     return score
#--------------------------------------------------------------------
# calcular una puntuación para una clase dada teniendo en cuenta la comunidad de palabras
def calculate_class_score(sentence, class_name, show_details=True):
    score = 0
     # tokenizar cada palabra en nuestra nueva oración
    for word in nltk.word_tokenize(sentence):
        # verifica si la raíz de la palabra está en alguna de nuestras clases
        if stemmer.stem(word.lower()) in class_words[class_name]:
             # tratar cada palabra con peso relativo
            score += (1 / corpus_words[stemmer.stem(word.lower())])

            #if show_details:
                #print ("   match: %s (%s)" % (stemmer.stem(word.lower()), 1 / corpus_words[stemmer.stem(word.lower())]))
    return score
#--------------------------------------------------------------------
# devuelve la clase con la puntuación más alta por oración
def classify(sentence):
    high_class = None
    high_score = 0
    # recorre nuestras clases
    for c in class_words.keys():
        # calcular la puntuación de la oración para cada clase
        score = calculate_class_score(sentence, c, show_details=False)
        # realizar un seguimiento de la puntuación más alta
        if score > high_score:
            high_class = c
            high_score = score
    print ("Class: ",high_class, "Score: ", high_score,"\n")
    return high_class, high_score
#--------------------------------------------------------------------
# ahora podemos calcular una puntuación para una nueva oración
sentence = "aumenta el agua"
classify(sentence)
# ahora podemos encontrar la clase con la puntuación más alta
#for c in class_words.keys():
    #print ("Class: %s  Score: %s \n" % (c, calculate_class_score(sentence, c)))