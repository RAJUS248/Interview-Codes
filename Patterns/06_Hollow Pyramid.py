def Hollow_Pyramid_v2(size):
    for i in range(1, size+1):
        space = size - i
        star = 2*i -1

        if i == 1 or i == size:
            print(" "* space + "*" * star)

        else:
            print(" "* space + "*" + " "*(2*i-3) + "*")

Hollow_Pyramid_v2(5)