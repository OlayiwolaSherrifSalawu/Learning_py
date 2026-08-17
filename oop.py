class Stack:
    def __init__(self):
        self.stack= []
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        val= self.stack[-1]
        self.stack= self.stack[:-1]
        del self.stack[-1]
        return val
        
        

hav= Stack()

class Queue:
    def __init__(self):
        self.__queue=[]
    def put(self,val):
        self.__queue.append(val)
    def pop(self):
        val = self.__queue[0]
        del self.__queue[0]
        return val
    def get(self):
        val= self.__queue[0]
        return val

class AddingQueu(Queue):
    def __init__(self):
        super().__init__()