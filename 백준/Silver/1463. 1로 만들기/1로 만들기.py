import sys
input = sys.stdin.readline
output = sys.stdout.write

'''
DP문제임.
n일때의 최소 연산은 n//2일 횟수, n-1일 때 횟수중 작은 것 +1임.
'''
def solution():
    
    n = int(input())
    if n == 1:
        return 0
    elif n ==2:
        return 1
    elif n ==3:
        return 1
    answer =[0]*(n+1)
    answer[1]=0
    answer[2]=1
    answer[3]=1
    for i in range(4,n+1):
        if i % 3 ==0 and i %2 ==0:
            answer[i]= min(answer[i//2],answer[i//3]) +1
        elif i%3==0:
            answer[i] = min(answer[i//3], answer[i-1]) + 1
        elif i%2==0 and (i-1)%3==0:
            answer[i] = min(answer[i//2], answer[i-1]) + 1
        elif i%2==0 and (i-2)%3 == 0:
            answer[i] = min(answer[i//2], answer[i-2] + 1) + 1
        else:
            answer[i] = answer[i-1] + 1
    return answer[n]


if __name__ == "__main__":
    print(solution())