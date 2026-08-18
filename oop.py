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
        # super().__init__()
        self.__Queue= Queue(self)
        self.__sum=0
    def add(self,val):
        self.__sum+=val
        self.__Queue.put(val)
    def get_sum(self):
        return self.__sum
    def pop(self):
        val= self.__Queue.pop()
        self.__sum-= val
        return val


class ExampleClass:
    def __init__(self, val = 1):
        self.first = val
 
    def set_second(self, val):
        self.second = val
 
 
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
 
example_object_2.set_second(3)
 
example_object_3 = ExampleClass(4)
example_object_3.third = 5
example_object_1.fourth= 7
 
print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)