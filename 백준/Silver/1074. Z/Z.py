import sys
input = sys.stdin.readline
output = sys.stdout.write

'''
python int 최대는 몇이지?
- 제한 없음

'''
def solution():
    n,r,c = map(int,input().split())
    answer=0
    for i in range(n,0,-1):
        w = 2**i
        quadrant = (w//2)**2
        if c< w//2 and r < w//2:
            #1사분면
            continue
        elif c >=w//2 and r < w//2:
            #2사분면
            answer += quadrant
            c -= w//2
        elif c < w//2 and r >= w//2:
            #3사분면
            answer += 2*quadrant
            r -= w//2
        else:
            #4 사분면
            answer += 3*quadrant
            r -= w//2
            c -= w//2
            
    return answer

if __name__ == "__main__":
    print(solution())