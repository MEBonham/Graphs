class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()
    
    def size(self):
        return len(self.stack)