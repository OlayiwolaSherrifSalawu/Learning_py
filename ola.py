# bubble sort 

hit= []
while swaped:
    swaped= False
    for i in range(len(hit)-1):
        if hit[i]>hit[i+1]:
            swaped=True
            hit[i], hit[i+1]=hit[i+1],hit[i]