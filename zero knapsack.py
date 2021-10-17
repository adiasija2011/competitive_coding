class Item:
    def __init__(self,weight,profit):
        self.weight=weight
        self.profit=profit


def zeroknapsack(items,max_capacity,currentIndex):
    if max_capacity<=0 or currentIndex<0 or currentIndex>=len(items):
        return 0
    elif(items[currentIndex].weight<=max_capacity):
        p1=items[currentIndex].profit+zeroknapsack(items,max_capacity-items[currentIndex].weight,currentIndex+1)
        p2=zeroknapsack(items,max_capacity,currentIndex+1)
        return max(p1,p2)

    else:
        return 0

A=Item(3,31)
B=Item(1,26)
C=Item(2,17)
D=Item(5,72)
items=[A,B,C,D]
print(zeroknapsack(items,7,0))