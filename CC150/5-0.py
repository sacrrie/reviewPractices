#bit manipulation practice file
#a simple bit manipulation function
import bitstring
print(int('111001', 2))

def repeated_arithmetic_right_shift(base,time):
    answer=base
    for i in range(time):
        answer=base>>1
    return(answer)
a=repeated_arithmetic_right_shift(-75,1)
print(a)

def repeated_logical_right_shift(base,time):
    answer=bitstring.BitArray(int=base,length=32)
    print(answer.int)
    for i in range(time):
        answer=answer >> 1
    return(answer)
b=repeated_logical_right_shift(5,1)
print(b.int)