from collections import deque
import sys
input = sys.stdin.readline
output = sys.stdout.write

di = [1,0,-1,0]
dj = [0,1,0,-1]
def solution():
    n,m = map(int,input().split())   
    road = [list(map(int,input().split())) for _ in range(n)]
    visited = [[-1]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if road[i][j] == 2:
                start_pos = (i, j)
                visited[i][j] = 0
            if road[i][j] == 0:
                visited[i][j] = 0
                
    
    q = deque()
    q.append(start_pos)

    while q:
        start_i,start_j=q.popleft()
        for k in range(4):
            new_i = start_i + di[k]
            new_j = start_j + dj[k]
            if 0 <= new_i < n and 0 <= new_j < m and visited[new_i][new_j] <0 and road[new_i][new_j]:
                visited[new_i][new_j] = visited[start_i][start_j] + 1
                q.append((new_i,new_j))
    
    for row in visited:
        print(*row)
    print('\n')
            
if __name__ == "__main__":
    solution()