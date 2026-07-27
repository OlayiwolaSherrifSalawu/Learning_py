# bubble sort 

hit= [3,1,2,4,5]
swaped = True
while swaped:
    swaped= False
    for i in range(len(hit)-1):
        if hit[i]>hit[i+1]:
            swaped=True
            hit[i], hit[i+1]=hit[i+1],hit[i]

print(hit)