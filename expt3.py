# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 06:22:14 2021

@author: Shivani
"""
import numpy as np
import random as rn
a=np.random.rand(3,3)
print("\ngiven matrix:\n",a)
print("\ntranspose of matrix:\n",a.T)
a=np.random.rand(3,3)
b=np.random.rand(3,3)
print("array a")
print(a,"\n")
print("array b")
print("matrix operation :\n","\naddition:\n")
c=np.add(a,b)
print(c)
c=np.subtract(a,b)
print("\nsubtraction:\n\n",c)
c=np.dot(a,b)
print("\nmultiplication:\n\n",c,"\n")
