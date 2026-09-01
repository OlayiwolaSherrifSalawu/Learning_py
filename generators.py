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

the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))
 
# for v in the_list:
#     print(v, end=" ")
# print()
 
# for v in the_generator:
#     print(v, end=" ")
# print()

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))
 
print(the_list)
# for v in the_generator:
#     print(v, end=" ")
# print()