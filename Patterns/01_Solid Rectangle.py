def Solid_Rectangle(gridsize):

    for _ in range(gridsize):
        print("* " * gridsize)

    for _ in range(gridsize):
        print("* " * (gridsize+1))

Solid_Rectangle(4)