import sys
input = sys.stdin.readline
output = sys.stdout.write

def dfs(result):
    global m
    if len(result) ==m:
        print(*result)
        return
    for i in range(1,n+1):
        if len(result) == 0 or i >= result[-1]:
            result.append(i)
            dfs(result)
            result.pop()


    
def solution():
    global n
    global m
    n,m = map(int,input().split())
    dfs([])
    
if __name__ == "__main__":
    solution()