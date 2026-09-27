import os
from pathlib import Path
# os.mkdir("hello") # the relative path

lists=os.listdir()
newList= [ f for f in lists if Path(f).is_dir()]
def path(path, dir):
    lists=os.listdir(path)
    newList=   [f for f in lists if os.path.isdir(os.path.join(path, f))]
    


def recursiveNumber(n:int) ->int:
    if n ==1 :
        return n
    if n%2==0:
        return n/2
    return n * recursiveNumber(n-1)

print(path("extra","good"))