def solution(keyinput, board):
    answer = [0,0]
    x = board[0]//2
    y = board[1]//2
    for key in keyinput:
        if key=='left' and answer[0]>-x:
            answer[0] -=1
        elif key=='right' and answer[0]<x:
            answer[0]+=1
        elif key=='up' and answer[1]<y:
            answer[1]+=1
        elif key=='down' and answer[1]>-y:
            answer[1]-=1
    return answer