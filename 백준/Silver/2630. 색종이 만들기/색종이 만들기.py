import sys
input = sys.stdin.readline
output = sys.stdout.write
'''
주어진 2차원 배열이 모두 같은 값인지 판단하려면?
모든 원소를xor 연산?
'''
'''
def check_colour(arr):
    if any(1 in l for l in arr) and any(0 in l for l in arr):
        return 2
    elif all(0 not in l for l in arr):
        return 1
    else:
        return 0
def make_sublist(arr,from_i,to_i,from_j,to_j):
    x=[]
    for i in range(from_i,to_i):
        x.append(arr[i][from_j:to_j])
    return x
def divide(arr,n):
    if n ==1:
        print('n==1, ',arr[0][0])
        return arr[0][0]
    n = n//2
    blue = white = 0
    arr_1 = make_sublist(arr,from_i=0,to_i=n,from_j=0,to_j=n)
    arr_2 = make_sublist(arr,from_i=n,to_i=2*n,from_j=0,to_j=n)
    arr_3 = make_sublist(arr,from_i=0,to_i=n,from_j=n,to_j=2*n)
    arr_4 = make_sublist(arr,from_i=n,to_i=2*n,from_j=n,to_j=2*n)

    # 1사분면

    colour_1 = check_colour(arr_1)
    if colour_1 ==2:
        b,w = divide(arr_1,n)
        blue +=b
        white += w
    elif colour_1 ==1:
        blue +=1
    elif colour_1 ==0:
        white +=1

    # 2사분면
    colour_2 = check_colour(arr_2)
    if colour_2 ==2:
        b,w = divide(arr_2,n)
        blue +=b
        white += w
    elif colour_2 ==1:
        blue +=1
    elif colour_2 ==0:
        white +=1

    # 3 사분면
    colour_3 = check_colour(arr_3)
    if colour_3 ==2:
        b,w = divide(arr_3,n)
        blue +=b
        white += w
    elif colour_3 ==1:
        blue +=1
    elif colour_3 ==0:
        white +=1
    # 4 사분면
    colour_4 = check_colour(arr_4)
    if colour_4 ==2:
        b,w = divide(arr_4,n)
        blue +=b
        white += w
    elif colour_4 ==1:
        blue +=1
    elif colour_4 ==0:
        white +=1

         
    
    return blue, white


'''
def div(arr,x,y,n):
    color = arr[x][y]
    result=[0,0]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != arr[i][j]:
                m = n//2
                arr1=div(arr,x,y,m)
                arr2=div(arr,x,y+m,m)
                arr3=div(arr,x+m,y,m)
                arr4=div(arr,x+m,y+m,m)
                return [arr1[0]+arr2[0]+arr3[0]+arr4[0],arr1[1]+arr2[1]+arr3[1]+arr4[1] ]
    if color==0:
        result[0] +=1
    else:
        result[1]+=1
    return result


def solution():
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

        
    white,blue = div(arr,0,0,n)
    print(white)
    print(blue)


    

if __name__ == "__main__":
    solution()