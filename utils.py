def areSameSize(a, b):
    if len(a) == len(b):
        if isinstance(a[0], list) and isinstance(b[0], list): # matrix
            return len(a[0]) == len(b[0]) 
        elif type(a[0]) == type(b[0]): # vector 
            return True 
    return False
