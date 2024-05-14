import sys
input = sys.stdin.readline
output = sys.stdout.write

def solution():
    n,m = map(int,input().split())
    num_list = list(map(int,input().split()))
    num_list.sort()
    
    def dfs(result: list):
        if len(result) == m:
            print(*result)
            return
        for i in range(n):
            if len(result) ==0 or num_list[i] >= result[-1]:
                result.append(num_list[i])
                dfs(result)
                result.pop()
    dfs([])

if __name__ == "__main__":
    solution()