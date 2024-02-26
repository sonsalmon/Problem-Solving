
'''
왜 틀렸는지 모르겠음
-> ㄹ모양으로 연결되는 경우, 2번 체크함. 내 코드는 위, 왼쪽만 확인하는데,
위에서 부터 연결된 배추가 (i,j)의 바로 위, 왼쪽이 아니라 한칸 띄고 ㄹ모양 또는 N모양으로 연결될 수도 있음.

def count(land):
    worm = 0
    for i in range(len(land)):
        for j in range(len(land[0])):
            # print('land[{}][{}] : {}'.format(i,j,land[i][j]))
            if land[i][j] == 0:

                continue
            else:
                if i >0 and land[i-1][j] == 1:
                    continue
                elif j >0 and land[i][j-1] == 1:
                    continue
                else:
                    #i또는 j가 0이거나, 이전에 센 적 없는 1이면
                    worm +=1
    
    return worm

'''

import sys
input = sys.stdin.readline
output = sys.stdout.write

sys.setrecursionlimit(10000)
def solution():
    def dfs(x,y):
        dx = [-1,1,0,0]            
        dy = [0,0,-1,1]
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<= nx < m) and (0<= ny < n):
                if land[ny][nx] ==1:
                    land[ny][nx] =0
                    dfs(nx,ny)
    T = int(input())
    for _ in range(T):
        m, n, k = map(int,input().split())
        land = [ [0]*m for _ in range(n) ]
        cnt = 0
        for _ in range(k):
            x, y = map(int,input().split())
            land[y][x]= 1
        
        # for i in land:
        #     for j in i:
        #         print(j, end=" ")
        #     print()

        
        for x in range(m):
            for y in range(n):
                if land[y][x] ==1:
                    dfs(x,y)
                    cnt +=1
        print(cnt)
    


if __name__ == "__main__":
    solution()