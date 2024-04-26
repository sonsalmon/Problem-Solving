import sys
input = sys.stdin.readline
output = sys.stdout.write

'''
n=5 이후부터는 계속 변의 크기가 증가한다.
새로운 삼각형이 붙으면서 계속 120도각도가 만들어진다.

'''
def solution():
    t = int(input())
    dp = [0] *101
    dp[1]=dp[2]=dp[3] = 1
    dp[4]=dp[5]=2
    have_answer=5
    for _ in range(t):
        n = int(input())
        if n<have_answer:
            print(dp[n])
        else:
            for i in range(have_answer+1, n+1):
                dp[i] = dp[i-1] + dp[i-5] # 60도니까 6번째 삼각형이 한바퀴를 돌게 된다.
            print(dp[n])
            have_answer=n

    

if __name__ == "__main__":
    solution()