import sys
input = sys.stdin.readline
output = sys.stdout.write
'''
집합연산
교집합 &
합집합 |
'''

def solution():
    n, m = map(int,input().split())
    never_seen=set()
    never_heard=set()
    for _ in range(n):
        never_heard.add(input().strip())
    for _ in range(m):
        never_seen.add(input().strip())
    never_sean_and_heard= never_heard & never_seen
    
    print(len(never_sean_and_heard))

    for name in sorted(list(never_sean_and_heard)):
        print(name)
        

if __name__ == "__main__":
    solution()