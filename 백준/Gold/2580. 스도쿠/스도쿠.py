import sys
from collections import deque
input = sys.stdin.readline
output = sys.stdout.write

def promising(board,i,j,x):
    if x in board[i]:
        return False
    elif x in [row[j] for row in board]:
        return False
    
    start_row, start_col = 3*(i // 3), 3*(j // 3)
    for row in range(start_row, start_row + 3):
        for col in range(start_col, start_col + 3):
            if board[row][col] == x:
                return False
    return True



def backtrack(board, blank,idx):
    if idx ==len(blank):
        return True
    
    i,j = blank[idx]
    for x in range(1,10):
        if promising(board,i,j, x):
            board[i][j] = x
            if backtrack(board,blank,idx+1):
                return True
            board[i][j]=0
        
    return False




def solution():
    board=[]
    for _ in range(9):
        board.append(list(map(int,input().split())))
    empty=deque()
    for i in range(9):
        for j in range(9):
            if board[i][j] ==0:
                empty.append([i,j])
    
    backtrack(board,empty,0)
    
    for row in board:
        print(' '.join(map(str,row)))
        


if __name__ == "__main__":
    solution()