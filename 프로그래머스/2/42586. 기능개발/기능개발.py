from collections import deque

'''
def solution(progresses, speeds):
    deploy_cnt = 0
    dq = deque(progresses)
    answer = []
    while len(dq)>0:
        for i in range(len(dq)):
            dq[i] += speeds[i]
                
        while dq[0]>=100:
            print(dq[0])
            deploy_cnt +=1
            dq.popleft()
        if deploy_cnt >0:
            answer.append(deploy_cnt)
            deploy_cnt = 0
    
    return answer
'''
def solution(progresses, speeds):
    time =0 
    cnt = 0
    answer =[]
    
    while len(progresses)>0:
        if (progresses[0] + time*speeds[0]) >=100:
            cnt +=1
            progresses.pop(0)
            speeds.pop(0)
        else:
            if cnt >0:
                answer.append(cnt)
                cnt=0
            time+=1
        
    answer.append(cnt)
            
    return answer
