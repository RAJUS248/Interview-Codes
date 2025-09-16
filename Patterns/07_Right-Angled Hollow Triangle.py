def Right_Angled_Hollow_Triangle(size):

    for i in range(1,size+1):
        if i == 1 or i == size:
            print("*" * i)

        else:
            print("*" + " "*(i-2) + "*")

Right_Angled_Hollow_Triangle(5)

def Inverted_Right_Angled_Hollow_Triangle(size):
    for i in range(size,0,-1):
        if i == 1 or i == size:
            print("*" * i)

        else:
            print("*" + " "*(i-2) + "*" )

Inverted_Right_Angled_Hollow_Triangle(5)