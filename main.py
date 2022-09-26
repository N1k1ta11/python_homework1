import math

def Task1():
    while(True):
        a=int(input())
        if(a==6 or a==7):
            print("Да")
            break
        elif(1<=a<=5):
            print("Нет")
            break


def Task2_1():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f=not(x or y or z) == (not x and not y and not z)
                print(x,y,z,f)

def Task2_2():
    x=int(input("X="))
    while(x==0):
       x=int(input("X="))

    y=int(input("Y="))
    while (y == 0):
        y = int(input("Y="))

    if(x>0 and y>0):
        print("Четверть =",1)

    elif(x<0 and y>0):
        print("Четверть =",2)

    elif(x<0 and y<0):
        print("Четверть =",3)

    elif(x>0 and y<0):
        print("Четверть =",4)

def Task3_1():
    quarter = int(input())
    while(not(1<=quarter<=4)):
        quarter = int(input())
    if(quarter == 1):
        print("{(0, +беcконечность, (0, +бесконечность))}")

    elif(quarter == 2):
        print("{(-бесконечность, 0),(0, +бесконечность)}")

    elif(quarter==3):
        print("{(-бесконечность, 0),(-бесконечность, 0)}")
    else:
        print("{(0, +бесконечность),(-бесконечность, 0)}")

def Task3_2():
    A=[]
    A.append(int(input("Ax =")))
    A.append(int(input("Ay =")))
    B=[]
    B.append(int(input("Bx =")))
    B.append(int(input("By =")))

    if(A[0]==B[0]):
        print(abs(A[1]-B[1]))
    elif(A[1]==B[1]):
        print((abs(A[0]-A[1])))
    else:
        lenght = math.sqrt((B[0]-A[0])**2 + (B[1]-A[1])**2)
        print(lenght)
