import sys
input = sys.stdin.readline
output = sys.stdout.write

def solution():
    n = int(input())
    dp = [0] * 1001
    dp[1] = 1
    dp[2] = 3
    for i in range(3,n+1):
        dp[i] = dp[i-1] + 2*dp[i-2]

    
    answer = dp[n] %10007
    return answer

if __name__ == "__main__":
    print(solution())