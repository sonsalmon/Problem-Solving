# 문제 : 다음 행의 최댓 값이 지금 행의 최댓값과 같은 열에 있을 때.
# 그렇지 않다면 각 행의 최댓값의 합만 구해도 됨.
def solution(land):
    answer = 0
    for i in range(1,len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][:j]+land[i-1][j+1:])


    answer = max(land[-1])
    return answer