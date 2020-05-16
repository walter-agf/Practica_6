#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 09:19:25 2020

@author: gualteros
"""
def contar(w):
    cont = 0
    for i in range (0,len(w)):
        if w[i] == "," :
            cont += 1
            if w[i+1] == ",":
                cont -= 1
    return cont
word = (input("Ingrese un texto : "))
cant = contar(word)
print ("\n",cant)

a = (input("Ingrese el nombre del archivo: "))
arch = open(a)
t = 0
for i in arch:
    t += 1
print (t)
for a in range (0,t):
    print (arch.read(a))