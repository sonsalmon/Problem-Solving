from collections import deque
def solution(maps):
    answer = 0
    visited = [[-1 for j in i] for i in maps]
    n = len(maps)
    m = len(maps[0])
    
    queue = deque()
    queue.append([0,0])
    visited[0][0]=1
    answer +=1
    di = [1,0,-1,0]
    dj = [0,1,0,-1]
    
    while queue:
        i,j = queue.popleft()
        #case 1: 아래
        
        #case 2: 오른쪽
        #case 3: 위
        #case 4: 왼쪽
    
        for r in range(len(di)):
            new_i = i +di[r]
            new_j = j +dj[r]
            if new_i<0 or new_j <0 or new_i>=len(maps) or new_j>=len(maps[0]):
                continue
            if maps[new_i][new_j] == 1 and visited[new_i][new_j] == -1:
                answer +=1
                queue.append([new_i,new_j])
                visited[new_i][new_j] = visited[i][j] +1
    
    
    
    return visited[n-1][m-1]