# minstack: http://www.lintcode.com/en/problem/min-stack/

class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.stack = []
        self.minStack = []
        
    def push(self, number):
        self.stack.append(number)
        if len(self.minStack) == 0:
            self.minStack.append(number)
        else:
            self.minStack.append(min(self.minStack[-1], number))

    def pop(self):
        # pop and return the top item in stack
        result = self.stack.pop()
        self.minStack.pop()
        return result

    def min(self):
        # return the minimum number in stack
        return self.minStack[-1]

myStack = MinStack()
myStack.push(1)
print myStack.pop()
myStack.push(2)
myStack.push(3)
print myStack.min()
myStack.push(1)
print myStack.min()
