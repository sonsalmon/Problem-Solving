import sys
input = sys.stdin.readline
output = sys.stdout.write
'''
땅과 초기 블럭이 주어졌을 때
땅 까기 VS 땅 쌓기 중 빠른 걸 선택해야 함.
아니지 중간에서 만나게 할 수도 있지.
1. 인벤토리에 있는 걸로 채울 수 있는지 확인
    1-1. 채울 수 있으면 채움
    1.2. 채울 수 없으면
        1-2-1. 가장 높은 높이의 블럭 전부 제거
---
그리디



'''

def solution():
    n,m,b = map(int, input().split())
    land = []
    for _ in range(n):
        land.extend(list(map(int,input().split())))
    max_height = max(land)
    min_height = min(land)
    best_time = float('inf')   # time[k] : 높이 k일 때 걸리는 시간
    best_height = 0
    
    for g in range(min_height,max_height+1):    # g 높이로 맞추기
        block = b
        current_time = 0
        for i in land:
            if i > g:
                block += i-g
                current_time += 2*(i-g)
            elif i<g:
                block -= g-i
                current_time += g-i
        if block >= 0 and current_time <=best_time:
            best_time = current_time
            best_height = g
            

    print(best_time, best_height)

if __name__ == "__main__":
    solution()