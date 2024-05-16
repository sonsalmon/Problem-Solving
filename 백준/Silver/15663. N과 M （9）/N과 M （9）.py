import sys
input = sys.stdin.readline
output = sys.stdout.write

def solution():
    n,m = map(int,input().split())
    num_list = list(map(int,input().split()))
    num_list.sort()

    stack = []
    stack.append(num_list[0])
    result = []
    visited = [False] * (n)

    # while stack:

    #     if len(result) == m:
    #         print(*result)
        
    #     for i in range(n):
    #         if not visited[i]:
    #             visited[i] = True
    result_set = set()
    def dfs(result):
        if len(result)==m and str(result) not in result_set:
            result_set.add(str(result))
            print(*result)
            return
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                result.append(num_list[i])
                dfs(result)
                visited[i] = False
                result.pop()
    dfs([])


if __name__ == "__main__":
    solution()