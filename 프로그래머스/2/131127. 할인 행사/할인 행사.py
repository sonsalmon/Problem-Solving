def make_dic(items):
    dic = {}
    for item in items:
        if item in dic:
            dic[item]+=1
        else:
            dic[item] = 1
    return dic
        
def check_items(want,number,discount_dic):
    for want_item, num in zip(want,number):
        if want_item not in discount_dic:
            return False
        elif discount_dic[want_item]<num:
            
            return False
            
    return True

def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9):
        discount_dic = make_dic(discount[i:i+10])
        if check_items(want,number,discount_dic):
            answer +=1
                
        
    return answer