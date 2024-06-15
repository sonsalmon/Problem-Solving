import sys
input = sys.stdin.readline
output = sys.stdout.write
'''
배낭문제
무게당 가치를 기준으로 그리디인가 - 아닌듯
dp문제임. 
 다시 풀어볼것
'''
def solution():
    n,k = map(int,input().split())
    weight = [0] * (n+1)
    value = [0]* (n+1)

    for i in range(1,n+1):
        w,v = map(int,input().split())
        weight[i] = w
        value[i] = v
    dp = [[0] * (k+1) for _ in range(n+1)] # k무게의 빈 공간이 있을 때 최대 가치
    
    for i in range(1,n+1):
        for j in range(1,k+1):
            if weight[i]<=j:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight[i]] + value[i])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][k]


if __name__ == "__main__":
    print(solution())