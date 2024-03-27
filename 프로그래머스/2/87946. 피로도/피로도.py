    
'''
1. 만약 현재 피로도가 최소필요 피로도보다 높다면 해당 던전을 방문처리하고 피로도를 감소시킨 후 다음 방문 던전을 탐색한다.
2.더이상 방문할 수 없다면 백트래킹한다. 모든 노드를 방문했거나, 피로도가 모자람.
3. 가능한 모든 조합을 살펴보고 최대 던전 값을 갱신한다.

'''
max_dungeon=0
def find_solution(current_energy, visited, dungeons):
    global max_dungeon
    if max_dungeon == len(dungeons):
        return max_dungeon
    
    for i,(need,cost) in enumerate(dungeons):
        if current_energy >= need and i not in visited:
            visited.append(i)
            if len(visited)>max_dungeon:
                max_dungeon = len(visited)
            find_solution(current_energy-cost,visited,dungeons)
            visited.pop()
    return max_dungeon
            
    
def solution(k, dungeons):
    
    answer=find_solution(k,[],dungeons)
        
        
    return answer