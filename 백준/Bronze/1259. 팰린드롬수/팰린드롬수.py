def solution(num):
    for i in range(len(num)//2):
        if num[i] != num[-(i+1)]:
            print('no')
            return

    print('yes')
    return
while True:
    num = input()
    if num =='0': break
    solution(num)