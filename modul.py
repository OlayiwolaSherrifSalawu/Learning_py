from math import e, exp, log,floor,ceil,trunc
from random import random, randint, randrange, choice,sample
from platform import platform, machine

# print(pow(e, 1) == exp(log(e)))
# print(pow(2, 2) == exp(2 * log(2)))
# print(log(e, e) == exp(0))
# print(pow(e,1))

x = 1.4
y = 2.6

# print(floor(x), floor(y))
# print(floor(-x), floor(-y))
# print(ceil(x), ceil(y))
# print(ceil(-x), ceil(-y))
# print(trunc(x), trunc(y))
# print(trunc(-x), trunc(-y))

# for i in range(5):
#     print(random())


# print(randrange(1), end=' ')
# print(randrange(0, 1), end=' ')
# print(randrange(0, 1, 1), end=' ')
# print(randint(0, 1))


# randint 



# for i in range(10):
#     print(randint(1, 10), end=',')


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# print(choice(my_list))
# print(sample(my_list, 5))
# print(sample(my_list, 10))
print(platform(aliased=False, terse=False))
print(platform(0, 1))
print(machine())
