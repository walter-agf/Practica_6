#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 08:51:53 2020

@author: gualteros
"""
"""
Haga una función en Python que reciba un string que contiene 
un texto y retorne otro string en el que solo aparezcan los 
números del texto original. Por ejemplo, si el string que 
recibe la función es:

"El cerebro humano tiene unas 86.000.000.000 neuronas. 
El elefante africano tiene 3 veces más."

La función debe retornar:

"860000000003"

Nota: Se sugiere utilizar la función isdigit() 
que determina si un caracter es un dígito o no.
"""
def num_in_str(word):
    resul = ""
    for i in range (0,len(word)):
        s = word[i].isdigit()
        if s == True:
            resul += word[i]
    return resul



palabra = (input("Ingrese un texto : "))
resultado = num_in_str(palabra)
print ("\nEl resultado final es :\n")
print (resultado)