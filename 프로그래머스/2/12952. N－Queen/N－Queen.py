'''
행마다 퀸을 하나씩 놓도록 한다.
다음 위치가 유망하다면 그 위치에서 다음 행에 대해 살펴본다.
현재 퀸의 위치를 담을 배열 필요
유망함수
백트래킹 함수
	만약 배치가 완료 되었다면 카운트 증가시키고 True 리턴
    만약 유망하다면
    	다음 위치에 퀸 배치
        
    
'''
    
def backtrack(n,current_row,width,diagonal1,diagonal2):
    cnt=0
    if current_row==n:
       	cnt +=1
    else:
        for i in range(n):
            if width[i] or diagonal1[i+current_row] or diagonal2[i-current_row +n]:
                continue
                
            width[i] = diagonal1[i+current_row] = diagonal2[i-current_row+n] = True
            cnt += backtrack(n,current_row+1,width,diagonal1,diagonal2)
            width[i] = diagonal1[i+current_row] = diagonal2[i-current_row+n] = False
            
    return cnt
            
    
    
    
    
def solution(n):
    width = [False]*n
    diagonal1=[False]*n*2
    diagonal2=[False]*n*2
    answer = backtrack(n,0,width,diagonal1,diagonal2)
    return answer