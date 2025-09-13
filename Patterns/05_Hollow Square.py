def Hollow_Square(gridsize):

    for row in range(1,gridsize+1):
        if row == 1 or row == gridsize:
            print("* " * gridsize)

        else:
            print("* " + "  "*(gridsize-2) + "* ")




def Hollow_Square_v2(gridsize):

    for row in range(1,gridsize+1):
        line = []
        for column in range(1,gridsize+1):
            if row == 1 or column == 1 or row == gridsize or column == gridsize:
                line.append("* ")

            else:
                line.append("  ")


        print(" ".join(line))


def Hollow_Square_v3(gridsize):

    for row in range(1,gridsize+1):
        line = []
        for column in range(1,gridsize+1):
            hollow_square =  row == 1 or column == 1 or row == gridsize or column == gridsize
            digonal = row == column or column == (gridsize - row + 1)

            if hollow_square or digonal:
                line.append("* ")

            else:
                line.append("  ")


        print(" ".join(line))


if __name__ == "__main__":

    Hollow_Square(5)
    Hollow_Square_v2(5)
    Hollow_Square_v3(9)
