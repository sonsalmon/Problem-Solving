def solution(n, words):
    answer = [0,0]
    words_set= set()
    num=0
    cnt=0
    for i in range(len(words)):
        num = i % n +1
        cnt = i//n + 1
        if i>0 and words[i-1][-1] != words[i][0]:
            answer = [num,cnt]
            break
        if words[i] in words_set:
            answer = [num,cnt]
            break
        words_set.add(words[i])
            
    return answer