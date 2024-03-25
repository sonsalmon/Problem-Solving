import heapq
def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    distance = [float('INF')for _ in range(N+1)]
    distance[1]= 0
    
    #그래프 
    for start,end,cost in road:
        graph[start].append((end,cost))
        graph[end].append((start,cost))
    
    queue =[]
    #시작 노드는 1
    heapq.heappush(queue,[distance[1],1])
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        for adjacent_node, weight in graph[current_node]:
            new_distance = current_distance + weight
            if new_distance < distance[adjacent_node]:
                distance[adjacent_node] = new_distance 
                
                heapq.heappush(queue,[new_distance,adjacent_node])
                
        
    
    answer = 0
    for cost in distance:
        if cost<=K:
            answer+=1


    return answer