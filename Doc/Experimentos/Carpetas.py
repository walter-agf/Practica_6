#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 04:50:45 2020

@author: gualteros
"""
import os
import io
directorio_actual = os.getcwd()
#print (directorio_actual)
retorno = directorio_actual.rfind("/")
directorio_actual = directorio_actual[:retorno]
#print (directorio_actual)
#print ("\n",os.listdir(directorio_actual))
directorio = (directorio_actual+"/Base")
#print (directorio)
#print ("\n",os.listdir(directorio))
municipios = open(directorio+"/municipios.txt","r")
#print (municipios.read())
municipios.seek(0)
lista_municipios = municipios.readlines()
#print("\n",lista_municipios)
key = []
for i in range(0,len(lista_municipios)):
    lista = []
    lista.append(lista_municipios[i][:-1])
    lista_municipios[i] = lista
    key.append(i+1)
print("\n",lista_municipios)
print ("\n",key)
dic_municipios = dict(zip(key,lista_municipios))
print ("\n",dic_municipios)
municipios.close()
