def solution(array, commands):
    sub_array = [sorted(array[i-1:j])[k-1]for i,j,k in commands]
    
    return sub_array