'''
    Module for storing pointer based list structures
'''
from node import Node

class SinglyLinkedList:
    '''
        Singly linked list implementation 
    '''

    def __init__(self, data=None):
        self.tail = None

        if data:
            for item in data:
                self.append(item)

    def append(self, data):
        '''
            Append an item into the singly linked list

            Arguments:
                :data: 
        '''
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.tail = node
