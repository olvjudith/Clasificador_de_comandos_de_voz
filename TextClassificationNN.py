# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 01:25:08 2020

@author: Judith
"""
#https://machinelearnings.co/text-classification-using-neural-networks-f5cd7b8765c6
#https://github.com/ugik/notebooks/blob/master/Neural_Network_Classifier.ipynb

# usa el kit de herramientas de lenguaje natural
import nltk
from nltk.stem.lancaster import LancasterStemmer
import os
import json
import datetime
import numpy as np
import time
import csv
stemmer = LancasterStemmer()

# 4 clases de datos de entrenamiento
training_data = [] #datos de entrenamiento
comandos=[]
auxiliar=[]
with open('basededatos.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        comandos.append(row)

for i in range(len(comandos)):
    auxiliar.append(comandos[i][0])

training_data=[]
for i in range(len(comandos)-1):
    training_data.append({"class":auxiliar[i+1], "sentence":auxiliar[i+1]})
#print ("%s sentences of training data" % len(training_data))
#--------------------------------------------------------------------
#organizacion de datos y estructuras para trabajar algoritmicamente
words = []
classes = []
documents = []
ignore_words = ['?']
# recorre cada oración en nuestros datos de entrenamiento
for pattern in training_data:
    # # tokenizar/dividir cada palabra en la oración
    w = nltk.word_tokenize(pattern['sentence'])
     # agregar a nuestra lista de palabras, es como un diccionario
    words.extend(w)
     # agregar a documentos en nuestro corpus
     #cada palabra derivada y el número de ocurrencias
    documents.append((w, pattern['class']))
     # agregar a nuestra lista de clases
     #cada clase y la lista de palabras derivadas que contiene
    if pattern['class'] not in classes:
        classes.append(pattern['class'])

# detener y poner en minuscula cada palabra y eliminar duplicados, raíz
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = list(set(words))

# eliminar duplicados
classes = list(set(classes))

print (len(documents), "documents")
print (len(classes), "classes", classes)
print (len(words), "unique stemmed words", words)

#--------------------------------------------------------------------
# crea nuestros datos de entrenamiento
training = []
output = []
# crear una matriz vacía para nuestra salida
output_empty = [0] * len(classes)

# conjunto de entrenamiento, bolsa de palabras para cada oración
for doc in documents:
    # inicializar nuestra bolsa de palabras
    bag = []
    # lista de palabras tokenizadas/divididas para el patrón
    pattern_words = doc[0]
     # raiz de  cada palabra
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    # crear nuestra matriz de bolsa de palabras
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    training.append(bag)
    # salida es un '0' para cada etiqueta y '1' para la etiqueta actual
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    output.append(output_row)

print ("# words", len(words))
print ("# classes", len(classes))
# # sample training/output
i = 0
w = documents[i][0]
#raices de la oración
print ([stemmer.stem(word.lower()) for word in w])
#coincidencia de las raices en la bolsa(1 si es igual)
print (training[i])
#pone un 1 a la clase pertenece
print (output[i])
#--------------------------------------------------------------------
# calcular la no linealidad sigmoidea
def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output
'''
la salida es la función de sigmoid evaluada en x
''' 

# convierte la salida de la función sigmoide a su derivada
def sigmoid_output_to_derivative(output):
    return output*(1-output)
 
def clean_up_sentence(sentence):
    # tokenizar/dividir el patrón/ divide la oración en palabras
    sentence_words = nltk.word_tokenize(sentence)
    # minusculas de cada palabra
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# conjunto de bolsa de palabras de retorno: 0 o 1 por cada palabra en la bolsa 
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bolsa de palabras
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))
##********************************THINK
def think(sentence, show_details=False):
    x = bow(sentence.lower(), words, show_details)
    if show_details:
        print ("sentence:", sentence, "\n bow:", x)
    # capa de entrada es nuestra bolsa de palabras
    l0 = x
    # multiplicación matricial de entrada y capa oculta
    l1 = sigmoid(np.dot(l0,synapse_0))
    # capa de salida
    l2 = sigmoid(np.dot(l1, synapse_1))
    return l2
##################_____________________
#--------------------------------------------------------------------
# función de entrenamiento de redes neuronales para crear pesos sinápticos/ multiplicación matricial
    # ANN and Gradient Descent code from https://iamtrask.github.io//2015/07/27/python-network-part2/
def train(X, y, hidden_neurons=10, alpha=1, epochs=50000, dropout=False, dropout_percent=0.5):

    print ("Training with %s neurons, alpha:%s, dropout:%s %s" % (hidden_neurons, str(alpha), dropout, dropout_percent if dropout else '') )
    #("Entrenamiento con% s neuronas, alfa:% s, abandono:
    print ("Input matrix: %sx%s    Output matrix: %sx%s" % (len(X),len(X[0]),1, len(classes)) )
    #("Matriz de entrada:% sx% s Matriz de salida
    np.random.seed(1)

    last_mean_error = 1
     # inicializa aleatoriamente nuestros pesos con media 0
    synapse_0 = 2*np.random.random((len(X[0]), hidden_neurons)) - 1
    synapse_1 = 2*np.random.random((hidden_neurons, len(classes))) - 1

    prev_synapse_0_weight_update = np.zeros_like(synapse_0)
    prev_synapse_1_weight_update = np.zeros_like(synapse_1)

    synapse_0_direction_count = np.zeros_like(synapse_0)
    synapse_1_direction_count = np.zeros_like(synapse_1)
        
    for j in iter(range(epochs+1)):

       # Avance a través de las capas 0, 1 y 2
        layer_0 = X
        layer_1 = sigmoid(np.dot(layer_0, synapse_0))
                
        if(dropout):
            layer_1 *= np.random.binomial([np.ones((len(X),hidden_neurons))],1-dropout_percent)[0] * (1.0/(1-dropout_percent))

        layer_2 = sigmoid(np.dot(layer_1, synapse_1))

        # ¿cuánto perdimos el valor objetivo?
        layer_2_error = y - layer_2

        if (j% 10000) == 0 and j > 5000:
            # si el error de esta iteración de 10k es mayor que la última iteración, explotar
            if np.mean(np.abs(layer_2_error)) < last_mean_error:
                print ("delta after "+str(j)+" iterations:" + str(np.mean(np.abs(layer_2_error))) )
                last_mean_error = np.mean(np.abs(layer_2_error))
            else:
                print ("break:", np.mean(np.abs(layer_2_error)), ">", last_mean_error )
                break
                
        # ¿en qué dirección está el valor objetivo?
        # ¿Estábamos realmente seguros? si es así, no cambies demasiado
        layer_2_delta = layer_2_error * sigmoid_output_to_derivative(layer_2)

        # ¿Cuánto contribuyó cada valor l1 al error l2 (de acuerdo con los pesos)?
        layer_1_error = layer_2_delta.dot(synapse_1.T)

        
        # ¿en qué dirección está el objetivo l1?
        # ¿Estábamos realmente seguros? si es así, no cambies demasiado
        layer_1_delta = layer_1_error * sigmoid_output_to_derivative(layer_1)
        
        synapse_1_weight_update = (layer_1.T.dot(layer_2_delta))
        synapse_0_weight_update = (layer_0.T.dot(layer_1_delta))
        
        if(j > 0):
            synapse_0_direction_count += np.abs(((synapse_0_weight_update > 0)+0) - ((prev_synapse_0_weight_update > 0) + 0))
            synapse_1_direction_count += np.abs(((synapse_1_weight_update > 0)+0) - ((prev_synapse_1_weight_update > 0) + 0))        
        
        synapse_1 += alpha * synapse_1_weight_update
        synapse_0 += alpha * synapse_0_weight_update
        
        prev_synapse_0_weight_update = synapse_0_weight_update
        prev_synapse_1_weight_update = synapse_1_weight_update

    now = datetime.datetime.now()

    # persisten las sinapsis
    synapse = {'synapse0': synapse_0.tolist(), 'synapse1': synapse_1.tolist(),
               'datetime': now.strftime("%Y-%m-%d %H:%M"),
               'words': words,
               'classes': classes
              }
    synapse_file = "synapses.json"

    with open(synapse_file, 'w') as outfile:
        json.dump(synapse, outfile, indent=4, sort_keys=True)
    print ("saved synapses to:", synapse_file)
#_-------------------
    ##################_____________________
    #construccion del modelo de la red neuronal
X = np.array(training)
y = np.array(output)

start_time = time.time()

train(X, y, hidden_neurons=20, alpha=0.1, epochs=100000, dropout=False, dropout_percent=0.2)

elapsed_time = time.time() - start_time
print ("processing time:", elapsed_time, "seconds")
#_-------------------
# umbral de probabilidad
ERROR_THRESHOLD = 0.2
# cargar nuestros valores de sinapsis calculados
synapse_file = 'synapses.json' 
with open(synapse_file) as data_file: 
    synapse = json.load(data_file) 
    synapse_0 = np.asarray(synapse['synapse0']) 
    synapse_1 = np.asarray(synapse['synapse1'])

def classify(sentence, show_details=False):
    results = think(sentence, show_details)

    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD ] 
    results.sort(key=lambda x: x[1], reverse=True) 
    return_results =[[classes[r[0]],r[1]] for r in results]
    print ("%s \n classification: %s" % (sentence, return_results))
    return return_results

classify("activar sonaja")
classify("adios auto")
classify("subir vidrio")
print ()
classify("activar ruido", show_details=True)
