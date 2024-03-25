
def count(n,wires,i):
    start,_=wires.pop(i)
    graph = [[] for _ in range(n+1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n+1)
    visited[0]=True#0번 인덱스 사용하지 않음
    stack=[]
    
    stack.append(start)
    count=0
    while stack:
        current_node= stack.pop()
        visited[current_node] = True
        count+=1
        for adjacent_node in graph[current_node]:
            if visited[adjacent_node] != True:
                stack.append(adjacent_node)
    return count
            
            
    
    
def solution(n, wires):
    answer = -1
    
    node_num=[]
    for i in range(len(wires)):
        node_num.append(count(n,wires[:],i))
    print(node_num)
    return min([abs(n-num -num) for num in node_num])
    
    
    
    
    #idx = node_num.index(min([abs(n//2-num) for num in node_num]))
    
    
    
    
        
    
    return min([abs(n//2 - count(n, wires[:],i)) for i in range(len(wires))])
    
    
        
        
    