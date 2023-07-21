"""
stack 
Author:LXQing
Date:2023/7/4
"""
class Stack:
    def __init__(self):
        self.stack=[]  # 初始化一个栈
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        return self.stack.pop()
    def top(self):   # 栈顶
        if self.empty():
            return 'Stack is empty'
        return self.stack[-1]
    def empty(self):
        return self.stack==[]
    def size(self):
        return len(self.stack)
    def size(self):
        return len(self.stack)
if __name__ == '__main__':
    stack=Stack()
    stack.push(1)
    # stack.pop()
    stack.push(2)
    # stack.top()
    # stack.empty()
    print(stack.stack)
    print(stack.size())