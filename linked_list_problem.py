class DoubleLinkedList:
    """ Intialize the object Node inside the the Linked list class"""

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.previous = None
    
    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        self.tail = None

    def insert_at_the_beginning(self, value):
        """
        Insert a new node at the front of the
        linked list which is the head
        """
        # Create the new node
        new_node = DoubleLinkedList.Node(value)  
        
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.head will be
        # affected.
        else:
            new_node.next = self.head # Connect new node to the previous head
            self.head.prev = new_node # Connect the previous head to the new node
            self.head = new_node      # Update the head to point to the new node


    def insert_at_the_end(self, value):
        """
        Insert a new node at the back (i.e. the tail) of the 
        linked list.
        """
        #create the new node
        new_node = DoubleLinkedList.Node(value)
        # if the list is empty, then point head and tail to the new node
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        # if the list is not empty, then only self.tail
        # will be affected
        else:
            new_node.prev = self.tail  # connect the previous of your new_node to the tail
            self.tail.next = new_node  # make the next element of the tail to be the new_node
            self.tail = new_node      # make the tail to be the new_node

    def delete_at_the_beginning(self):
        """ 
        Remove the first node (i.e. the head) of the linked list.
        """
        # If the list has only one item in it, then set head and tail 
        # to None resulting in an empty list.  This condition will also
        # cover an empty list.  Its okay to set to None again.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the list has more than one item in it, then only self.head
        # will be affected.
        elif self.head is not None:
            self.head.next.prev = None  # Disconnect the second node from the first node
            self.head = self.head.next  # Update the head to point to the second node

    def delete_at_the_end(self):
        """
        Remove the last node (i.e. the tail) of the linked list.
        """
        # If the list has only one item in it, then set head and tail 
        # to None resulting in an empty list.  This condition will also
        # cover an empty list.  Its okay to set to None again.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the list has more than one item in it, then only self.tail
        # will be affected
        elif self.tail is not None:
            self.tail.prev.next = None
            self.tail = self.tail.prev



    def insert_at_position(self,data,position):
        count = 1
        current = self.head
        while count < position-1 and current is not None:
            current = current.next
            count += 1
        new_node = DoubleLinkedList.Node(data)
        new_node.next=  current.next
        current.next = new_node
 ###################
    # Start Problem #
 ###################


    def del_at_position(self,position):
        """To delete a node in between the linked list, at every node
           we will check if the position of next node is the node to be deleted,
           if yes, we will delete the next node and assign the next reference
           to the next node of the node being deleted
        """

        pass
        
  ###################
    # End Problem  #
 ###################   
    def __iter__(self):
        """
        Iterate foward through the Linked List
        """
        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list

    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output


ll = DoubleLinkedList()
ll.insert_at_the_end(1)
ll.insert_at_the_beginning(2)
ll.insert_at_the_beginning(2)
ll.insert_at_the_beginning(2)
ll.insert_at_the_beginning(3)
ll.insert_at_the_beginning(4)
ll.insert_at_the_beginning(5)
#print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 1]

ll.insert_at_the_end(0)
ll.insert_at_the_end(-1)
#print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 1, 0, -1]


ll.delete_at_the_end()
print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 1, 0]
ll.delete_at_the_end()
#print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 1]



ll.del_at_position(5)
#print(ll) # linkedlist[5, 4, 3, 2, 2, 1]


ll.insert_at_position(0, 5)
print(ll) # linkedlist[5, 4, 3, 2, 0, 2, 1]
