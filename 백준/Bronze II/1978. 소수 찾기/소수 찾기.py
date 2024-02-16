import sys
input = sys.stdin.readline
output = sys.stdout.write

def function():
    # write code down
    n = int(input())
    numbers = list(map(int, input().split()))
    not_sosu = 0
    
    for i in range(n):
        for j in range(2,(numbers[i]//2) +1):
            if (numbers[i] % j) == 0:
                not_sosu += 1
                break
        if numbers[i] ==1:
            not_sosu +=1
            continue


        

    
    return n-not_sosu

if __name__ == "__main__":
    print(function())