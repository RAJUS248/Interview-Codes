# Pyramid Pattern
def Pyramid_Pattern(hieght):

    for row in range(1,hieght+1):
        space = hieght - row
        star = (row * 2) -1 
        print(" " * space + "*" * star)

Pyramid_Pattern(25)

def invert_Pyramid_Pattern(hieght):

    for row in range(hieght,0,-1):
        space = hieght - row
        star = (row * 2) -1 
        print(" " * space + "*" * star)

invert_Pyramid_Pattern(25)