def binary_search(numbers,target):
    l,r =0,len(numbers)
    while l <r:
        m=l+(r-l)//2
        if numbers[m]==target: return m
        if numbers[m]<target:
            l=m+1
        else:
            r=m
    return -1

def lower_bound(numbers,target):
    l,r =0,len(numbers)
    while l <r:
        m=l+(r-l)//2
        if numbers[m]<target:
            l=m+1
        else:
            r=m
    return r

def last_small(numbers,target):
    '''
    return the last number smaller than target
    '''
    l,r =0,len(numbers)
    while l <r:
        m=l+(r-l)//2
        if numbers[m]<target:
            l=m+1
        else:
            r=m
    return r-1