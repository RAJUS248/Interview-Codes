def Right_Angled_Triangle(gridsize):

    for index in range(1,gridsize+1):
        print("* " * index)

Right_Angled_Triangle(5)


# Inverted Right-Angled Triangle
def Inverted_Right_Angled_Triangle(gridsize):

    for index in range(gridsize,0,-1):
        print("* " * index)

Inverted_Right_Angled_Triangle(5)

# Right-Angled Triangle (Aligned Right)
def Aligned_Right(gridsize):

    for level in range(1,gridsize+1):
        space = gridsize - level
        print("  " * space + " *" * level)

Aligned_Right(4)

def Invert_Aligned_Right(gridsize):

    for level in range(gridsize,0,-1):
        space = gridsize - level
        print("  " * space + " *" * level)

Invert_Aligned_Right(4)



        
