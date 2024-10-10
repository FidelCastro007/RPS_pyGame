def reverseRightAngledTriangle():
    for i in range(5):
        for j in range(i):
            print('_',end='')
        for k in range (5-i):
            print('*',end='')
        print()

reverseRightAngledTriangle()

print('')

def invertedEquiletralTriangle():
    for i in range(7,0,-2):
        for j in range((7-i) // 2):
            print("_",end="")
        for k in range(i):
            print("*",end="")
        for j in range((7-i) // 2):
            print("_",end="")
        print()
        
invertedEquiletralTriangle()

print('')

def equiletralTriangle():
    for i in range(0,7,2):
        for j in range((7-i) // 2):
            print("_",end="")
        for k in range(i+1):
            print("*",end="")
        for j in range((7-i) // 2):
            print("_",end="")
        print()
        
equiletralTriangle()

print('')

def RightAngledTriangle():
    for i in range(5,0,-1):
        for j in range(i-1):
            print('_',end='')
        for k in range (5,i-1,-1):
            print('*',end='')
        print()

RightAngledTriangle()