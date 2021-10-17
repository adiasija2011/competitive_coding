import math
def binarysort(A,v):
    last=len(A)-1
    mini=0
    mid=round(last/2)
    #print(mid)
    for i in range(0,round(math.log2(last)+1)):
        if(A[mid]==v):
            return mid
        elif(A[mid]<v):
            mini=mid
            mid=round((last+mid)/2)
        else:
            last=mid
            mid=round((mini+mid)/2)
    return mini
    
A=[1,3,4,7,8]
print(binarysort(A,9))




        
