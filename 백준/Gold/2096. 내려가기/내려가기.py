import sys
input = sys.stdin.readline
output = sys.stdout.write
'''
dp인듯
깊은복사?? - mutable 객체의 깊은 복사
-
실패 - 메모리 초과
공간복잡도 계산해야할듯
그냥 dp로는 안 되고 슬라이딩 윈도우 사용해야함
'''
#메모리 초과 실패
def solution():
    n = int(input())
    num_table =[]
    dp_max = [[0]*3 for _ in range(n)]
    dp_min = [[0]*3 for _ in range(n)]
    for _ in range(n):
        num_table.append(list(map(int,input().split())))
    dp_max[0] = num_table[0]
    dp_min[0] = num_table[0]

    
    for i in range(1,n):
        dp_max[i][0]= max(dp_max[i-1][0],dp_max[i-1][1]) + num_table[i][0]
        dp_max[i][1]= max(dp_max[i-1]) + num_table[i][1]
        dp_max[i][2]= max(dp_max[i-1][1],dp_max[i-1][2]) + num_table[i][2]
        
        dp_min[i][0]= min(dp_min[i-1][0],dp_min[i-1][1]) + num_table[i][0]
        dp_min[i][1]= min(dp_min[i-1]) + num_table[i][1]
        dp_min[i][2]= min(dp_min[i-1][1],dp_min[i-1][2]) + num_table[i][2]
    
    print(max(dp_max[-1]), min(dp_min[-1]))


#역시나 메모리 초과
def solution2():
    n = int(input())
    num_list =[]
    for _ in range(n):
        a,b,c = map(int,input().split())
        num_list.append([[a,a],[b,b],[c,c]])
    for i in range(1,n):
        num_list[i][0][0]= max(num_list[i-1][0][0],num_list[i-1][1][0]) + num_list[i][0][0]
        num_list[i][1][0]= max(num_list[i-1],key=lambda x:x[0])[0] + num_list[i][1][0]
        num_list[i][2][0]= max(num_list[i-1][1][0],num_list[i-1][2][0]) + num_list[i][2][0]
        
        num_list[i][0][1]= min(num_list[i-1][0][1],num_list[i-1][1][1]) + num_list[i][0][1]
        num_list[i][1][1]= min(num_list[i-1],key=lambda x:x[1])[1] + num_list[i][1][1]
        num_list[i][2][1]= min(num_list[i-1][1][1],num_list[i-1][2][1]) + num_list[i][2][1]
    
    print(max(num_list[-1],key=lambda x:x[0])[0], min(num_list[-1],key=lambda x:x[1])[1])


def solution3():
    n = int(input())
    arr = list(map(int,input().split()))
    max_dp = arr
    min_dp = arr
    for i in range(n-1):
        arr = list(map(int,input().split()))
        max_dp = [arr[0] + max(max_dp[0],max_dp[1]), arr[1] + max(max_dp), arr[2] + max(max_dp[1],max_dp[2])]
        min_dp = [arr[0] + min(min_dp[0],min_dp[1]), arr[1] + min(min_dp), arr[2] + min(min_dp[1],min_dp[2])]
    print(max(max_dp),min(min_dp))

if __name__ == "__main__":
    solution3()