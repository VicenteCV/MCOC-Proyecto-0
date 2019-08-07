# -*- coding: utf-8 -*-
"""

Created on Tue Aug 06 23:12:45 2019


@author: Vicente
"""

import scipy as sp
import matplotlib.pylab as plt
import sys
import numpy

import random

lista=sp.zeros(10, dtype=sp.float64)
#Se crean numeros aleatorios y se insertan en listas creadas anteriormente
def Creacion_numeros(lista):
    x=0
    for i in lista:
        lista[x]=random.random()
        x+=1
    return lista
#Estos numeros se van multiplicando por 10 hasta llegar a que sean enteros
def Elevar_numeros(lista):    
    elevados=[]
    decimales=[]
    for i in lista:
        contador=0
        while (i).is_integer()== False :
            i=i*10
            contador+=1
        elevados.append(i)
        elevados.append(contador)
        contador=0
    return elevados
# Se suma el número con aquel que lo precede en la lista
def Sumas(lista):
    sumas=[]
    for i in range(9):
        a=lista[i]+lista[i+1]
        sumas.append(a)
    return sumas
# Se resta el número con aquel que lo precede en la lista
def Restas(lista):
    restas=[]
    for i in range(9):
        a=lista[i]-lista[i+1]
        restas.append(a)
    return restas
#Se comparan los resultados de las operaciones entre los numeros antes y despues de ser elevados
#Para esto, aquellos numeros que no estaban elevados se multiplican por 10 a la potencia que los anteriores fueron elevados

def Comparacion(a,b):
    decimales=[]
    if len(a)>10:
        print 'es'
        for i in range(20):
            if i%2==1:
                decimales.append(a[i])
        contador=0
        for i in a:
            if i<100:
                del a[contador]
            contador+=1
    nuevo=[]
    for j in range(9):
        c=b[j]*10**decimales[j]
        nuevo.append(c)
    comparacion=[]
    for k in range(9):
        d=nuevo[k]-a[k]/nuevo[k]
        comparacion.append(d)
    return comparacion

        
    
a=Creacion_numeros(lista)
b=Elevar_numeros(a)
c=Comparacion(b,a)
#Se produjeron los numeros, se elevaron en dos instancias y luego se compararon
print c

plt.plot(c, label='Comparacion')
plt.legend()
plt.axis('auto')
plt.grid(True)
plt.savefig('Lossofsignifcance.png')
plt.show()





#multiplicarlos y luego elevarlos
#elevarlos y luego multiplicarlos
#ver diferencia
=======
lista=[]
a1=random.random()
print a1
lista.append(a1)
a2=random.random()
print a2
lista.append(a2)
b=random.uniform(0,1,2)
for i in b:
    print i
    lista.append(i)
c1= numpy.random.uniform(0,1)
print c1
lista.append(c1)
c2= numpy.random.uniform(0,1)
print c2
lista.append(c2)
d=numpy.random.uniform(0,1,size=(2,1))
print d
for i in d:
    for j in i:
        print j
        h=len(str(j))-1
        print h
        lista.append(j)
print lista        
        

