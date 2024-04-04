def solution(n):
    '''
    
    ans = 0
    
    
    while n>1:
        if n % 2 !=0:#점프
            n -=1 
            ans +=1
            continue
        n /=2
    ans+=1
    
    return ans
    '''

    return bin(n).count('1')
  