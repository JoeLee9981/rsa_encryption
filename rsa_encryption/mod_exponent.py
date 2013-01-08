'''
Created on Sep 12, 2012

@author: Joseph Lee
'''

#Algorithm from Discrete Math and 
#its Applications 7th Edition, 
#by Kenneth H. Rosen
def _base_b_convert(n, b):
    if b < 1 or n < 0:
        raise ValueError("Invalid Argument")
    
    q = n
    a = []
    while q != 0:
        value = int(q % b)
        a.append(value)
        q =int(q / b)
    return a

#Algorithm from Discrete Math and 
#its Applications 7th Edition, 
#by Kenneth H. Rosen
def mod_exp(base, n, mod):
    if base < 0 or n < 0 or mod < 0:
        raise ValueError("Invalid Argument")
    a = (_base_b_convert(n, 2))
    x = 1
    pow = base % mod
    for i in range(0, len(a)):
        if a[i] == 1:
            x = (x * pow) % mod
        pow = pow**2 % mod
    return x
        

    
        