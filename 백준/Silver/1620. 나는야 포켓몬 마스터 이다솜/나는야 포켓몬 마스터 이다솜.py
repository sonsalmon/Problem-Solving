import sys
input = sys.stdin.readline
output = sys.stdout.write

'''
*input()받을 때 개행문자 제외하기
딕셔너리 value값으로 검색하기
'''
def solution():
    n, m = map(int, input().split())
    poketmon_dict={}
    num_dict={}
    for i in range(1,n+1):
        name = input().rstrip()
        poketmon_dict[i]=name
        num_dict[name]=i
    
    for j in range(m):
        question = input().rstrip()
        try:
            poketmon_num = int(question)
            print(poketmon_dict[poketmon_num])
        except:
            print(num_dict[question])


        



if __name__ == "__main__":
    solution()