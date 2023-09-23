from utils import *
import numpy as np

def add(a, b):
    if not areSameSize(a, b):
        raise Exception("The matrices are not the same size!")
    
    rows = len(a)
    cols = len(a[0]) if isinstance(a[0], list) else -1
    matrix = []

    if cols == -1: # vector
        matrix = [a[i] + b[i] for i in range(rows)]
    else: # matrix
        matrix = [[a[i][j] + b[i][j] for j in range(cols)] for i in range(rows)]

    return matrix

def subtract(a, b):
    if not areSameSize(a, b):
        raise Exception("The matrices are not the same size!")
    
    rows = len(a)
    cols = len(a[0]) if isinstance(a[0], list) else -1
    matrix = []

    if cols == -1: # vector
        matrix = [a[i] - b[i] for i in range(rows)]
    else: # matrix
        matrix = [[a[i][j] - b[i][j] for j in range(cols)] for i in range(rows)]

    return matrix

def transpose(a):
    if isVector(a):
        raise Exception("There's no difference in row and column vectors in python")

    rows = len(a)
    cols = len(a[0]) 

    return [[a[i][j] for i in range(cols)] for j in range(rows)]
    
def multiply(a, b):
    if len(a[0]) != len(b):
        raise Exception("Matrices dimensions are not compatible for multiplication")

    multiplication = []

    for i in range(len(a)): # row elements of a
        row = []
        for j in range(len(b[0])): # col elements of b
            sum = 0
            for k in range(len(a[0])): # matching dimension of a and b
                sum += a[i][k] * b[k][j]
            row.append(sum)
        multiplication.append(row)

    return multiplication

def tensorProduct(a, b):
    rows = len(a) * len(b) 
    cols = len(a[0]) * len(b[0])
    tensorProduct = np.zeros((rows, cols))

    for i in range(len(a)):
        for j in range(len(a[i])):
            e = a[i][j]
            if e == 0:
                continue

            for k in range(len(b)):
                for l in range(len(b[k])):
                    target = b[k][l]
                    tensorProduct[i*len(b)+k][j*len(b[0])+l] = e * target

    return tensorProduct