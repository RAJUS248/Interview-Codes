# manual way
def gcd(a,b):
    while b != 0:
        a,b = b,(a%b)
    
    return a

def lcm(a,b):
    return (a*b)//gcd(a,b)


def bell_ring(a,b):

    print(f"the bells of {a,b} is rings at {lcm(a,b)} miniutes")

bell_ring(12,18)

# or

from math import gcd
def bell_ring_v2(a,b):

    LCM = (a * b) // gcd(a,b)

    print(f"the bells of {a,b} is rings at {LCM} miniutes")

bell_ring_v2(12,18)


