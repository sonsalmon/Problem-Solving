def solution(records):
    answer = []
    message_format = {
        'Enter' : '님이 들어왔습니다.',
        'Leave' : '님이 나갔습니다.'
    }
    
    
    nickname_data={}
    for record in records:
        inst = record.split()
        if inst[0] =='Enter' or inst[0] == 'Change':
            nickname_data[inst[1]] = inst[2]
    
    
    for record in records:
        inst = record.split()
        if inst[0]=='Change':
            continue
        message = nickname_data[inst[1]]+message_format[inst[0]]
        answer.append(message)
        
    return answer