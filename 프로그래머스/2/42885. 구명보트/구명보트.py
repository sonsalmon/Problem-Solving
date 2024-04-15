'''
탐욕 알고리즘으로 풀 수 없는 문제인 것 같다.
[40,40,60,60]이고 무게제한이 100이라면,
40,60씩 두 척이면 되는데 그리디로는 세 척이 필요하다.
아니면 무거운 사람부터 태우면?
'''
'''
1차 시도
def solution(people, limit):
    answer = 0
    people = sorted(people,reverse=True)
    
    
    while people:
        amount=limit
        capability=2
        i=0
        while i <len(people) and capability >0:
            if people[i]<=amount:
                amount-=people[i]
                capability -=1
                del people[i]
                
            else:
                i+=1
        answer +=1
                
'''                
#2차 시도 

#
'''
idea:
구명보트의 최대 인원수는 2명씩이므로 필요한 구명보트 수는 인원수 //2 또는 인원수 //2 +1이다.
몸무게로 내림차순 해서 절반을 태운다.
나머지 절반은 오름차순으로 정렬해서 태워본다. 
'''
def solution(people, limit):
    answer = 0
    if len(people)==1:
        return 1
    people = sorted(people,reverse=True)
    
    i = 0 #가장 무거운 사람 인덱스
    j = len(people)-1 #가장 가벼운 사람 인덱스
    
    while i <=j:
        if people[i]+ people[j] <=limit:
            i+=1
            j-=1
        else:
            i+=1 #무거운 사람 한 사람만 태움
        
        answer +=1
        
        
    return answer

