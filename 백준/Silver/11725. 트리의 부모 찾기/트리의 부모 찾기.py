import sys
input = sys.stdin.readline
output = sys.stdout.write


def solution():
    n = int(input())
    edges = {i:[] for i in range(1,n+1)}
    for i in range(n-1):
        x,y = map(int,input().split())
        edges[x].append(y)
        edges[y].append(x)
    
    visited = [False] *(n+1)
    parents = [0]*(n+1)
    parents[1] = 1
    stack = []
    stack.append(1)
    while stack:
        current = stack.pop()
        visited[current] = True
        for child in edges[current]:
            if not visited[child]:
                parents[child] = current 
                stack.append(child)

    for i in range(2,n+1):
        print(parents[i])


if __name__ == "__main__":
    solution()