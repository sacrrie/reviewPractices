#Is Unique
#Implementing an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

#1. Naive set version
def is_unique(string):
    s=set(string)
    if len(s)!=len(string):
        print('Not Unique!')
    else:
        print('Unique!')

is_unique('hello')
is_unique('random')

#2. Can only use string structure.

def is_unique_string(string):
    l=len(string)
    for i in range(l-1):
        for j in range(i+1,l):
            if string[i]==string[j]:
                print('Not Unique!')
                return(0)
    print('Unique')
    return(0)

is_unique_string('hello')
is_unique_string('random')