from collections import Counter
import sys
input = sys.stdin.readline
output = sys.stdout.write
'''
노드들이 한 그래프 안에 있는지 확인
루트 노드가 같은지 확인해보자.
---
실패. 
구현하려고 했던 것 : 유니온 파인드

'''

def find_root(root_list, a):
    if root_list[a] == a:
        return a
    root_list[a] = find_root(root_list,root_list[a])    #경로 압축
    return root_list[a]




def solution():
    node = int(input())
    num_edge = int(input())
    edges = []
    root_list= [i for i in range(node+1)]

    for _ in range(num_edge):
        a,b = map(int,input().split())
        edges.append((a,b))

    for a,b in edges:
        root_a = find_root(root_list,a)
        root_b = find_root(root_list,b)
        root_list[max(root_a,root_b)] = min(root_a, root_b)     #루트 노드 기준 합치기
    


    for i in range(1,node+1):
        root_list[i]= find_root(root_list,i)
    
    answer = Counter(root_list)
    return answer[1] - 1    # 1번 컴퓨터 제외

if __name__ == "__main__":
    print(solution())