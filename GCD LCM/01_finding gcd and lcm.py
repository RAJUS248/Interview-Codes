def gcd(a,b):
    while b != 0:

        a,b = b,a%b

    
    return a
    
print(gcd(12,18))


import math
print(math.gcd(12,18)) 


def lcm(a,b):
    return (a * b) // gcd(a,b)
print(lcm(12,18))


import math
print(math.lcm(12,18))
