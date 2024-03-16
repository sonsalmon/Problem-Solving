'''
가능한 종류는 1~N/2
각 종류의 폰켓몬이 몇마리씩 있는지 구한다.
N/2를 넘지 않는 최대 종류를 포함하는 조합을 구한다.

'''
def solution(nums):
    answer = 0
    num_dict = {}
    for num in nums:
        if num in num_dict:
            num_dict[num]+=1
        else:
            num_dict[num]=1
    
    
    # num_dict의 value값들을 선택해 더했을 때 N/2를 넘지 않는 경우의 수?
    n = len(nums)
    if n//2 <= len(num_dict):
        answer = n//2
    else:
        answer = len(num_dict)
    
    return answer