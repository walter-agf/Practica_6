#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 22:13:54 2020

@author: gualteros
"""
ingreso = open(directorio+"/ingreso.txt","r")
#print ("\n"+ingreso.read())
lista_ingreso = ingreso.readlines()
for i in range (len(lista_ingreso)):
    lista_ingreso[i] = lista_ingreso[i][:-1]
#print (lista_ingreso)
for i in dic_municipios.keys():
    lista_in = []
    for c in range (len (lista_ingreso)):
        if int(lista_ingreso[c][0]) == i:
            pos_in = lista_ingreso[c].find(",")
            lista_in.append(lista_ingreso[c][pos_in+1:])
    #print ("\n\n",lista_in)
    for a in dic_municipios[i][1:]:
        #print (a)
        lista_ingre = []
        for d in range (len(lista_in)):
            pos_inicio = lista_in[d].find(",")
            if int(lista_in[d][:pos_inicio]) in a:
                pos_in = lista_in[d].find(",")
                lista_ingre.append(lista_in[d][pos_in+1:])
        #print ("\n\n",lista_ingre)
        dic_in = {}
        lis_val = []
        for e in range(len(lista_ingre)):
            pos_in = lista_ingre[e].find(",")
            val = lista_ingre[e][pos_in+1:]
            val = val[1:-1]
            #print ("\n",val)
            lis_valore = []
            for f in range (4):
                pos_val = val.find(",")
                #print (pos_val)
                lis_valore.append(float(val[:pos_val]))
                val = val[pos_val+1:]
                #print ("\n",lis_valore)
            lis_val.append(lis_valore)
        #print ("\n",lis_val)
        if len(lis_val) > 0:
            print (len(a))
        #for b in range(1,len(a)+1):
            #print (a[f])