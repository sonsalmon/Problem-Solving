import sys
input = sys.stdin.readline
output = sys.stdout.write
'''
제곱수는 같은 수를 반복해서 곱하니까 끝자리가 반복된다.
처음 반복이 나타나는 수를 찾는다. 
그 반복의 b%c번째 수
'''

# 시간 초과
def solution():
    a,b,c = map(int,input().split())
    x = a
    cnt=1
    #a가 c보다 작다면 먼저곱함
    while x<c and cnt <b:
        x = x*a
        cnt+=1
    if cnt == b:
        return x%c
        
    repeat = [x%c]

    while repeat[0]%c != (repeat[-1]*a) %c:
        repeat.append((repeat[-1]*a)%c)
    
    return repeat[((b-cnt)%len(repeat))]


def solution2():
    a,b,c = map(int,input().split())
    return pow(a,b,c)
    

if __name__ == "__main__":
    print(solution2())