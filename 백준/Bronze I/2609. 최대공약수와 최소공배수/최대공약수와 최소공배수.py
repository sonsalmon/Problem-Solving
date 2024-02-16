import sys
input = sys.stdin.readline
output = sys.stdout.write

def get_gcd(a,b):


    r = a%b
    if r == 0:
        return b
    else:
        return get_gcd(b,r)

def solution():
    a,b = map(int,input().split())
    '''
    최대공약수 : a,b의 최대공약수는 a를 b로 나눈 나머지가 r일 때 b와 r의 최대공약수와 같다.(유클리드 호제법)
    최소공배수 : ab/최대공약수(a,b)
    
    '''
    if a>=b:
        gcd = get_gcd(a,b)
    else:
        gcd = get_gcd(b,a)
    lcm = int(a*b / gcd)
    
    return gcd, lcm 

if __name__ == "__main__":
    gcd, lcm = solution()
    print(gcd)
    print(lcm)