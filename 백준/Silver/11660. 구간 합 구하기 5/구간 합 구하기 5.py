import sys
input = sys.stdin.readline
output = sys.stdout.write

'''
그냥 이중반복문으로 구하면 되려나?
시간복잡도는 O(n^2)이면 될 거같음.
시간초과났다.
'''
def solution():
    n,m = map(int,input().split())
    table = [list(map(int,input().split())) for _ in range(n)]
    for i in range(m):
        x1,y1,x2,y2 = map(int,input().split())
        answer = 0
        for x in range(x1-1,x2):
            for y in range(y1-1,y2):
                answer += table[x][y]
        print(answer)
    return

#역시나 DP문제였던 것..
def solution2():
    n,m = map(int,input().split())
    table = [list(map(int,input().split())) for _ in range(n)]
    dp = [[0]*(n+1) for _ in range(n+1)]

    for x in range(1,len(dp)):
        for y in range(1, len(dp[0])):
            # (1,1)에서 부터 (x,y)까지의 누적합 배열 dp 초기화
            dp[x][y] = dp[x-1][y] + dp[x][y-1] - dp[x-1][y-1] +table[x-1][y-1]
    for i in range(m):
        x1,y1,x2,y2 = map(int,input().split())
        #부분합은 (x2,y2)까지의 누적합에서 해당하지 않은 부분을 뺀 것
        answer = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
        print(answer)
        


if __name__ == "__main__":
    solution2()