import sys
input = sys.stdin.readline
output = sys.stdout.write
'''
비슷한 문제 푼적있는데,,
dp? 백트래킹? 
'''
def solution():
    n,k = map(int,input().split())
    
    if n>=k:
        return n-k
    dp = [10**6] *(2*k + 1)
    dp[n]= 0
    for i in range(n):
        dp[i]= n-i # n보다 작을 때는 한칸씩 가야함
    dp[n+1] = 1

    
    for j in range(n+2,2*k):
        if j%2==0:
            dp[j] = min(dp[j-1],dp[j//2]) + 1
        else:
            dp[j] = min(dp[j-1], dp[(j+1)//2] +1) + 1
        
        
    
    return dp[k]

if __name__ == "__main__":
    print(solution())