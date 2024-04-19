import sys
input = sys.stdin.readline
output = sys.stdout.write

'''
스케줄링 문제
중요도가 같다면 빨리 끝나는 프로세스부터 하는 게 효율적이다.
'''
def solution():
    n = int(input())
    time = list(map(int,input().split()))
    time.sort()
    answer =0

    for i in range(len(time)):
        answer += time[i] * (n-i)
    
    return answer

if __name__ == "__main__":
    print(solution())