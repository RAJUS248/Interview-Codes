def Mirrored_Right_Triangle(size):
    for i in range(1, size+1):
        space = size - i
        print(" "* space + "*"* i)

Mirrored_Right_Triangle(5)

def Mirrored_Mirrored_Right_Triangle(size):
    for i in range(size,0,-1):
        space = size - i
        print(" "* space + "*" * i)

Mirrored_Mirrored_Right_Triangle(5)