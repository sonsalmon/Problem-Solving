import sys
input = sys.stdin.readline
output = sys.stdout.write
'''
제일 작은 수가 0으로 바뀜. 자기보다 작은 수가 0개이므로

'''
def solution():
    n = int(input())
    nums = list(map(int,input().split()))
    sorted_nums = sorted(nums)
    compact_dict = {}
    order = 0
    for i in range(n):
        if sorted_nums[i] in compact_dict:
            continue
        compact_dict[sorted_nums[i]] = order
        order+=1
        
    for i in range(n):
        nums[i] = compact_dict[nums[i]]
    
    print(*nums)

if __name__ == "__main__":
    solution()