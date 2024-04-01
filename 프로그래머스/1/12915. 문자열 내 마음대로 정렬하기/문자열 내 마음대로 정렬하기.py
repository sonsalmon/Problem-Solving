# 문자가 같은 경우가 문제. 어떻게 처리하지?

def solution(strings, n):
    answer = []
    return sorted(strings,key=lambda x:(x[n],x))