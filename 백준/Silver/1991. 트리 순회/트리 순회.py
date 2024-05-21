import sys
import copy
input = sys.stdin.readline
output = sys.stdout.write


def preorder(tree,visited,current,result):
    if not visited[current]:
        visited[current] = True
        result.append(current)
    if tree[current][0] != '.':
        result = preorder(tree,visited,tree[current][0],result)
    if tree[current][1] != '.':
        result = preorder(tree,visited,tree[current][1],result)
    return result
def inorder(tree,visited,current,result):
    if tree[current][0] != '.':
        result = inorder(tree,visited,tree[current][0],result)
    if not visited[current]:
        visited[current] = True
        result.append(current)
    if tree[current][1] != '.':
        result = inorder(tree,visited,tree[current][1],result)
    return result
def postorder(tree,visited,current,result):
    if tree[current][0] != '.':
        result = postorder(tree,visited,tree[current][0],result)
    if tree[current][1] != '.':
        result = postorder(tree,visited,tree[current][1],result)
    if not visited[current]:
        visited[current] = True
        result.append(current)
    return result



    
def solution():
    n = int(input())
    tree = dict()
    visited = dict()
    for i in range(n):
        node, left, right = input().split()
        tree[node] = (left,right)
        visited[node] = False
    preorder_result = preorder(tree,copy.deepcopy(visited),'A',[])
    inorder_result = inorder(tree,copy.deepcopy(visited),'A',[])
    postorder_result = postorder(tree,copy.deepcopy(visited),'A',[])
    print(''.join(preorder_result))
    print(''.join(inorder_result))
    print(''.join(postorder_result))

        
    
    return

if __name__ == "__main__":
    solution()