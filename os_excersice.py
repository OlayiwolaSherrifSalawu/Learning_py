import os
from pathlib import Path
# os.mkdir("hello") # the relative path

lists=os.listdir()
newList= [ f for f in lists if Path(f).is_dir()]
def path (path, sense):
    lists=os.listdir(path)
    newList= [ f for f in lists if Path(f).is_dir()]
    