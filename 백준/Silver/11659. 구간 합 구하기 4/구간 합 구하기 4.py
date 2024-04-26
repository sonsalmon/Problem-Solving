import sys
input = sys.stdin.readline
output = sys.stdout.write

def solution():
    n,m = map(int,input().split())
    nums = list(map(int,input().split()))
    num_sum = [0]*n
    num_sum[0] = nums[0]
    for i in range(1,len(num_sum)):
        num_sum[i] = num_sum[i-1] + nums[i]
    for _ in range(m):
        i,j = map(int,input().split())

        print(num_sum[j-1]- (num_sum[i-2] if i>1 else 0))
    
if __name__ == "__main__":
    solution()