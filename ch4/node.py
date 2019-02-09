'''
    Demonstrating the use case and implementation of nodes
'''
class Node:
    '''
        Node class

        Arguments:
            :data: the data to be stored within the node
    '''
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        '''
            Return the string representation of the node the data
            is storing
        '''
        return str(self.data)

def create_singly_linked_list():
    '''
        Create a singly linked list 
    '''
    n1 = Node('hey')
    n2 = Node('heyyy')
    n3 = Node('Hoi')

    n1.next = n2
    n2.next = n3

if __name__ == '__main__':
    create_singly_linked_list()
