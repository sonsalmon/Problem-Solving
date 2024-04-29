import sys
import heapq
input = sys.stdin.readline
output = sys.stdout.write

'''
class Heap:
    def __init__(self):
        self.heap =[] 
        self.depth = 0
    def is_empty(self):
        return True if len(self.heap)==0 else False
    def _change(self,parent,child):
        tmp = self.heap[child]
        self.heap[child] = self.heap[parent]
        self.heap[parent] = tmp
        
    def sort(self):
        current_index = len(self.heap) - 1
        parent_index = current_index//2
        while(parent_index >=0):
            if self.heap[parent_index]>self.heap[current_index]:
                self._change(parent_index,current_index)
                current_index=parent_index
                parent_index = current_index//2
            else:
                break
    def add(self, x):
        self.heap.append(x)
        self.sort()
        self.depth = len(self.heap)//2 + 1
    def pop(self):
        if not self.is_empty():
            root = self.heap[0]
            print(root)
            self.heap[0] = self.heap[-1]
            self.heap.pop(-1)
            parent = 0
            while(2*parent+2 < len(self.heap)):
                if self.heap[2*parent+1]< self.heap[2*parent+2]:
                    child = 2*parent+1
                else:
                    child=2*parent+2
                if  self.heap[parent]>self.heap[child]:
                    self._change(parent=parent,child=child)
                    parent = child
                else:
                    break
            if 2*parent + 1 <len(self.heap) and self.heap[parent]>self.heap[2*parent+1]:
                self._change(parent=parent,child=2*parent+1) 
                
        else:
            print('0')
                

'''

def solution():
    
    n = int(input())

    heap = []
    for i in range(n):
        x = int(input())
        if x ==0:
            if len(heap) ==0 :
                print('0')
            else:
                print(heapq.heappop(heap))
        else:
            heapq.heappush(heap,x)
    return

if __name__ == "__main__":
    solution()