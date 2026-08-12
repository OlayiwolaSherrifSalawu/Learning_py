class Algorithm:
    def __init__(self,stack:list, val):
        self.stack= stack
        self.val= val
        

class Queue(Algorithm):
    def add(self):
        self.stack.append(self.val)
    