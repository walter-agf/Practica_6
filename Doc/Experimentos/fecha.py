#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:25:13 2020

@author: gualteros
"""
import datetime
ahora = datetime.datetime.now()
print(ahora)
print(type(ahora))
ahora = ahora.strftime("%Y/%m/%d %H:%M:%S")
print (ahora)
print (type(ahora))
print ("\n")
x = datetime.date.toordinal().year
print (x)
