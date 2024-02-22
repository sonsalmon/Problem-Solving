import sys
input = sys.stdin.readline
output = sys.stdout.write

class Node():
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next
class Deque():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    def push_front(self, item:int):
        new_node = Node(item)
        if self.length==0:
            self.first = self.last = new_node
        else:
            new_node.next = self.first
            self.first.prev = new_node
            self.first = new_node
        self.length +=1
    def push_back(self, item:int):
        new_node = Node(item)
        if self.length==0:
            self.first= self.last = new_node
        else:
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node
        self.length +=1
    def pop_front(self):
        if self.empty():
            return -1
        else:
            new_front = self.first.next
            result = self.first.data
            del self.first
            self.first = new_front
            self.length -=1
            return result
            
    def pop_back(self):
        if self.empty():
            return -1
        else:
            new_back = self.last.prev
            result = self.last.data
            del self.last
            self.last = new_back
            self.length -=1
            return result
    def size(self):
        return self.length
    def empty(self):
        return 1 if self.size() == 0 else 0
    def front(self):
        return self.first.data if not self.empty() else  -1
    def back(self):
        return self.last.data if not self.empty() else -1
    

def solution():
    n = int(input())
    
    dq = Deque()
    for _ in range(n):
        inst = input().split()
        
        if inst[0] == 'push_front':
            dq.push_front(int(inst[1]))
        elif inst[0] == 'push_back':
            dq.push_back(int(inst[1]))
        elif inst[0] == 'pop_front':
            print(dq.pop_front())
        elif inst[0] == 'pop_back':
            print(dq.pop_back())
        elif inst[0] == 'size':
            print(dq.size())
        elif inst[0] == 'empty':
            print(dq.empty())
        elif inst[0] == 'front':
            print(dq.front())
        elif inst[0] == 'back':
            print(dq.back())


if __name__ == "__main__":
    solution()