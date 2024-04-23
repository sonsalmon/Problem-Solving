import sys
input = sys.stdin.readline
output = sys.stdout.write
'''

시작점을 제외하고 생각하면, 한칸을 오른 후에는 반드시 두칸을 올라야 한다.
두칸을 오른 후는 선택할 수 있다.
시작은 첫번째 계단으로 가는 것과 두번째 계단으로 가는 것 두가지가 있다.
거꾸로 내려와야하나?
어떤 알고리즘을 써야하지? - DP
'''

def solution():
    n = int(input())
    steps = [0] *n
    scores = [0]*n
    for i in range(n):
        steps[i] = int(input())
    if n==1:
        return steps[0]
    elif n ==2:
        return sum(steps)

    scores[0] = steps[0]
    scores[1]= sum(steps[:2])
    for i in range(2,n):
        scores[i] = max(scores[i-2], scores[i-3]+steps[i-1]) + steps[i]
        
    return scores[-1]

if __name__ == "__main__":
    print(solution())