import sys
input = sys.stdin.readline
output = sys.stdout.write
'''
백트래킹으로 해야할거같은디
아냐 DP
'''
def solution():
    s1 = input().rstrip()
    s2 = input().rstrip()

    dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[len(s1)][len(s2)]


if __name__ == "__main__":
    print(solution())