import sys
input = sys.stdin.readline
output = sys.stdout.write

'''
n을 나타내는 것은, 
n-1을 만드는 방법의 수 뒤에 1을 붙이는 방법
n-2를 만드는 방법의 수 뒤에 2를 붙이는 방법
n-3을 만드는 방법의 수 뒤에 3을 붙이는 방법이다.

'''
def solution():
    t = int(input())
    dp = [0]*11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for _ in range(t):
        n = int(input())
        if dp[n]>0:
            print(dp[n])
        else:
            for j in range(4,n+1):
                if dp[j]>0:
                    continue
                dp[j]= dp[j-1]+dp[j-2]+dp[j-3]
            print(dp[n])

if __name__ == "__main__":
    solution()