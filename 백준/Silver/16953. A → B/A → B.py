import sys
input = sys.stdin.readline
output = sys.stdout.write

'''
홀수라면 끝에 1을 붙이는 방법밖에 없음
dp?
아 b가 짝수라면 -> 2를 곱한거임
b가 홀수라면 -> 1을 붙인거임
이 두 경우밖에 없다.

시간복잡도
시간제한 2초고 n이 10^9 10억이면,
O(2n)까지 되는건가??
'''

def solution():
    a,b = map(int,input().split())
    
    cnt = 0
    while a<b:
        if b %2 ==0:
            b =b //2
        elif b%10 == 1:
            b = b //10
        else:
            return -1
        cnt +=1
    if a!=b:
        return -1

    return cnt + 1

if __name__ == "__main__":
    print(solution())