'''
하나의 기지국이 커버하는 범위 : 2*w + 1
1부터 첫번째 기지국
i ~ i+1 기지국 사이
마지막 기지국부터 끝까지
'''
def solution(n, stations, w):
    answer = 0
    
    coverage = 2*w+1 # 하나의 기지국이 커버하는 범위
    for i in range(len(stations)-1):
        
        #no_signal_num= range(stations[i]+w+1, stations[i+1]-w)
        no_sig_num = stations[i+1]-stations[i] - (2*w)-1 #기지국 사이 신호 없는 아파트 개수
        answer += no_sig_num//coverage
        if no_sig_num % coverage !=0: #만약 딱 떨어지지 않으면 기지국 하나 더 세워야 함.
            answer +=1
    
    front = stations[0]-w-1
    rear = n-stations[-1]-w
    if front >0:
        answer += front//coverage
        if front % coverage !=0: #만약 딱 떨어지지 않으면 기지국 하나 더 세워야 함.
            answer +=1
    if rear >0:
        answer += rear//coverage
        if rear % coverage !=0: #만약 딱 떨어지지 않으면 기지국 하나 더 세워야 함.
            answer +=1

    return answer