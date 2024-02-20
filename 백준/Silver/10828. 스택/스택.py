import sys
input = sys.stdin.readline
output = sys.stdout.write

#자료형 정수형으로만 고정 어떻게 함??
class My_stack():
    _stack=[]
    def push(self, item):
        self._stack.append(item)
    def pop(self):
        if len(self._stack)>0:
            tmp = self._stack[-1]
            del self._stack[-1]
            return tmp
        else:
            return -1
    def size(self):
        return len(self._stack)
    def empty(self):
        if len(self._stack) ==0:
            return 1
        else:
            return 0
    def top(self):
        if not self.empty():
            return self._stack[-1]
        else:
            return -1

def solution():
    n = int(input())
    
    stack = My_stack()
    for _ in range(n):
        inst = input().split()
        # print(stack._stack)
        
        if inst[0] == 'push':
            stack.push(int(inst[1]))
        elif inst[0] == 'pop':
            print(stack.pop())
        elif inst[0] == 'size':
            print(stack.size())
        elif inst[0] == 'empty':
            print(stack.empty())
        elif inst[0] == 'top':
            print(stack.top())
        
    
    

if __name__ == "__main__":
    solution()