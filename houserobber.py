def houseRobber(houses,currenthouse):
    if currenthouse>=len(houses):
        return 0
    else:
        steal=houses[currenthouse]+houseRobber(houses,currenthouse+2)
        skip=houseRobber(houses,currenthouse+1)
        return max(skip,steal)
houses=[6,7,1,30,8,2,4]
print(houseRobber(houses,0))