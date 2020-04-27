# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 19:05:26 2020

@author: olvju
"""
'''
https://code.tutsplus.com/es/tutorials/how-to-read-and-write-csv-files-in-python--cms-29907
'''
import csv
comandos=[]
auxiliar=[]
test=[]
with open('basededatos.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        comandos.append(row)

for i in range(len(comandos)):
    auxiliar.append(comandos[i][0])

training=[]
for i in range(len(comandos)-1):
    training.append({"class":auxiliar[i+1], "sentence":auxiliar[i+1]})
print ("%s sentences of training data" % len(training))
print(training[25])


        


