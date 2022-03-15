import random
import numpy as np
import time

row=int(input("Rows: "))
col=int(input("Columns: "))


def Matrix(row,col):
    matrix=[]
    for i in range(row):
        matrix.append([])
        for j in range(col):
             matrix[i].append(random.randint(1, 100))                
    return matrix


X = Matrix(row,col)
Y = Matrix(row,col)


Xnp = np.array(X)
Ynp = np.array(Y)

startTime = time.time()
#Multiplication
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
MultTime=time.time() - startTime
print("Matrix Multiplication Time: {:.9f} sec" .format(MultTime))

startNP = time.time()
#Multiplication by numpy
MultNumpy= np.dot(Xnp,Ynp)
NumPyTime=time.time() - startNP
print("Matrix Multiplication by NumPy Time: {:.9f} sec" .format(NumPyTime))




