#this is a testing file for chapter 4 containing simole and basic tree&graph algorithms
class binary_tree_node:
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
#Pre order traverse
def preorder(root):
    if root is not None:
        print(root.msg)
        inorder(root.left)
        inorder(root.right)
#post order traverse
def postorder(root):
    if root is not None:
        inorder(root.left)
        inorder(root.right)
        print(root.msg)
#reverse order traverse
def reverseorder(root):
    if root is not None:
        inorder(root.right)
        print(root.msg)
        inorder(root.left)
tree=binary_tree_node('root')
left=binary_tree_node('left')
right=binary_tree_node('right')
tree.left=left
tree.right=right
inorder(tree)
preorder(tree)
postorder(tree)
reverseorder(tree)

#undirected graph set up
class graph:
    def __init__(self):
        self.list=[]

class graph_node:
    def __init__(self,msg):
        self.msg=msg
        self.neighbor=[]

#DFS
#todo: refactir the DFS below using a qieue or
#other python method that is compatible with simple
#implementation above
def DFS(root):
    if roit is not None:
        visit(root)
        root.visited=true
        for i in root.neighbor:
            if not i.visited:
                DFS(i)
                
#Depth first search, need further test
def BFS(root):
    if root is not None:
        q=queue()
        visit(root)
        root.visited=true
        for i in root.neighbor:
            if not i.visited:
                q.append(i)
        while len(q) != 0 :
            j=q.pop()
            if j is not None:
                visit(j)
            for i in root.neighbor:
                if not i.visited:
                    q.append(i)
        
