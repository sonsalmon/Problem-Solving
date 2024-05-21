import sys
input = sys.stdin.readline
output = sys.stdout.write
'''
dp문제인듯
양 끝 스티커는 무조건 선택하게 되어있음 그 전 스티커에 의해서 영향을 안 받으니까.

'''

def solution():
    t = int(input())
    for _ in range(t):
        sticker=[]
        n = int(input())
        sticker.append(list(map(int,input().split())))
        sticker.append(list(map(int,input().split())))
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = sticker[0][0]
        dp[1][0] = sticker[1][0]
        if n==1:
            print(max(dp[0][0],dp[1][0]))
            continue
        
        dp[0][1] = dp[1][0] + sticker[0][1]
        dp[1][1] = dp[0][0] + sticker[1][1]
        if n == 2:
            print(max(dp[0][1],dp[1][1]))
            continue
        
        for i in range(2,n):
            dp[0][i]= max(dp[1][i-1],dp[1][i-2]) + sticker[0][i]
            dp[1][i]= max(dp[0][i-1],dp[0][i-2]) + sticker[1][i]
        
        print(max(dp[0][-1],dp[1][-1]))
    return

if __name__ == "__main__":
    solution()