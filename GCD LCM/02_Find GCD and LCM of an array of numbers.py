import math
def gcd_lcm_array(arr):
    print(math.gcd(*arr))
    print(math.lcm(*arr))

arr = [2, 7, 3]
gcd_lcm_array(arr)

# or  manual_version()

def gcd(a,b):

    while b != 0:
        a,b = b, (a % b) 

    return a

def lcm(a,b):
    return (a * b)//gcd(a,b)

def find_gcd_lcm_array(arr):

    result = arr[0]
    result2 = arr[0]

    for num in arr[1:]:
        result = gcd(result,num)
        result2 = lcm(result2,num)
        
    print("GCD =", result, "LCM =", result2)
arr = [2, 7, 3]
find_gcd_lcm_array(arr)