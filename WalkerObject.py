from LinkedList import Node
from LinkedList import NodeList
from AdjacencyList import Edge
from AdjacencyList import Graph

import random

class RandomWalker():
    def __init__ (self, startVertex = 1):
        self.__currentVertex = startVertex
        self.__distWalked = 0
        self.__visited = [startVertex]
        
    def getCurrentVertex(self):
        return self.__currentVertex
    
    def setCurrentVertex(self, v):
        self.__currentVertex = v

    def getDistWalked(self):
        return self.__distWalked

    def randomChoice(self, graph):
        # FOR LATER: Find cleaner/more efficient way for checking
        # if path choice is valid. Perhaps find way to represent
        # vertices and remove possible options for random selection
        # once vertex has been visited to avoid generating
        # redundant invalid path possibilities
        
        ## randomChoice returns boolean:
        ##  --> TRUE if another move could be made (makes move)
        ##  --> FALSE if hit dead end or already visited all options
        
        numPathChoices = graph.getOutDegree(self.__currentVertex)
        tried = []

        if numPathChoices == 0: ## IF at dead end (outDeg == 0)
            return False        ## -> False
        else:
            nextVertex = self.__currentVertex
            while nextVertex in self.__visited:     ## while haven't found new vertex
                
                if len(tried) == numPathChoices:    ## IF all possible paths
                    return False                    ## have been tried -> False
                
                ## otherwise generate random path from vertex
                randPathChoice = random.randint(0, numPathChoices - 1)
                edges = graph.getEdges(self.__currentVertex)
                chosenPath = edges.getNodeAt(randPathChoice).getData()
                nextVertex = chosenPath.getEndVertex()
                
                ## IF have not yet, add vertex/destination of random path to "tried"
                if not nextVertex in tried:
                    tried.append(nextVertex)
                    
            ## ONLY IF path is valid:
            ## add to visited, change vertex, and add weight to distWalked
            self.__visited.append(nextVertex)
            self.__currentVertex = chosenPath.getEndVertex()
            self.__distWalked += chosenPath.getWeight()
            return True ## could take a step
        
    def reset(self, start):
        self.__currentVertex = start
        self.__distWalked = 0
        self.__visited = [start]
