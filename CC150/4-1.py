#Given a DIRECTED graph, design an algorithm that shows if there are any links between two nodes
def BFS(node):
    #import the code from 4-0
    #return all the nodes it can reach in a set
    #idea for improvement: stop once when reaches target
    pass
    return([None])

def pathfinder(node1,node2):
    set1=BFS(node1)
    if node2 in set1:
        print("Node2 can be reached from node1")

    set2=BFS(node2)
    if node1 in set2:
        print("Node1 can be reached from node2")


#the above is basically right, simple graph travelsal would do the trick,
#DFS BFS all would work, textbook solution is given below:
import queue
states=enumerate('Unvisited', 'Visited', 'Visiting')
def search(graph,start,end):
    if start == end:
        return True
    q=queue.Queue()
    for n in graph:
        n.visited='Unvisited'
    q.put(start)
    while not q.empty():
        u=q.get()
        if u is not None:
            for i in u.neighbor:
                if i.state=='Unvisited':
                    if i==end:
                        return(True)
                    else:
                        i.state='Visited'
                        q.put(i)
        u.state='Visited'
    return(False)

#It is worth discussing with interviewer the tradeoffs between BFS and DFS.
#DFS is easier to implement but BFS helps to find shortest path. DFS would go
# very deeply before checking other immediate neighbors thus wasting efforts.