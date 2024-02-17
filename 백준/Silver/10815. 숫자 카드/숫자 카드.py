import sys
input = sys.stdin.readline
output = sys.stdout.write

def solution():
    # write code down
    n = int(input())
    cards = set(map(int, input().split()))
    m = int(input())
    numbers = list(map(int,input().split()))
    
    result = [0]*m
    
    for i in range(m):
        if numbers[i] in cards:
            result[i]= 1


    
    return result

if __name__ == "__main__":
    

    print(*solution())