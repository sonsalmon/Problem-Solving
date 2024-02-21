import sys
input = sys.stdin.readline
output = sys.stdout.write

class Queue():
    _q = []
    def push(self,item):
        self._q.append(item)

    def pop(self):
        if not self.empty():
            tmp = self._q[0]
            del self._q[0]
            return tmp
        else:
            return -1
    def size(self):
        return len(self._q)
    def empty(self):
        return 1 if self.size() == 0 else 0
    def front(self):
        if not self.empty():
            return self._q[0]
        else:
            return -1
    def back(self):
        if not self.empty():
            return self._q[-1]
        else:
            return -1

def solution():
    n = int(input())
    
    queue = Queue()
    for i in range(n):
        inst = input().split()
        
        if inst[0] == 'push':
            queue.push(int(inst[1]))
        elif inst[0] == 'pop':
            print(queue.pop())
        elif inst[0] == 'size':
            print(queue.size())
        elif inst[0] == 'empty':
            print(queue.empty())
        elif inst[0] == 'front':
            print(queue.front())
        elif inst[0] == 'back':
            print(queue.back())
    

if __name__ == "__main__":
    solution()