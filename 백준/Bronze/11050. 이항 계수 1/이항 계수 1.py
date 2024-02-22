import sys
input = sys.stdin.readline
output = sys.stdout.write

'''
# 이항 계수
주어진 집합에서 원하는 개수만큼 순서없이 뽑는 조합의 개수
(nk) = nCk = n!/(n-k)!k!
'''
# def factorial(i:int):
#     if i > 1:
#         return i*(i-1)

#     elif i == 1 or i ==0:
#         return 1
#     else:
#         return None

def binary_coef(n,k):
    if k ==0 or k ==n:
        return 1
    else:
        return binary_coef(n-1,k-1)+binary_coef(n-1,k)
def solution():
    # write code down

    n, k = map(int, input().split())
    return binary_coef(n,k)

    
    

if __name__ == "__main__":
    print(solution())