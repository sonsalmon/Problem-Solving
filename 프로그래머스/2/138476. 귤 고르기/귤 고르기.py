'''
종류의 최솟값을 구해야 한다.
크기 : 개수로 딕셔너리를 구축한 후 내림차순으로 정렬.
개수가 많은 크기부터 k를 채운다.
'''
def solution(k, tangerine):
    answer = 0
    t = {}
    for i in tangerine:
        t[i] = t[i]+1 if i in t else 1
    
    t_num = sorted(t.items(),key=lambda x:x[1],reverse=True)
    
    tmp=0
    
    for _,num in t_num:
        tmp+=num
       	answer+=1
        if tmp>=k:
            break
        
            
            
    
    return answer