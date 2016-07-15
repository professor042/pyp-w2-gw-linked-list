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
        aux = self.start
        count = 0
        while aux.next != None:
            count += 1
            
        return count

    def __iter__(self):
        # return iter(self.list)
        pass

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
        if not self.start and not other.start:
            return True
        
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
        if self.start:
            count = 1
            aux = self.start
            while aux.next != None:
                count += 1
                aux = aux.next
        return count
        

    def pop(self, index=None):
        #pop remo
        return self.list.pop(index)
