"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        nodeAnswer =  Node()
        nodeAnswer.val = 1
        nodeAnswer.neighbors=[]

        #initialize the 1st node
        nodeAnswer.val = node.val

        #visited array shouldn't use visited
        #visited=set()

        #so i shouldn't use visited set for edges it creates the node and then goes through enighbors and then checks if its in visited at that point its too late because if the node 1: copy node 1 already exists then u just skip the for loop entirely right and just add the copy node 1 into the neighbor section of that nodex? and for visited set it only  checks edges it doesnt' check if the whoel node has already been traversed so itll be wasted effort with visited set. is that right? with the hashmap of node 1: copy of node 1 i will check before going into for loop before callign dfs if a copy already exists if it exists i wouldn't go into for loop thru its neighbor or call dfs on it to make a copy i will just attaach it to the node x neighbors and then move on?
        nodeVisited={}

        def dfs(node): 
            if node in nodeVisited:
                return nodeVisited[node]
            dfsAnswer =  Node()
            dfsAnswer.val = node.val
            nodeVisited[node] = dfsAnswer #should add it before because it will do 1-2 then when it goes through 2 it will run dfs(2) and go back to 1 because 1 was not aadded to node visited
            for neigh in node.neighbors: 
                dfsAnswer.neighbors.append(dfs(neigh))
            
            return dfsAnswer
        return dfs(node)

       # for neigh in node.neighbors:
            #run dfs get the new copy of neigh
           # dfsNewNode = dfs(neigh)
            # add to visited node(the vals only) to neigh
           # nodeVisited[node]=dfsNewNode
            # add the new node to nodeAnswer neighbor, shouldn't have to worry about duplicate because for looping through node's neighbors
           # nodeAnswer.neighbors.append(dfsNewNode)

        #return nodeAnswer
            
            #visited should keep track of 1,3 or 2,3 3,2 it has already added throughout all of it, so it doesn't repeat, that should be enough, if not in visited means could be added the new node and its neighbors

            # i go through each neighbor in node, and create a copy of the 1st node ? create a new copy of neigh, and send it to dfs and attach it to nodenew neighbor?  and within dfs i go through the neighbors of the 'node' parameter and does dfs on them as well but returns the 'node' parameter at the end and which when it goes back to the initial for loop i set the neigh node to whatever dfs returns?


        