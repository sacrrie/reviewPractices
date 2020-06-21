#IDA* search
class Node:
    def __init__(self,N,content):
        self.N = N
        self.look=content
        self.position=self.update_position()
        self.action=None
    def update_position(self):
        res={}
        for i in range(len(self.look)):
            for j in range(len(self.look[i])):
                res[self.look[i][j]]=(i,j)
        return res
        
def heuristic(node,target):
    res=0
    for i in node.position.keys():
        xs,ys = node.position[i]
        xt,yt = target.position[i]
        res+=abs(xs-xt)
        res+=abs(ys-yt)
    return(res/node.N)

def is_goal(node,target):
    return(node.look==target.look)

def successors(node,target):
    res=[]
    hs=[]
    content=node.look
    N=node.N
    for x in [1,2]:
        for y in [1,node.N+1]:
            for z in [1,2]:
                action=(x,y,z)
                if x==1:
                    content[y-1]=shift(content[y-1],z)
                else:
                    content=yshift(content,y,z)
                n=Node(N,content)
                n.action=action
                res.append(n)
                hs.append(heuristic(n,target))
    return([x for _,x in sorted(zip(hs,res))])

def shift(arr,inver):
    if inver == 1:
        temp=(arr*2)[1:len(arr)+1]
    else:
        temp=(arr*2)[-1-len(arr):-1]
    return(temp)

def yshift(content,y,z):
    temp=content.copy()
    arr=[]
    #extract the array
    for i in content:
        arr.append(i[y-1])
    arr=shift(arr,z)
    #put them back 
    for i in range(len(content)):
        temp[i][y-1]=arr[i]
    return(temp)

#IDA* search 
def IDAstar(root,target):
    bound=heuristic(root,target)
    path=[root]
    while True:
        t =IDAstar_sub(path,target,0,bound)
        if t==True:
            return(path)
        if t==float("inf"):
            return False
        bound = t

def IDAstar_sub(path,goal,g,bound):
    node=path[-1]
    f = g+heuristic(node,goal)
    if f > bound:
        return f
    if is_goal(node,goal): return True
    min=float("inf")
    for i in successors(node,goal):
        if i not in path:
            path.append(i)
        t=IDAstar_sub(path,goal,g+1,bound)
        if(t):return t
        if t<min:min=t
        path.pop()
    return min

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        t=l.rstrip('\r\n')
        t=t.split()
        t=[int(x) for x in t]
        lines.append(t)
    N=lines[0][0]
    root_content=lines[1:N+1]
    target_content=lines[N+1:]
    root=Node(N,root_content)
    target=Node(N,target_content)
    answer=IDAstar(root,target)
    if answer is not False:
        print("yes")
        answer=answer[1:]
        print(len(answer))
        for i in answer:
            x,y,z=i.action
            print("{0} {1} {2}".format(x,y,z))
