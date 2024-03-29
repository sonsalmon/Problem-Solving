import sys
input = sys.stdin.readline
output = sys.stdout.write

def find_order(num_list, idx, operand,result):
    global max_num, min_num
    if idx == len(num_list):
        max_num = max(max_num,result)
        min_num = min(min_num,result)
        return result
    
    for i in range(4):
        if operand[i]>0:
            operand[i] -=1
            if i== 0:# add
                find_order(num_list,idx+1,operand,result + num_list[idx])
            if i==1: # sub
                find_order(num_list,idx+1,operand,result - num_list[idx])
            if i==2: # mul
                find_order(num_list,idx+1,operand,result * num_list[idx])
            if i==3: # sub
                find_order(num_list,idx+1,operand,int(result/num_list[idx]))
            operand[i] +=1
            




def solution():
    n = int(input())
    num_list = list(map(int,input().split()))

    operand = list(map(int,input().split()))
    global max_num, min_num
    max_num = -1e10
    min_num = 1e10
    find_order(num_list,idx=1,operand=operand,result=num_list[0])

    
    print(max_num)
    print(min_num)

if __name__ == "__main__":
    solution()