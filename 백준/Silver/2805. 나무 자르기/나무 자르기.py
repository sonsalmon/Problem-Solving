import sys
input = sys.stdin.readline
output = sys.stdout.write

'''
이진탐색

'''
def solution():
    # write code down
    n,m = map(int,input().split())
    trees = list(map(int,input().split()))
    start, end = 1, max(trees)

    while start <=end:
        mid = (start + end) //2
        sum = 0

        for tree in trees:
            if tree > mid:
                sum += tree-mid
        
        if sum < m: # 가져갈 수 있는 나무가 목표보다 적음
            end = mid -1 # 높이를 낮춤
        if sum >=m: # 나무가 목표보다 많음
            start = mid +1 # 높이를 높임
            
    
    return end

if __name__ == "__main__":
    print(solution())