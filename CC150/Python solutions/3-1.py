# Implementing 3 stacks with 1 array.

class arraystack:
    # 3 Stacks in 1 Array

    def __init__(self):
        self.array=[None,None,]
        self.bottom1=1
        self.bottom2=0

    def isEmpty1(self):
        if self.array[-1] is None:
            return(True)
        else:
            return(False)

    def push1(self,x):
        self.array.append(x)

    def peek1(self):
        if not self.isEmpty1():
            print(self.array[-1])
        else:
            print('Empty Stack!')
    
    def pop1(self):
        if not self.isEmpty1():
            r=self.array[-1]
            self.array=self.array[:-1]
            return(r)
        else:
            print('Empty Stack!')

    def isEmpty2(self):
        if self.array[0] is None:
            return(True)
        else:
            return(False)

    def push2(self,x):
        self.array.insert(0,x)
        self.bottom1+=1
        self.bottom2+=1

    def peek2(self):
        if not self.isEmpty2():
            print(self.array[0])
        else:
            print('Empty Stack!')
    
    def pop2(self):
        if not self.isEmpty2():
            r=self.array[0]
            self.array=self.array[1:]
            self.bottom1-=1
            self.bottom2-=1
            return(r)
        else:
            print('Empty Stack!')

    def isEmpty3(self):
        if (self.bottom1-self.bottom2)==1:
            return(True)
        else:
            return(False)

    def push3(self,x):
        self.array.insert(self.bottom2+1,x)
        self.bottom1+=1

    def peek3(self):
        if not self.isEmpty3():
            print(self.array[self.bottom2+1])
        else:
            print('Empty Stack!')
    
    def pop3(self):
        if not self.isEmpty3():
            r=self.array[self.bottom2+1]
            self.array.pop(self.bottom2+1)
            self.bottom1-=1
            return(r)
        else:
            print('Empty Stack!')

a=arraystack()
print(a.isEmpty1())
a.pop1()
a.peek1()
a.push1(1)
a.push1(2)
a.push1(3)
a.peek1()
a.pop1()
a.pop1()
a.peek1()
print(a.array)
print('--------------')
print(a.isEmpty2())
a.pop2()
a.peek2()
a.push2(1)
a.push2(2)
a.push2(3)
a.peek2()
a.pop2()
a.pop2()
a.peek2()
print(a.array)
print('--------------')
print(a.isEmpty3())
a.pop3()
a.peek3()
a.push3(1)
a.push3(2)
a.push3(3)
a.peek3()
a.pop3()
a.pop3()
a.peek3()
print(a.array)