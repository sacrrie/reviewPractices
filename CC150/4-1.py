#Given a DIRECTED graph, design an algorithm that shows if there are any links between two nodes
def BFS(node):
    #import the code from 4-0
    #return all the nodes it can reach in a set
    #idea for improvement: stop once when reaches target
    pass

def pathfinder(node1,node2):
    set1=BFS(node1)
    if node2 in set1:
        print("Node2 can be reached from node1")

    set2=BFS(node2)
    if node1 in set2:
        print("Node1 can be reached from node2")
