def solution(topping):
    
    
    answer = 0
    front_num = []
    rear_num = []
    front_set=set()
    rear_set=set()
    length = len(topping)
    for i in range(length):
        j=length-(i+1)
        if topping[i] not in front_set:
            front_set.add(topping[i])
            front_num.append(len(front_set))
        else:
            front_num.append(front_num[-1])
        if topping[-i-1] not in rear_set:
            rear_set.add(topping[-i-1])
            rear_num.append(len(rear_set))
        else:
            rear_num.append(rear_num[-1])
    for i in range(length-1):# 한사람이 다 가져가는 경우는 없으므로
        if front_num[i]==rear_num[length-i-2]:
            answer+=1
        
        
        
        
    
    return answer