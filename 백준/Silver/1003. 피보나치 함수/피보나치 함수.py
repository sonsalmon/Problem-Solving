import sys
input = sys.stdin.readline
output = sys.stdout.write

#
# 시간 초과
# def fibo(n:int):
#     if n ==0 :
#         return 1,0
#     elif n ==1 :
#         return 0,1
#     else:
#         a_0, a_1 = fibo(n-1)
#         b_0,b_1 = fibo(n-2)
#         return a_0 + b_0, a_1+b_1

# def solution():
#     n = int(input())
#     for i in range(n):
#         num = int(input())
#         result = fibo(num)
#         print(*result)
    
        
def solution():
    T = int(input())
    
    zero = [1,0,1]
    one = [0,1,1]
    for _ in range(T):
        length = len(zero)
        num = int(input())
        if num>=length:
            for i in range(length,num+1):
                zero.append(zero[i-1]+zero[i-2])
                one.append(one[i-1]+one[i-2])
        print('{} {}'.format(zero[num], one[num]))


if __name__ == "__main__":
    solution()