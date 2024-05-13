import sys
input = sys.stdin.readline
output = sys.stdout.write

'''
아 혹시 dfs?
'''
def backTracking(result,n,m,visited):
    if len(result) == m:
        print(*result)
        return
    for i in range(1,n+1):
        if (visited[i] == False) and (len(result)==0 or i > result[-1]):
            visited[i] = True
            result.append(i)
            backTracking(result,n,m,visited)
            visited[i] = False
            result.pop()
def solution():
    n,m = map(int, input().split())
    
    visited = [False] * (n+1)
    backTracking([],n,m,visited)


if __name__ == "__main__":
    solution()