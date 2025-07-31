"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
<<<<<<< HEAD
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else: 
        return b / a
    
def log(a, b):
    if b == 1 or b <= 0 or a <= 0:
        raise ValueError
    else:
        return math.log(b, a)
    
def exp(a, b):
=======
def add(a, b): 
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError
    return b/a

def log(a,b):
    if b <= 0:
        raise ValueError
    if a <= 0 or a == 1:
        raise ValueError
    return math.log(b,a)

def exp(a,b):
>>>>>>> 9dd63b6e40ede2aed611ed1514b9ac235418e119
    return a ** b

