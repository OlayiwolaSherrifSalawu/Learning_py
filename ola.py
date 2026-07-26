blocks = int(input("Enter the number of blocks: "))

height= 0
count = 0
while count != blocks and count < blocks:
    if (height+1)+count > blocks:
        break
    height+=1
    count+=height

print("The height of the pyramid:", height)
