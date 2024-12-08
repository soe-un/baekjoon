while (True):
    x, y, z = map(int, input().split(' '))
    if (x == 0 and y == 0 and x == 0):
        break
    
    lineList = sorted([x,y,z])
    if(lineList[2] >= lineList[0] + lineList[1]) :
        print('Invalid')
    elif (x == y) and (y == z):
        print('Equilateral')
    elif (x == y) or (x == z) or (y == z):
        print('Isosceles')
    elif (x != y) and (y != z):
        print('Scalene')


