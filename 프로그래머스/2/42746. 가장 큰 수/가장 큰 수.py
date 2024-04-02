import functools
def compare(a,b):
    a_first= str(a)+str(b)
    b_first = str(b)+str(a)
    if int(a_first)<int(b_first):
        return 1
    else:
        return -1
def solution(numbers):
    answer=''
        
    new_list=[]
    for number in numbers:
        number=str(number)
        new_list.append((number[0],number))
    
    
        
    new_list = sorted(numbers,key=functools.cmp_to_key(compare))
    answer = ''.join(map(str,new_list))
    
        
        
    return '0' if answer[0]=='0' else answer