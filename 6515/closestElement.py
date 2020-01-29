import copy
#given 2 arrays of length n of distinct integers, A and B, find the closest element in B for each 
#element in A

def closestElement(A,B):
#Step 1, merge sort the array B
    mergeSort(B)
    ans=[]
#Step 2, loop through A, find closest element in B for every A using binary search
    for i in a:
        added=False
        b=copy.deepcopy(B)
        if i<=b[0]:
            ans.append(b[0])
            continue
        if i>=b[-1]:
            ans.append(b[-1])
            continue

        while len(b)>1:
            j=len(b)//2
            if b[j]==i:
                ans.append(b[j])
                added=True
                break
            elif b[j]<i:
                if j<len(b) and i<b[j+1]:
                    ans.append(closest(b[j],b[j+1],i))
                    added=True
                    break
                b=b[j:]
            else:
                if j>0 and i>b[j-1]:
                    ans.append(closest(b[j],b[j-1],i))
                    added=True
                    break
                b=b[:j]
        if not added:
            ans.append(b[0])
    return(ans)

def closest(v1,v2,target):
    if abs(v1-target)>abs(v2-target):
        return(v2)
    else:
        return(v1)

def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        mergeSort(left)
        mergeSort(right)
        i=j=k=0
        while i<len(left) and j < len(right):
            if left[i]>right[j]:
                arr[k]=right[j]
                #k+=1
                j+=1
            else:
                arr[k]=left[i]
                #k+=1
                i+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            k+=1
            i+=1
        while j<len(right):
            arr[k]=right[j]
            k+=1
            j+=1

a=[6,1,12]
b=[8,0,1]
c=closestElement(a,b)
print(c)