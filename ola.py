# collaaz hypothesis
c0 = int(input("enter a number: "))
count= 0
while c0 !=1:
    if c0%2==0:
        c0//=2
    else:
        c0=3*c0 + 1
    count+=1

print(count)