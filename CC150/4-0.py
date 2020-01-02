#this is a testing file for chapter 4 containing simole and basic tree&graph algorithms
class node:
    def __init__(self,msg):
        self.msg=msg
        self.right=None
        self.left=None

#In order traverse
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.msg)
        inorder(root.right)
#print('hello,2020')
tree=node('ag')
left=node('left')
right=node('right')
tree.left=left
tree.right=right
inorder(tree)