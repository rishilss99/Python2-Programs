"""I Just go crazy sometimes"""
import math
def power(a,b):
    """Raise it to any power"""
    r = a**b
    print ("%d raised to %d is %d") % (a,b,r)
def square_root(n):
    """Square root any number"""
    s = math.sqrt(n)
    return s
def add(a):
    a = square_root(a) + 5
    print("So the sum is %d") % (a)
def maximum(*b):
    print type(abs(max(b)))



maximum(-1,-2,-3)

