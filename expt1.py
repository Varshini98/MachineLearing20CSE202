import numpy as np
import random as rn
print("Normal matrix:-\n")
a=np.array([-1,-2,1,2])
a=a.reshape(2,2)
print(a,"\n")
c=np.absolute(a)
print("Absolute matrix:\n")
print(c,"\n")
c=np.negative(c)
print("Negative matrix:\n")
print(c,"\n")
print("First array:-\n")
x=np.arange(9).reshape(3,3)
print(x,"\n\nsecond array:-\n")
y=np.arange(3).reshape(3,1)
print(y,"\n")

print("\nAdding a column to the first array\n")
print(np.append(x,y,axis=1))
print("\nAdding a row to the first array\n")
print(np.insert(x,[2],y,axis=1))

arr=np.arange(12).reshape(3,4)
print("\nArray : \n",arr)
print("Shape:",arr.shape)

a=np.delete(arr,1,0)
print("\nDeleting array 2 times:\n",a)
print("Shape:",a.shape)

a=np.delete(arr,1,1)
print("\nDeleting arr 2 times:-\n",a)
print("Shape:",a.shape)

print("\nMinimum value of the matrix\n",a.min())
print("\nMaximum value of the matrix\n",a.max())
print("\nSum  of the matrix\n",a.sum())
