import sys
input = sys.stdin.readline
output = sys.stdout.write
'''
bfs아닌 거 같은데..
dfs?
그리디였구나..
'''

def solution():
    n = int(input())
    meetings = []
    for _ in range(n):
        i,j=map(int,input().split())
        meetings.append((i,j))
        
    meetings.sort(key=lambda x:(x[1],x[0]))
    
    count = 1
    end = meetings[0][1]
    for i in range(1,n):
        if meetings[i][0]>=end:
            end = meetings[i][1]
            count+=1

    return count

if __name__ == "__main__":
    print(solution())