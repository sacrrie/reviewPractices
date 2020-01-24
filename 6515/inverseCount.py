def findReverse(arr):
    c=0
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        cl=findReverse(left)
        cr=findReverse(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]>right[j]:
                arr[k]=right[j]
                j+=1
                c+=1
            else:
                arr[k]=left[i]
                i+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
        c+=cr
        c+=cl
    return(c)
arr=[1,20,6,4,5]
r=findReverse(arr)
print(r)