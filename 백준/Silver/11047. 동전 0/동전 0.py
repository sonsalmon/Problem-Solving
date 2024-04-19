import sys
input = sys.stdin.readline
output = sys.stdout.write

'''
그리디로 할 수 있나

'''
def solution():
    n,k =map(int,input().split())
    coin=[]
    answer=0
    for _ in range(n):
        coin.append(int(input()))
    coin.reverse()

    for money in coin:
        answer += k // money
        k = k % money
        
    return answer

if __name__ == "__main__":
    print(solution())