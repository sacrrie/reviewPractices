#bit manipulation practice file
#a simple bit manipulation function
print(int('111001', 2))

def repeated_arithmetic_right_shift(base,time):
    answer=base
    for i in range(time):
        answer=base>>1
    return(answer)
a=repeated_arithmetic_right_shift(-75,1)
print(a)
