        
        

def solution(enroll, referral, seller, amount):
    answer = []
    parent = dict(zip(enroll, referral))
    total = {name:0 for name in enroll}
    
    for name, num in zip(seller, amount):
        money = num *100
        cur_name = name
        
        while money >0 and cur_name != "-":
            total[cur_name] += money - (money//10)
            cur_name = parent[cur_name]
            money = money//10
        
        
    return [total[name] for name in enroll]