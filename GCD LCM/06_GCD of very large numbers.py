def gcd(number1,number2):
    while number2 != 0:
        number1 , number2 = number2, (number1 % number2)

    return number1

def very_large_num_gcd(number1, number2):

    result = gcd(number1,number2)

    print(result)

num1 = "12345678910111213141516"
num2 = "123456789101112131415160"


very_large_num_gcd(int(num1),int(num2))

# or

from math import gcd

num1 = "12345678910111213141516"
num2 = "123456789101112131415160"
print(gcd(int(num1),int(num2)))