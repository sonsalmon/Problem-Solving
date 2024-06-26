# 1과 2를 이용해 n을 만드는 가짓수를 구하면 된다.
# n이 1 증가할 때마다 두가지의 경우의 수가 있음.
# 맨 마지막 타일을 가로로 배치하는 경우와 맨 마지막 타일을 세로로 배치하는 경우
# 가로로 배치하는 경우 바닥이 N-2인 방법의 수가 필요.
# 세로로 배치하는 경우 바닥이 n-1인 방법의 수가 필요/
def solution(n):
    answer = 0
    dp = [0]*(n+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]= (dp[i-1]+dp[i-2])%1000000007
    
    
    return dp[n]