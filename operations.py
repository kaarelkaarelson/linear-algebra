from utils import *

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

