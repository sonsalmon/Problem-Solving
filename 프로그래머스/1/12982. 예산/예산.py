'''
0-1 배낭 문제 아닌가?
무게만 맞추면 되고 가장 많이 넣어야 한다.
'''
def solution(d, budget):
    answer = 0
    d = sorted(d)
    for i in range(len(d)):
        if d[i]<=budget:
            budget -=d[i]
            answer +=1
        else:
            break
    return answer