#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#La lemniscate de Bernouilli
t=np.linspace(0, 2*np.pi, 100)
x=np.sin(t)/(1+np.cos(t)**2)
y=(np.sin(t)*np.cos(t))/(1+np.cos(t)**2)

plt.plot(x, y, 'g')
plt.title('La lemniscate de Bernouilli')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#La spirale d''archimèd
t1=np.linspace(0, 10*np.pi, 100)
x1=t1*np.cos(t1)
y1=t1*np.sin(t1)

plt.plot(x1, y1, 'b')
plt.title('La spirale d''archimède')
plt.xlabel('x1')
plt.ylabel('y1')
plt.show()

#La courbe du coeur
t2=np.linspace(0, 2*np.pi, 100)
x2=16*np.sin(t2)**3
y2=13*np.cos(t2)-5*np.cos(2*t2)-2*np.cos(3*t2)-np.cos(4*t2)

plt.plot(x2, y2, 'r')
plt.title('La courbe du coeur')
plt.xlabel('x2')
plt.ylabel('y2')
plt.show()
#Les cyclos harmoniques
#p, q=8,3
#t3=np.linspace(0, 2*q*np.pi, 100)
#x3=(1+np.cos((p/q)*t3))*np.cos(t3)
#y3=(1+np.cos((p/q)*t3))*np.sin(t3)
#
#plt.plot(x3, y3)
#plt.title('Les cyclos harmoniques')
#plt.xlabel('x3')
#plt.ylabel('y3')
#
#plt.show()

for p in range(1,10):
    for q in range(1,10):
        t3=np.linspace(0, 2*q*np.pi, 100)
        x3=(1+np.cos((p/q)*t3))*np.cos(t3)
        y3=(1+np.cos((p/q)*t3))*np.sin(t3)
        
        plt.plot(x3, y3)
        plt.title('Les cyclos harmoniques pour p ={} et q={}'.format(p,q))
        plt.xlabel('x3')
        plt.ylabel('y3')
        plt.show()

