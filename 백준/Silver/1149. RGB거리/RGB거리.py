import sys
input = sys.stdin.readline
output = sys.stdout.write
from collections import deque
'''
이웃집과 색다르게 칠하기
bfs로 완전탐색?
시간초과..
이전 선택이 이후에 영향주니까 그리디는 안 됨
분할정복? 아닌듯
백트래킹?
'''

# bfs 시간초과
def solution1():
    n = int(input())
    price = [list(map(int,input().split())) for _ in range(n)]
    q= deque()
    ans = [float('inf')] * 3
    for i in range(3):
        q.append((0,i,0))
        while q:
            house,idx,total = q.popleft()
            if house == n:
                ans[i] = min(ans[i],total)
            else:
                if idx !=0:
                    q.append((house+1,0, total + price[house][idx]))
                if idx !=1:
                    q.append((house+1,1, total + price[house][idx]))
                if idx !=2:
                    q.append((house+1,2, total + price[house][idx]))
    return min(ans)

#dp??
def solution2():
    global price,n
    n = int(input())
    price = [list(map(int,input().split())) for _ in range(n)]
    dp = [[0]*3 for _ in range(n)]
    dp[0] = price [0]
    for i in range(1,n):
        dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + price[i][0]
        dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + price[i][1]
        dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + price[i][2]
    return min(dp[-1])
    
    

if __name__ == "__main__":
    # print(solution1())
    print(solution2())