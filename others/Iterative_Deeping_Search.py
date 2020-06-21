#Python program to print DFS traversal from a given graph(commented off)
#Python program to print IDAstar traversal from a given graph
from collections import defaultdict
#This class represents a directed graph using adjacency list repr.
class Node:
    def __init__(self,color,x,y):
        self.color = color
        self.x,self.y = x,y
class move_node:
    def __init__(self,action,x,y):
        self.action = action
        self.x,self.y = x,y
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)

    #function to add an edge to graph
    def add_edge(self,u,v):
        self.graph[u].append(v)

    '''
    def DLS(self,src,target,max_depth):
        if src==target: return True
        if max_depth<=0: return False
        for i in self.graph[src]:
            if(self.DLS(i,target,max_depth-1)):
                return True
        return False

    def IDDFS(self,src,target,max_depth):
        for i in range(max_depth):
            if (self.DLS(i,target,i)):
                return True
        return False
    '''

    #IDA* search 
    #the heuristic function for A* searching
    #can and need to be modified according to context
    def heuristic(self,a,b):
        return(abs(a-b))
    '''
    cost(node,succ) is 1 per layer in a tree
    heuristic function is a problem
    '''
    def IDAstar(self,src,target):
        threshold = self.heuristic(src,target)
        path=[src]
        while True:
            distance =self.IDAstar_sub(path,target,0,threshold)
            if distance==float("inf"):
                return False
            elif distance==True:
                return(path)
            else:
                threshold = distance

    def IDAstar_sub(self,path,goal,g,threshold):
        start=path[-1]
        estimate = g+self.heuristic(start,goal)
        if estimate > threshold:
            return estimate
        if start == goal: return True
        min=float("inf")
        for i in self.graph[start]:
            new_path=path.copy()
            new_path.append(i)
            t=self.IDAstar_sub(new_path,goal,g+1,threshold)
            if(t):return t
            if t<min:min=t
            path.pop()
        return min
'''
g=Graph(7)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,5)
g.add_edge(2,6)

target=6;max_depth=3;src=0

if g.IDAstar(src,target)!=False:
    print("The target is reachable within the max depth")
else:
    print("The target is not reachable within the max depth")
'''