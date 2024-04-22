import sys
input = sys.stdin.readline
output = sys.stdout.write

def solution():
    n,m = map(int, input().split())
    password={}
    for _ in range(n):
        a,b = input().split()
        password[a]=b
    
    for _ in range(m):
        query = input().strip()
        print(password[query])

if __name__ == "__main__":
    solution()