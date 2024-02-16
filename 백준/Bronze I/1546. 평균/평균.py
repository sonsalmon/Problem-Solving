import sys
input = sys.stdin.readline
output = sys.stdout.write

def solution():
    # write code down
    n = int(input())
    scores = list(map(int, input().split()))
    M = max(scores)
    for i in range(n):
        scores[i] = (scores[i]/M) * 100

    return sum(scores)/len(scores)
if __name__ == "__main__":
    print(solution())