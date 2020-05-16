#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 05:54:31 2020

@author: gualteros
"""
x = []
x.append(1010101010)
x.append(1111111111)
x.append(1212121212)
x.append(1313131313)
x.append(1231231233)
x.append(3254235434)
print ("\n",x)
z = []
z.append(["Mariana Montoya",1234,"Administrador"])
z.append(["Elkin Perez",1234,"Operador"])
z.append(["Camila Serna",1234,"Administrador"])
z.append(["Oscar Jaramillo",1234,"Operador"])
z.append(["Juan Carlos Sierra",123123,"Administrador"])
z.append(["Sebastián Isaza",77777,"Administrador"]) 
print ("\n",z)
a = zip(x,z)
for i in a:
    print ("\n",i)

