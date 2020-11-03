def clean(floor):  
    c=0
    i=0
    j=0
    row=len(floor)
    column=len(floor[0])
    while i < row:
        if (i % 2 == 0):          # If current row is even, traverse from  left to right 
            while j < column: 
                if floor[i][j] == 1:
                    floor[i][j]=0
                    c=c+1                 #increment the count
                    print_floor(floor,i,j,c)
                j=j+1
                       
        # If current row is even,traverse from right to left        
        else:
            j = column -1
            while j > 0:
                 if floor[i][j] == 1:     #If floor is dirt(1) clean(0) it
                    floor[i][j]=0
                    c=c+1                 #increment the count
                    print_floor(floor,i,j,c)
                 j=j-1
        i=i+1
        

def print_floor(floor, row, col,count):
    print('step:',count)
    print("Action:SUCK")
    print('vaccum cleaner Position :',row,col)
    print("After cleaning the matrix looks like:")
    for c in floor:
        print(c)
    
    print("\n")
    
   # Test 2
floor = [[1, 1, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 1, 1, 1, 1, 1, 1],
         [0, 1, 0, 1, 0, 1, 0]]
clean(floor)
