
def clean(floor):
    row = len(floor)
    col = len(floor[0])
    for i in range(0, row):
        if(i%2 == 0):
            for j in range(0, col):
                if(floor[i][j] == 1):
                    floor[i][j] = 0
                    print_floor(floor, i, j)
                else:
                   print('vaccum cleaner Position :',i,j)
                   print("No Action")
                   print("\n")
                    
        else:
            for j in range(col-1, -1, -1):
                if(floor[i][j] == 1):
                    floor[i][j] = 0
                    print_floor(floor, i, j)
                else:
                    print('vaccum cleaner Position :',i,j)
                    print("No Action")
                    print("\n")

def print_floor(floor, row, col):
    print("Action:SUCK")
    print('vaccum cleaner Position :',row,col)
    print("After cleaning the matrix looks like:")
    for c in floor:
        print(c)
    print("\n")

column_size = int(input("Enter size of column: "))
row_size = int(input("Enter size of row: "))
floor = []
for i in range(0, row_size):
    b = []
    for j in range(0, column_size):
        print("Input {0} {1} element of 2d array".format(i, j))
        temp = int(input())
        b.append(temp)
    floor.append(b)


clean(floor)
