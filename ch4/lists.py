'''
    Module for storing pointer based list structures
'''
from node import Node

class SinglyLinkedList:
    '''
        Singly linked list implementation 

        Properties:
            :head: the front of the linked list
            :tail: the back of the linked list
            :size: the overall size (total nodes) of the linked list
    '''

    def __init__(self, data=None):
        self.head = None
        self.tail = None
        self.size = 0

        if data:
            for item in data:
                self.append(item)

    def append(self, data):
        '''
            Append an item into the singly linked list

            Arguments:
                :data: the data to be stored into the node
        '''
        node = Node(data)

        # Check to see if there is at least one node within the list
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def delete(self, data):
        '''
            Delete an item from the singly linked list

            Arguments:
                :data: the data to be removed from the linked list (if it exists)

            Returns:
                None if a node containing the data we're looking for isn't found
                and the data we've successfully deleted if found
        '''

        #Grab the current and previous nodes (both start at the head)
        current = self.head
        prev = self.head

        # Keep checking until you can't check anymore!
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next

                self.size -= 1
                return data

            #Move the pointers one node up
            prev = current
            current = current.next

        return None

    def search(self, data):
        '''
            Search the singly linked list to see if it contains the data we're looking for

            Arguments:
                :data: the data we're trying to find within our linked list

            Returns:
                True if found, false otherwise
        '''
        for node in self.iter():
            if data == node:
                return True
        return False

    def clear(self):
        '''
            clear the entire list 
        '''
        self.head = None
        self.tail = None

    def iter(self):
        '''
            Return all nodes via a generator

            Returns the data of a node for as many nodes that there are
        '''
        current = self.head

        # Create a generator to iterate over the list
        while current:
            data = current.data
            current = current.next
            yield data

def test_single_linked_list():
    '''
        Testing out the singly linked list
    '''
    single_ll = SinglyLinkedList()

    # Demonstrate appending two items into the list
    single_ll.append('hello')
    single_ll.append('yeet')

    # Demonstrate iterating over the items of the list
    for data in single_ll.iter():
        print(data)

def main():
    '''
        Execute all test functions
    '''
    test_single_linked_list()

if __name__ == '__main__':
    main()
