import sys
input = sys.stdin.readline
output = sys.stdout.write

'''
가장 긴지는 수열을 만들어봐야 알 수 있다.
백트래킹으로??
아님 그리드??
백트래킹ㄱ시간초과
DP로 풀어야함
'''
'''
시간초과났음
def backTacking(result,num_list, start, last, max_len):
    for i in range(start,last):
        if len(result) == 0 or num_list[i]>result[-1]:
            result.append(num_list[i])
            max_len= max(max_len,backTacking(result,num_list,i+1,last, max(max_len,len(result)))) 
            result.pop()
    
    return max_len

'''

def solution():
    n = int(input())
    num_list = list(map(int,input().split()))
    
    dp = [1] * n #가장 짧은 부분수열의 길이 1. 첫번째 원소로 끝나는 부분수열의 길이는 1
    for i in range(1,n):
        for j in range(i):
            if num_list[j] < num_list[i]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)



if __name__ == "__main__":
    print(solution())