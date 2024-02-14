#1차원 배열 인덱스 조작으로 풀어보려다 실패함.

def solution(n):
    answer = []
    snail = [[0] *i for i in range(1,n+1)]
    x=y=angle=0
    cnt=1
    num = n*(n+1)//2
    dx = [0,1,-1]
    dy = [1,0,-1]
    
    while cnt<=num:
        snail[y][x] = cnt
        nx = x + dx[angle]
        ny = y + dy[angle]
        cnt = cnt+1
        if 0<=ny<n and 0<=nx<=ny and snail[ny][nx]==0:
            x = nx
            y = ny
        else:
            angle = (angle+1)%3
            x = x+dx[angle]
            y = y+dy[angle]
        
    return [i for j in snail for i in j]