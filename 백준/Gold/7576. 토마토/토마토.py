from collections import deque
import sys
input = sys.stdin.readline
output = sys.stdout.write
'''
bfs같긴한데, 하루가 지나면 모돈 익은 토마토 주변이 전부 익게 됨.
그냥 bfs로 하면 날짜를 셀 수가 없음.

'''
dm = [1,0,-1,0]
dn = [0,1,0,-1]
def solution():
    m,n = map(int,input().split())
    tomato = [list(map(int,input().split())) for _ in range(n)]
    q = deque()
    cnt_day = -1
    today_tomato = 0
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:
                q.append((i,j))
                today_tomato +=1 #오늘 익은 토마토 몇개있는지
    tomorow_tomato = 0
    while q:
        for _ in range(today_tomato): #오늘 익어있는 토마토 만큼 반복
            start_i,start_j = q.popleft()
            for k in range(4):
                next_i = start_i + dn[k]
                next_j = start_j + dm[k]
                if 0 <= next_i < n and 0 <= next_j < m and tomato[next_i][next_j] == 0:
                    tomato[next_i][next_j] = 1
                    q.append((next_i,next_j))
                    tomorow_tomato +=1 
        cnt_day+=1
        today_tomato = tomorow_tomato
        tomorow_tomato = 0 # 내일은 새로 익은 토마토 주변만 보면 됨. 오늘 익어 있던 것들은 이미 다 영향 줬음.

    #다 돌았는데 안 익은 토마토가 있다면 경로가 없는 것
    for row in tomato:
        if 0 in row:
            return -1
    
    return cnt_day

if __name__ == "__main__":
    print(solution())