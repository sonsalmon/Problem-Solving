import sys
input = sys.stdin.readline
output = sys.stdout.write

def solution():
    n,m = map(int,input().split())
    num_list = list(map(int,input().split()))
    num_list.sort()
    visited = [False] * n

    def dfs(result):
        if len(result) == m:
            print(*result)
            return
        for i in range(n):
            if not visited[i]:
                visited[i] =True
                result.append(num_list[i])
                dfs(result)
                result.pop()
                visited[i] = False
    dfs([])
            
if __name__ == "__main__":
    solution()