def Pyramid_with_Numbers(size):

    for i in range(size):
        space = size - i
        
        print("  "* space +  str(11**i) * i )

Pyramid_with_Numbers(5)