def solution(participant, completion):
    participant_dic = {name:0 for name in participant}
    
    for name in participant:
        participant_dic[name] += 1
    
    for name in completion:
        participant_dic[name] -= 1
        
    for k,v in participant_dic.items():
        if v >0:
            return k
