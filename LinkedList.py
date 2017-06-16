'''
Created: April 17th, 2017
Author: Julia Garbuz
'''

class Node():

    ## Node is element of linked list structure defined below
    ## Two attributes are "data' of node and link to next node
    ## (data for current node in this application will be edge object)

    def __init__(self, nodeData, nextNode = None):
        self.__data = nodeData
        self.__next = nextNode

    ## Getters/setters for all attributes

    def getData(self):
        return self.__data
    def setData(self, newData):
        self.__data = newData
    def getNext(self):
        return self.__next
    def setNext(self, newNext):
        self.__next = newNext

    def __str__(self):
        return str(self.__data)

class NodeList():

    ## Node list structure built from Nodes
    ## Head attribute holds on to header Node of NodeList
    ## Tail attribute holds on to last not None-value Node

    def __init__(self, headerNode):
        self.__head = headerNode
        self.__tail = headerNode
        self.__length = 1
        ## If header node passed in already linked, while loop
        ## will correctly assign tail to last valued node
        while self.__tail.getNext() != None:
            self.__tail = self.__tail.getNext()
            self.__length += 1

    ## Getter methods (getCurrent returns tail node)

    def getHead(self):
        return self.__head
    def getCurrent(self):
        return self.__tail
    def getLength(self):
        return self.__length

    def add(self, node):
        ## Adds node to NodeList

        ## If currently only one element in list (head = tail)
        ## assignment done slightly differently
        if self.__tail == self.__head:
            self.__head.setNext(node)
            self.__tail = node

        else:
            self.__tail.setNext(node)
            self.__tail = self.__tail.getNext()

        self.__length += 1

    def getNodeAt(self, i):
        # FOR LATER: Implement exception for index out of bounds

        ## Node List is indexed from 0 (head has index 0)
        if (i+1) > self.__length:
            ## if out of bounds, returns tail
            ## (this shouldn't happen, but should be handled with exceptions)
            return self.__tail
        else:
            current = self.__head
            current_idx = 0
            while current_idx != i:
                current = current.getNext()
                current_idx += 1
            return current

    def __str__(self):
        s = str(self.__head)
        current = self.__head
        while current.getNext() != None:
            current = current.getNext()
            s += "\n" + str(current)
        s += "\n"
        return s
