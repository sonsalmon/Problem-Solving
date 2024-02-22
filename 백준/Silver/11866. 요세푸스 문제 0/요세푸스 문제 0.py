import sys
input = sys.stdin.readline
output = sys.stdout.write


def del_person(people, k):
    if k <0:
        print('index error')
        return None
    else:
        if k >=len(people):
            k = k%len(people)
        tmp = people[k]
        del people[k]
        result_list = people[k:] + people[:k]
        return result_list, tmp


def solution():
    n,k = map(int,input().split())
    people = [i for i in range(1,n+1)]
    yosefus = []
    index = 0
    step = k-1
    

    # del_person(people,step)
    #반복
    while len(people)>0:
        people, num = del_person(people,step)
        yosefus.append(num)
        
    print('<'+', '.join(map(str,yosefus))+'>')
        


if __name__ == "__main__":
    solution()