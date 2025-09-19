def gcd(a,b):
    while b != 0:
        a,b = b,(a % b)

    return a

def simple_fraction(a,b):
    GCD = gcd(a,b)

    print(f"Simplified fraction: {(a//GCD)}/{(b//GCD)} " )


simple_fraction(18,24)