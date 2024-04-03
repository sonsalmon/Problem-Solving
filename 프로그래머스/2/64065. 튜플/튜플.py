'''

튜플의 리스트로 변환
튜플의 길이 오름차순으로 정렬
각 튜플을 집합으로 변환
첫번째 원소 정답 리스트에 삽입
i번째 원소와 i+1원소의 차집합을 정답리스트에 삽입

'''
def solution(s):
    #바깥 괄호 제거
    s=s[2:-2]
    answer = []
    #문자열 파싱
    tmp = s.split('},{')
    #int 집합의 리스트로 변환
    t_list=[set(map(int,item.split(','))) for item in tmp]
    #집합의 길이로 정렬
    t_list.sort(key=lambda x:len(x))
    
    answer=list(t_list[0])
    for i in range(1,len(t_list)):
        sub=t_list[i]-t_list[i-1]
        answer +=sub
        
    
    return answer