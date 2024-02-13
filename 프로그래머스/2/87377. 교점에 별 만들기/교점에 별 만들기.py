'''
두 직선 사이 교점은 0개 또는 1개이다.
만약 ad - bc == 0이면 두 직선은 평행 또는 일치한다.
일치하는 것은 무수히 많은 교점이 생기는 것 -> 제한사항에 명시 존재하지 않음
그렇지 않으면 두 직선 사이에 교점이 1개 존재한다.

'''

def solution(line):
    position =[]
    answer = []
    x_min = y_min = int(1e15)
    x_max = y_max = -int(1e15)
    
    for i in range(len(line)):
        a,b,e = line[i]
        for j in range(i+1,len(line)):
            c,d,f = line[j]
            if a*d == b*c:
                continue
            else:
                x = (b*f-e*d)/(a*d - b*c)
                y = (e*c-a*f)/(a*d - b*c)
                if x ==int(x) and y == int(y):
                    x = int(x)
                    y = int(y)
                    position.append([x,y])
                    #최대 최소 좌표 찾기
                    if x_min > x : x_min = x
                    if y_min > y : y_min = y
                    if x_max < x : x_max = x
                    if y_max < y : y_max = y
    x_len = x_max-x_min+1
    y_len = y_max-y_min+1
    coord = [['.']*x_len for _ in range(y_len)]
    
    for star_x, star_y in position:
        n_x = star_x + abs(x_min) if x_min <0 else star_x - x_min
        n_y = star_y + abs(y_min) if y_min <0 else star_y - y_min
        coord[n_y][n_x] = '*'
        
    for result in coord: answer.append(''.join(result))
            
    return answer[::-1]