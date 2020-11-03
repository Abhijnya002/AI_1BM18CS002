
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

# Test 1
floor = [[1, 0, 0, 0],
         [0, 1, 0, 1],
         [1, 0, 1, 1]]

clean(floor)
