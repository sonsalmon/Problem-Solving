'''
노랑으로 만든 사각형을 
갈색 타일이 감쌀 수 있는지 확인한다.
노랑이 w * h의 사각형일 때 필요한 갈색 타일 개수는
2*w + 2*h + 4이다.
이때 노랑으로 만들 수 있는 사각형의 경우의 수는 노랑 타일 개수를 2개의 숫자로 인수분해 할 수 있는 경우의 수다.

y = w*h
b = 2*(w+h)+4
y+b = (w+2)*(h+2)
2.
갈색으로 만든 테두리 안에 노랑이 들어갈 수 있는지 확인한다.

'''
def solution(brown, yellow):
    
    answer = []
    for h in range(1,int(yellow **0.5) +1):
        w = yellow//h
        if h * w != yellow:
            continue
        if 2*(w+h)+4 == brown:
            answer=[w+2,h+2]
        
    
    
    
    return answer