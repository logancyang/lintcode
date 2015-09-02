# queueBy2Stacks: http://www.lintcode.com/en/problem/implement-queue-by-two-stacks/


class Queue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def adjust(self):
        # adjust only when stack2 is empty. 
        # This keeps the order of newly pushed nodes in stack1 and old nodes in stack2
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())

    def push(self, element):
        self.stack1.append(element)

    def top(self):
        # return the top element
        self.adjust()
        if len(self.stack2) != 0:
            return self.stack2[-1]

    def pop(self):
        # pop and return the top element
        self.adjust()
        return self.stack2.pop()

myQ = Queue()
myQ.push(1)
myQ.push(2)
myQ.push(3)
print myQ.top()
print myQ.pop()
myQ.push(4)
print myQ.pop()