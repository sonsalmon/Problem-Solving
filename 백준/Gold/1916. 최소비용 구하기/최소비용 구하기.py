import heapq
import sys
input = sys.stdin.readline
output = sys.stdout.write
'''
다익스트라 알고리즘 최단경로
'''

def solution():
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        dep, des, cost = map(int,input().split())
        graph[dep].append([des,cost])
    start, end = map(int,input().split())

    distances = [float('inf')] * (n+1)
    distances[start] = 0
    queue =[]
    heapq.heappush(queue,[distances[start],start])
    
    while queue:
        distance, node = heapq.heappop(queue)
        if distances[node] < distance:
            continue
        
        for next_node, next_dist in graph[node]:
            if distances[next_node] > distance + next_dist:
                distances[next_node] = distance+next_dist
                heapq.heappush(queue,[distance+next_dist, next_node])
    

    return distances[end]

if __name__ == "__main__":
    print(solution())