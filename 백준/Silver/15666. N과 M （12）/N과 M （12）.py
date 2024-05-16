import sys
input = sys.stdin.readline
output = sys.stdout.write
sys.setrecursionlimit(100000)

def solution():
    n,m = map(int,input().split())
    num_list=  list(map(int,input().split()))
    num_list.sort()
    print_set = set()
    def dfs(result):
        if len(result) == m:
            if str(result) not in print_set:
                print(*result)
                print_set.add(str(result))
            return
        for i in range(n):
            if len(result) ==0 or num_list[i]>= result[-1]:
                result.append(num_list[i])
                dfs(result)
                result.pop()
    dfs([])

    

if __name__ == "__main__":
    solution()