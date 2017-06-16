from LinkedList import Node
from LinkedList import NodeList

class Edge():

    ## Edge object represents a (directed) connection between two vertices
    ## Attributes include start vertex, destination vertex, and weight
    ## (weight is equivalent to length in this application)
    
    def __init__(self, initSource, initDest, initWeight):
        self.__startVertex = initSource
        self.__endVertex = initDest
        self.__weight = initWeight

    ## Getters/setters for all attributes

    def getStartVertex(self):
        return self.__startVertex
    def setStartVertex(self, newStart):
        self.__startVertex = newStart

    def getEndVertex(self):
        return self.__endVertex
    def setEndVertex(self, newEnd):
        self.__endVertex = newEnd

    def getWeight(self):
        return self.__weight
    def setWeight(self, newWeight):
        self.__weight = setWeight

    def __str__(self):
        return "\t(" + str(self.__startVertex) + ") --- " + \
               str(self.__weight) + " ---> (" + \
               str(self.__endVertex) + ")"

class Graph():

    ## Graph object is a Adjacency list representation of a directed graph
    ## In AdjList list, indices correlate to vertex number
    ## At each vertex a linked list stores all edges exiting that vertex
    
    def __init__(self, numVertices = 10):
        ## List sets all vertices initially to "None", then edges are added 
        ## to the corresponding index using setVertex or addEdge
        self.__AdjList = []
        for i in range(numVertices+1):  # Vertices will start from index 1
            self.__AdjList.append(None)    # (index 0 will be 'null header')

    def expandList(self, newMax):
        ## Since setter (add) method accesses vertex by index, if that
        ## index is not initialized to some value, you will get a index out of
        ## bounds error. ExpandList method initializes necesasry indices to None.
        currLen = len(self.__AdjList)
        for i in range(currLen, newMax+1):
            self.__AdjList.append(None)

    def getEdges(self, vertex):
        ## Returns linked list of edges at given vertex
        return self.__AdjList[vertex]
            
    def addEdge(self, edge):
        ## Single edge object passed in, vertex determined from attributes of
        ## edge. List expanded if needed. Edge added as node to linked list
        vertex = edge.getStartVertex()
        if vertex + 1 > len(self.__AdjList):
            self.expandList(vertex)
            
        if self.__AdjList[vertex] == None:
            ## If no nodes have yet been added to vertex, edge set as head
            ## of linked list at vertex
            self.__AdjList[vertex] = NodeList(Node(edge))
        else:
            self.__AdjList[vertex].add(Node(edge))
            
    def getOutDegree(self, vertex):
        ## out degree is number of edges leaving given vertex
        if self.__AdjList[vertex] == None:
            return 0
        else:
            return self.__AdjList[vertex].getLength()

    def getValidStartVertices(self):
        ## returns list of all vertices that have an out degree > 0
        validVertices = []
        for i in range(1, len(self.__AdjList)):
            if self.getOutDegree(i) > 0:
                validVertices.append(i)
        return validVertices

    def __str__(self):
        s = ""
        for i in range(1,len(self.__AdjList)):
            if self.__AdjList[i] != None:
                s += "\n[ VERTEX " + str(i) + " ]" + "\n" + str(self.__AdjList[i]) 
        return s        
        
