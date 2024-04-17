import sys
input = sys.stdin.readline
output = sys.stdout.write

def solution():
    n = int(input())
    s = set()
    for i in range(n):
        inst= input().split()
        
        if inst[0] =='add':
            s.add(inst[1])
        elif inst[0] =='remove':
            s.discard(inst[1])
        elif inst[0] =='check':
            if inst[1] in s:
                print('1')
            else:
                print('0')
        elif inst[0] =='toggle':
            if inst[1] in s:
                s.remove(inst[1])
            else:
                s.add(inst[1])
        elif inst[0] =='all':
            s = set('1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20'.split())
        elif inst[0] =='empty':
            s = set()

        
if __name__ == "__main__":
    solution()