import sys
input = sys.stdin.readline
output = sys.stdout.write
'''
백트래킹?
dfs로 전체 확인?
dp
'''
        
def solution():
    n = int(input())
    triangle=  []
    for i in range(n):
        triangle.append(list(map(int,input().split())))
    dp = [[0]*i for i in range(1,n+1)]
    dp[0][0] = triangle[0][0]
    for i in range(1,n):
        for j in range(i+1):
            if j ==0:
                dp[i][j]= dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + triangle[i][j]
    print(max(dp[-1]))
    
        
    
if __name__ == "__main__":
    solution()