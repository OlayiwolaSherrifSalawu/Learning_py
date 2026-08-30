class Fib():
    def __init__(self, n):
        self.__n= n
        self.__i= 0
        self.__p1= self.__p2=1
    def __iter__(self):
        return self
    def __next__(self):
        self.__i+=1
        if self.__i>self.__n:
            raise StopIteration
        if self.__i in [1,2]:
            return 1
        ret = self.__p1+ self.__p2
        self.__p1, self.__p2= self.__p2, ret
        return ret




def fun(n):
    for i in range(n):
        yield i
 
list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)

list_2 = [10 ** ex for ex in range(6)]

print(list_1)
print(list_2)