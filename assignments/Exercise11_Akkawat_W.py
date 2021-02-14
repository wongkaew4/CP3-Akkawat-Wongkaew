PyramidHigh = int(input("Input high of Pyramid (number):"))
space = PyramidHigh
for i in range(PyramidHigh):
    space = space - 1
    print(" "*space,"*"*((i*2)+1))