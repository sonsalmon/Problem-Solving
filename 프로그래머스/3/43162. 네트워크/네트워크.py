'''

def solution(n, computers):
    answer = 0
    network ={}
    networks = [i for i in range(n)]
    def find_root(num):
        if networks[num] == num:
            return num
        networks[num] = find_root(networks[num])
        return networks[num]
        
    for i in range(n):
        for j in range(i+1,n):
            if computers[i][j] ==1:
                print(networks)
                networks[j] = find_root(i)
                
                
    num_net = set(networks)
        
    answer = len(num_net)
            
            
            
    return answer
'''

def solution(n, computers):
    answer = 0
    networks = [i for i in range(n)]  # 각 노드의 네트워크 번호를 저장하는 배열

    # 두 노드가 속한 네트워크의 루트를 찾는 함수
    def find_root(num):
        if networks[num] == num:
            return num
        networks[num] = find_root(networks[num])
        return networks[num]

    # 두 네트워크를 결합하는 함수
    def union_network(a, b):
        root_a = find_root(a)
        root_b = find_root(b)
        if root_a != root_b:
            networks[root_b] = root_a

    # 모든 노드들을 순회하면서 네트워크 결합
    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                union_network(i, j)

    # 네트워크 루트의 개수를 세어 반환
    answer = len(set(map(find_root, networks)))
    return answer