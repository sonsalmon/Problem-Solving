import sys
input = sys.stdin.readline
output = sys.stdout.write
sys.setrecursionlimit(10**6)

def dfs(nodes,visited,current):
    for node in nodes[current]:
        if visited[node]:
            continue
        else:
            visited[node] = True
            visited = dfs(nodes,visited,node)
    return visited

def solution():
    n, m = map(int,input().split())
    visited = [False] * (n+1)
    nodes = [[] for _ in range(n+1)]
    answer =0

    for _ in range(m):
        u,v = map(int,input().split())
        nodes[u].append(v)
        nodes[v].append(u)

    

    for i in range(1,n+1):
        if not visited[i]:
            visited = dfs(nodes,visited,i)
            answer +=1

        
        
    
    return answer

if __name__ == "__main__":
    print(solution())
    