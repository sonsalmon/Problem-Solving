def solution(triangle):
    answer = 0
    sum = [[0]*i for i in range(1,len(triangle)+1)]
    sum[0][0]=triangle[0][0]
    sum[1][0]=sum[0][0] + triangle[1][0]
    sum[1][1]=sum[0][0] + triangle[1][1]
    for d in range(2,len(triangle)):
        for l in range(d+1):
            if l ==0:
                sum[d][l]=sum[d-1][l]+ triangle[d][l]
            elif l == d:
                sum[d][l]=sum[d-1][l-1]+ triangle[d][l]
            else:
                sum[d][l]=max(sum[d-1][l-1],sum[d-1][l]) + triangle[d][l]
            answer=max(answer,sum[d][l])
            
    return answer