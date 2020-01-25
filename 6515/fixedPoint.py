#find the item value equals to index in log n time
#first let's implement the binary search algo
#done

def fixedPoint(arr):
    #index=list(range(len(arr)))
    i=0
    while len(arr)>1:
        j=len(arr)//2
        i+=j
        if arr[j]==i:
            return(True)
        elif arr[j]<i:
            arr=arr[j:]
        #else arr[i]>target:
        else:
            arr=arr[:j]
            i-=len(arr)
    if arr[0]==i:
        return(True)
    return(False)

a=[-12,-3,1,3,9]
print(fixedPoint(a))
