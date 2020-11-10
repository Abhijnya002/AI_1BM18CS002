import numpy as np 
import random 
from time import sleep 
  

def create_board(): 
    
    return(np.array([[0, 0, 0], 
                     [0, 0, 0], 
                     [0, 0, 0]])) 
  

def check_empty(board): 
    l = [] 
      
    for i in range(len(board)): 
        for j in range(len(board)): 
              
            if board[i][j] == 0: 
                l.append((i, j)) 
    return(l) 
  
 
def random_move(board, player): 
    select = check_empty(board) 
    curr = random.choice(select) 
    board[curr] = player 
    return(board) 
  
#check if any computer has three of their symbol in a row 
def wining1(board, player): 
    for x in range(len(board)): 
        win = True
          
        for y in range(len(board)): 
            if board[x, y] != player: 
                win = False
                continue
                  
        if win == True: 
            return(win) 
    return(win) 

#check if any computer has three of their symbol in a column
def wining2(board, player): 
    for x in range(len(board)): 
        win = True
          
        for y in range(len(board)): 
            if board[y][x] != player: 
                win = False
                continue
                  
        if win == True: 
            return(win) 
    return(win) 
  
#check if any computer has three of their symbol in a diagonal
def wining3(board, player): 
    win = True
    y = 0
    for x in range(len(board)): 
        if board[x, x] != player: 
            win = False
    if win: 
        return win 
    win = True
    if win: 
        for x in range(len(board)): 
            y = len(board) - 1 - x 
            if board[x, y] != player: 
                win = False
    return win 
  
 
def decision(board): 
    winner = 0
      
    for player in [1,2]: 
        if (wining1(board, player) or wining2(board,player) or wining3(board,player)): 
                 
            winner = player 
              
    if np.all(board != 0) and winner == 0: 
        winner = -1
    return winner 
  

def start_game(): 
    board, winner, counter = create_board(), 0, 1
    print(board) 
    sleep(2) 
      
    while winner == 0: 
        for player in [1,2]: 
            board = random_move(board, player) 
            print('-------------------------------')
            print( "Step:" + str(counter)  )
            print("Board after Computer " , player , " moves")
            print(board) 
            sleep(2) 
            counter += 1
            winner = decision(board) 
            if winner != 0: 
                break
    return(winner) 

#computer -1 means tie
print("Let the game starts between Computer1 Vs Computer2")
print('*********************************')
print("\n !!! The Winner is : COMPUTER " + str(start_game()) + "  !!!")