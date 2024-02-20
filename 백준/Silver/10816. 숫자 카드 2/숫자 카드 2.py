import sys
input = sys.stdin.readline
output = sys.stdout.write

'''
1<=n<=500,000
10,000,000 <= cards[i]<=10,000,000
1<= m <=500,000
10,000,000 <= numbers[i] <=10,000,000
'''
def solution():
    n = int(input())
    cards = list(map(int,input().split()))
    m = int(input())
    numbers = list(map(int,input().split()))
    result = [0] * m
    
    cards_dict={}
    for card in cards:
        cards_dict[card] = cards_dict[card] + 1 if card in cards_dict else 1
        

    for i, num in enumerate(numbers):
        if num in cards_dict:
            result[i] = cards_dict[num]
        
    return result

if __name__ == "__main__":
    print(*solution())