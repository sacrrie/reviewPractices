# This is the 1st practice problem of the 2nd chapter.
# Write Code to remove duplicates from an unsorted linked list.


# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?
# 指针操作非常绕，多加小心，注意Python里object的互相拷贝是不带reference的指针拷贝

class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class sLinkedList:
    def __init__(self):
        self.head=None

    def print(self):
        n=self.head
        while(n is not None):
            print(n.data)
            n=n.next

    def append(self,n):
        new=Node(n)
        if self.head is None:
            self.head=new
        else:
            pointer=self.head
            while(pointer.next is not None):
                pointer=pointer.next
            pointer.next=new

    def remove_duplicates(self,buffer=False):
        n=self.head
        if n is None:
            print('Empty List')
            return
        if buffer:
            temp=[]
            previous=Node()
            while(n is not None):
                if n.data in temp:
                    previous.next=n.next
                else:
                    temp.append(n.data)
                    previous=n #这里拷贝的是静态指针，下一循环n改变但是previous不改变
                n=n.next
        else:
            while(n is not None):
                current=n
                while(current.next is not None):
                    if current.next.data == current.data:
                        current.next=current.next.next
                    else:
                        current=current.next
                n=n.next
testSL=sLinkedList()
test=[1,1,1,2,2,3,4,3]
for i in test:
    testSL.append(i)

testSL.print()
testSL.remove_duplicates(buffer=False)
print('---------------------------')
testSL.print()