def fibon(n):
    a = 0
    b = 1
    for i in range(1, n):
        c = a
        a = b
        b = a + c
    return b

#def fibon(n):
 #   t = 5
