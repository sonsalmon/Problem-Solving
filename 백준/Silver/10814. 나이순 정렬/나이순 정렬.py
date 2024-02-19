import sys
input = sys.stdin.readline
output = sys.stdout.write

# python의 stable 정렬 
def solution():

    
    n = int(input())
    members = []
    for i in range(n):
        age, name = input().split()
        members.append((int(age), name))
    

    # sort()에 비교하고 싶은 dict 키를 줄 수 있나??
    members.sort(key = lambda x:x[0])
    for member in members:
        print(member[0], member[1])

    
        


if __name__ == "__main__":
    solution()