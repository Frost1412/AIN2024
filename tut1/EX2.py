def recursiveFact(a : int):
    if a==0 or a==1:
        return 1
    return a * recursiveFact(a-1)
