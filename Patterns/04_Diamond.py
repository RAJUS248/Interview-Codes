def diamond(gridsize):

    for i in range(1,gridsize+1):
        space = gridsize - i
        star = (i * 2) - 1
        print(" "* space + "*" * star)

    for i in range(gridsize-1, 0, -1):
        space = gridsize - i
        star = (i * 2) - 1
        print(" "* space + "*" * star)

diamond(3)