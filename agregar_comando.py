# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 01:25:08 2020

@author: Judith
"""

#https://es.stackoverflow.com/questions/88274/c%C3%B3mo-puedo-escribir-csv-en-python-3-utilizando-pandas-sin-que-trunque-el-ficher

import pandas as pd

text="ADIOS"
if text.lower() == "adios":
    #creacion =[text]
    #my_df = pd.DataFrame(creacion) 
    print("si")
    #my_df.to_csv('basededatos.csv', mode='a', index=False, header=False,sep=';',decimal=',')
else:
    print("no")

