import sys
input = sys.stdin.readline
output = sys.stdout.write
'''
n을 1,2로 채우는 문제
n-1에다가 1짜리를 붙이는 경우와 n-2에다 2짜리를 붙이는 경우를 합한다.
'''

def solution():
    n = int(input())
    dp = [0] *1001
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    answer=dp[n]
    return answer % 10007

if __name__ == "__main__":
    print(solution())