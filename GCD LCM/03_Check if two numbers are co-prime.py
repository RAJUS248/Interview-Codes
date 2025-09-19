# manual way

def co_prime_gcd(a,b):
    while b != 0:
        a,b = b , (a % b)
    
    if a == 1:
        print("co_prime")

    else:
        print("not co_prime")

co_prime_gcd(8,9)

# or

from math import gcd

def co_prime_gcd_v2(a,b):
    if gcd(a,b) == 1:
        print("co_prime")

    else:
        print("not co_prime")

co_prime_gcd_v2(8,9)

