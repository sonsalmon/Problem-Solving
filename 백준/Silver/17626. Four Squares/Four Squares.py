import math
import sys
input = sys.stdin.readline
output = sys.stdout.write

'''
n의 제곱근보다 작은 가장 큰 자연수를 구한다. 이것을 x라 하면
n-x^2로 반복한다.이 때 구해지지 않는다면(x-1)^2로 해본다.
-그게 최소 개수라는 보장이 없음.



'''
# 브루트 포스
# 4가지 경우중 하나임.
def solution():
    n = int(input())
    #n이 제곱수일 때
    if math.sqrt(n) == int(math.sqrt(n)):
        return 1
    for i in range(1,int(math.sqrt(n))+1):
        # n - i**2 가 제곱수일 때
        if math.sqrt(n-i**2) == int(math.sqrt(n-i**2)):
           return 2
    for i in range(1,int(math.sqrt(n))+1):
        for j in range(1,int(math.sqrt(n-i**2))+1):
            if math.sqrt(n-i**2 - j**2) == int(math.sqrt(n-i**2-j**2)):
                return 3
    # 남은 경우는 4
    return 4

# DP
def solution2():
    n = int(input())
    dp =[0,1]
    for i in range(2,n+1):
        min_value = 1e9
        for j in range(1,int(math.sqrt(i))+1):
            min_value = min(min_value, dp[i-j**2])
                            
        dp.append(int(min_value+1))
    return dp[n]

if __name__ == "__main__":
    print(solution2())