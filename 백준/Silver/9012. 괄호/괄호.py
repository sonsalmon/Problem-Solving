import sys
input = sys.stdin.readline
output = sys.stdout.write

class Vps_stack:
    stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if self.have_item():
            item = self.stack[-1]
            del self.stack[-1]
            return item
        else:
            return None
            
    def have_item(self):
        if len(self.stack)>0:
            return True
        else:
            return False
    def flush(self):
        self.stack = []
    def check_vps(self, vps):


        for item in vps:
            if item == '(':
                self.push(item)
            elif item == ')':
                if self.have_item():
                    self.pop()
                else:
                    return "NO"
                    
        if self.have_item():
            return "NO" 
        else: 
            return "YES"
        
    

def solution():
    # write code down
    t = int(input())
    stack = Vps_stack()
    for i in range(t):
        vps = input()
        stack.flush()
        result = stack.check_vps(vps)
        print(result)
    

if __name__ == "__main__":
    solution()