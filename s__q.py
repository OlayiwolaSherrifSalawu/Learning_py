class Algorithm:
    
    def __init__(self):
        stack=[]    
        self.stack= stack
  
        

class Queue(Algorithm):
    def add(self,val):
        self.stack.append(val)
        return self.stack
    def pop(self):
        # ensure that i dont try to pop an empty list 
        if len(self.stack)== 0:
            return f"the list is empty cant pop an empty list"
        self.stack.pop(0)
        return self.stack