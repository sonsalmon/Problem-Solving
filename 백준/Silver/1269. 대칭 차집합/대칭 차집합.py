import sys
input = sys.stdin.readline
output = sys.stdout.write

def solution():
    # write code down
    num_a, num_b = map(int,input().split())
    set_a = set(map(int,input().split()))
    set_b = set(map(int,input().split()))
    return len((set_a-set_b)|(set_b-set_a))

if __name__ == "__main__":
    print(solution())