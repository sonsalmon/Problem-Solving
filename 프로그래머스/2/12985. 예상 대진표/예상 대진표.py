def solution(n,a,b):
    answer = 0
    answer +=1
    while (a+1)//2 != (b+1)//2:
        a = (a+1)//2
        b = (b+1)//2
        answer +=1
    return answer