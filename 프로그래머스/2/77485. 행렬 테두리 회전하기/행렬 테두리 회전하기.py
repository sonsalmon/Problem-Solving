def rotate(matrix, query):
    '''
    1.행값 바뀜
    	1.1. 행값 +1 y2열에서 [x1:x2]
        2.2. 행값 -1 y1열에서 [x1+1:x2+1]
    2.열값 바뀜
    	2.1. 열값 +1	x1행에서 [y1:y2]
        2.2. 열값 -1	x2행에서 [y1+1:y2+1]
    
    '''
    x1,y1,x2,y2 = query
    x1=x1-1
    y1=y1-1
    x2=x2-1
    y2=y2-1
    mat_min = tmp = matrix[x1][y1]
    
    for i in range(x1,x2):
        matrix[i][y1] = matrix[i+1][y1] 
        mat_min= find_min(mat_min,matrix[i][y1])
        
    for j in range(y1,y2):
        matrix[x2][j] = matrix[x2][j+1]
        mat_min=find_min(mat_min,matrix[x2][j])
        
    for i in range(x2,x1,-1):
        matrix[i][y2] = matrix[i-1][y2] 
        mat_min=find_min(mat_min,matrix[i][y2])
        
    for j in range(y2,y1+1,-1):
        matrix[x1][j] = matrix[x1][j-1]
        mat_min=find_min(mat_min,matrix[x1][j])
        
        
    matrix[x1][y1+1] = tmp
    return matrix, mat_min
        
def find_min(current_min, value):
    return current_min if current_min <= value else value
def solution(rows, columns, queries):
    
    #matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    
    matrix = [[(i)*columns +(j+1) for j in range(columns)] for i in range(rows)]
    answer = []
    
    for query in queries:
        matrix, min_value = rotate(matrix, query)
        answer.append(min_value)
        
    
    return answer
