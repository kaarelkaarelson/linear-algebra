def areSameSize(a, b):
    if len(a) == len(b):
        if isinstance(a[0], list) and isinstance(b[0], list): # matrix
            return len(a[0]) == len(b[0]) 
        elif isVector(a) and isVector(b): # vector 
            return True 
    return False

def isVector(a):
    return isinstance(a, list) and type(a[0]) != list
