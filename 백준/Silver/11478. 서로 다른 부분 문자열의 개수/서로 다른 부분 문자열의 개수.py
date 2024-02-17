import sys
input = sys.stdin.readline
output = sys.stdout.write

'''
idea
가능한 모든 substring을 구한다. > substring만드는 법 모름
set함수를 적용해 중복을 제거한다.
길이를 출력한다.
'''
def solution():
    # write code down
    line= list(input().strip())
    substring=[]
    for i in range(len(line)):
        for j in range(i+1,len(line)+1):
            substring.append(''.join(line[i:j]))

    set_string=set(substring)


    return len(set_string)

if __name__ == "__main__":
    # solution()
    print(solution())