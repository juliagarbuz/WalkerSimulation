'''
Created: April 17th, 2017
Author: Julia Garbuz
'''

from LinkedList import Node
from LinkedList import NodeList

from AdjacencyList import Edge
from AdjacencyList import Graph

from WalkerObject import RandomWalker

import random

def constructFromInput():
# FOR LATER: More robust input handling (catching invalid input)
# Also maybe find better way for user to enter edges (perhaps just 1, 2, 3)
# with one edge entered per prompt for input
    print("---------------------------------")
    print("------BUILD ADJACENCY LIST-------")
    print("---------------------------------\n")

    print(" Instructions ".center(52, '*'))
    print("(1) enter \'\' to stop entering vertices/edges")
    print("(2) enter edge destination and weight delim by \',\'")

    print("\n(i.e.) to generate an edge from vertex 1 to vertex 2")
    print("with a weight (length) of 3, enter:")
    print("\nVERTEX: 1")
    print("\tEDGE (to, weight): 2, 3")
    print("****************************************************\n")

    adjList = Graph()

    vertex = input("VERTEX: ")
    while vertex != "":
        vertex = int(vertex)
        edge = input("\tEDGE (to, weight): ")
        prevNode = None
        while edge != "":
            edge = edge.strip(" ").split(",")
            edge = Edge(vertex, int(edge[0]), int(edge[1]))
            adjList.addEdge(edge)
            edge = input("\tEDGE (to, weight): ")
        vertex = input("VERTEX: ")

    return adjList

def printAdjList(lis):
    print("\n---------------------------------")
    print("------PRINT ADJACENCY LIST-------")
    print("---------------------------------\n")
    print("(source) --- weight ---> (destination)")
    print(lis)

def readFromFile():
# FOR LATER: User enters text file from which to extract graph
    file = open("sampleGraph.txt", 'r')
    adjList = Graph()
    ## .txt file formatted like .csv (one edge per line)
    ## like so: "source, dest, weight\n"
    for line in file:
        edge = line.split(",")
        edge = Edge(int(edge[0]), int(edge[1]), int(edge[2]))
        adjList.addEdge(edge)
    return adjList

def oneWalk(walker, graph):
    steps = 0
    while walker.randomChoice(graph):
        steps = walker.getDistWalked()
    return steps

def simulation(graph, trials = 100):
    print("---------------------------------")
    print("----RANDOM WALKER SIMULATION-----")
    print("---------------------------------\n")
    print(" Explanation ".center(52, '*'))
    print("Walker initialized at a random vertex with an out\n" \
          "degree > 0. At each vertex a random \'path\' (edge\n" \
          "leaving the current vertex) is selected. The weight\n" \
          "of an edge represents the number of steps between\n" \
          "two vertices. Once a walker hits a dead end (vertex\n" \
          "with an out degree of 0) or has already visited all\n" \
          "possible vertices visitable from its current vertex,\n" \
          "the number of steps taken will be recorded. Min, max,\n" \
          "and avg number of steps are then calculated from 100\n" \
          "trials.")
    print("\nNOTE: Simulation does not run walker through")
    print("previously walked paths (no cycles and no self-")
    print("loops) even if they are included in graph.")
    print("*"*52, "\n")

    ## Generate list of valid start vertices
    validStarts = graph.getValidStartVertices()

    ## Initialize walker at randomly selected vertex
    walker = RandomWalker()

    maxSteps = -9999
    minSteps = 9999
    sumSteps = 0

    for i in range(0, trials):
        ## set walker to new start vertex and distWalked to 0
        rand_idx = random.randint(0, len(validStarts)-1)
        walker.reset(validStarts[rand_idx])

        ## run one simulation (oneWalk) and update values
        steps = oneWalk(walker, graph)
        if steps > maxSteps:
            maxSteps = steps
        elif steps < minSteps:
            minSteps = steps
        sumSteps += steps

    avgSteps = sumSteps/trials
    print("For a simulation of", trials, "trials:")
    print("\tMaximum number of steps:", maxSteps)
    print("\tMinimum number of steps:", minSteps)
    print("\tAverage number of steps:", avgSteps)

def main():
    print("WELCOME TO THE RANDOM WALK SIMULATION")
    print("\nWould you like to (1) build your own graph\n" + \
         "or (2) use the graph from the text file?")

    opt = 0
    while not (opt in [1, 2]):
        opt = int(input("--> "))

    if int(opt) == 1:
        aL = constructFromInput()
    else:
        aL = readFromFile()

    printAdjList(aL)
    simulation(aL)

main()
