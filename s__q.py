class Algorithm:
    def __init__(self,stack:list, val):
        self.stack= stack
        self.val= val
        

class Queue(Algorithm):
    def add(self):
        self.stack.append(self.val)
    def pop(self):
        # ensure that i dont try to pop an empty list 
        if len(self.stack)== 0:
            return f"the list is empty cant pop an empty list"
        self.stack.pop(0)