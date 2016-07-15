from .interface import AbstractLinkedList
from .node import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """


    def __init__(self, elements=None):
        self.start = None
        self.end = None
    
        if elements:
            for elem in elements:
                self.append(elem)
                    
    def __str__(self):
        pass

    def __len__(self):
        return self.count()

    def __iter__(self):
        return self

    def __getitem__(self, index):
        # return self.list[index]
        pass

    def __add__(self, other):
        if other.start:
            aux = other.start
            while aux:
                self.append(aux.elem)
                aux = aux.next

    def __iadd__(self, other):
        pass

    def __eq__(self, other):
        # If both None, return True
        if self.start == None and other.start == None:
            return True
        
        # If only one is None, return False
        if self.start == None or other.start == None:
            return False
        
        # Check if unequal counts
        if self.count() != other.count():
            return False
        
        # To be equal, they must have same count and same elem
        # in each place
        # Assume True and test both criteria
        equal = True
            
        # Assign dummies for both start nodes
        aux_s = self.start
        aux_o = other.start
            
        while aux_s != None and aux_o != None:
            if aux_s != aux_o:
                equal = False
                
        return equal

    def append(self, elem):
        aux = Node(elem)
        if self.start == None:
            self.start = aux
            self.end = self.start
        
        self.end.next = aux
        self.end = aux
        #print(aux.next)

    def count(self):
        # Start at 
        count = 0
        if self.start != None:
            aux = self.start
            while aux != None:
                count += 1
                aux = aux.next
        return count
        

    def pop(self, index=None):
        
        if index >= self.count() or index < 0:
            raise IndexError("index greater than self.count()")
            
        if self.start == None:
            raise IndexError("LinkedList is empty")
        
        if index == None:
            index = self.count()


        # If it gets here, iterate to index
        aux = self.start
        for i in range(0, index):
            aux = aux.next
        
        elem = aux.elem
        aux = aux.next
        
        return elem
