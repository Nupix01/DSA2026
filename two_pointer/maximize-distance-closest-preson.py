#maximum distance to closed person
def maxdistance(seats:list[int])->int:
    prev=-1
    distance=0
    for index in range(len(seat)):
        if seats[index]==1:
            if prev== -1:
                distance=index
            else:
                distance=max(distance,(index-prev)//2)
            prev=index
    distance=max(distance,len(seats)-1-prev)
    