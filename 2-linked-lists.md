# Linked Lists

Linked lists are an ordered collection of objects. So what makes them different from normal lists? Linked lists differ from lists in the way that they store elements in memory. While lists use a contiguous memory block to store references to their data, linked lists store references as part of their own elements.
Each linked list consists of nodes which have a data field and a link to the next node in the linked list.
Specifically, the link will be a pointer to the location in memory that contains our next element.

![Simple linked List](https://www.mycplus.com/mycplus/wp-content/uploads/2017/09/linked-list.png)

In the linked list shown above, the first node is called the head. If you know where the head is, then you can traverse the entire linked list by following the pointers. The blue indicates the data that the node contains and the green is the pointer to the next node that gives the address of the next element.
We can implement the above object using a class Node having two fields namely data and next as follows.

``` python
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
```

Most linked lists maintain a bi-directional linking between nodes. Bi-directional means that each node will maintain a pointer to both the next node and previous node. The doubly-linked list shown below has both a head and a tail.

![Double linked list](https://files.realpython.com/media/Group_21.7139fd0c8abb.png)
``` python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

```

Just the same as the class Node before this time we have a pointer that points to the previous node.

## Creating a Double Linked List

``` python
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
``` 
## Inserting an element in a Linked List

We can insert an element in a linked list at the first position, in the last position on anywhere in between. 
To insert an element in a linked list at the beginning, we will first create a node and with the given value and assign its next reference to the first node i.e where the head is pointing. Then we point the head reference to the new node.

``` python
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
```

To insert an element in a linked list at the end, we just have to find the node where the next element refers to None i.e. the last node. Then we create a new node with the given data and point the next element of the last node to the newly created node. 

``` python
    
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
```

## 	Removing an element from a Linked List

We can delete a node either from the start or end or in between two nodes of a linked list. 
To delete the first node of a linked list, we will first check if the head of the linked list is also the tail
if so then we set the head and tail of our linked list to be none. Otherwise, we update the head to be the pointing to the second node. 


``` python

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
```

To delete the tail of our linked list we first check if our tail is also our head if so then we set our tail and head to be none. Otherwise we update the tail to be the previous node.

``` python

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
```

## Accessing elements from a Linked List

To traverse a linked list in python, we will start from the head, print the data and move to the next node until we reach None i.e. end of the linked list. The following traverse() method implements the program to traverse a linked list in python.

``` python

    def traverse(self):
        # Start at the beginning (the head)
        current = self.head

        # Loop until we have reached the end (None)
        while current is not None:

            # Do something with the current node
            print(current.data)

            # Follow the pointer to the next node
            current = current.next

```
## Inserting an element at a specific position

To insert an element at any other given position, we can count the nodes till we reach that position and then we point the next element of the new node to the next node of the current node and the next reference of the current node to the new node

``` python
def insert_at_position(self,data,position):
        count = 1
        current = self.head
        while count < position-1 and current is not None:
            current = current.next
            count += 1
        new_node = DoubleLinkedList.Node(data)
        new_node.next=  current.next
        current.next = new_node
```

## Deleting an element from a specific position

To delete a node in between the linked list, at every node we will check if the position of next node is the node to be deleted, if yes, we will delete the next node and assign the next reference to the next node of the node being deleted.



## Big O Notation

Common Linked List Operation | Description | Performance
-------- | -------- | --------
insert_at_the_beginning(value)  | Adds "value" at the beginning | O(1) - Just need to adjust the pointers near the head.
insert_at_the_end(value) | Adds "value" at the end | O(1) - Just need to adjust the pointers near the tail.
delete_at_the_beginning() | deletes the first item (the head) | O(1) - Just need to adjust the pointers near the head.
delete_at_end() | deletes the last item (the tail) | O(1) - Just need to adjust the pointers near the head.
size() | Return the size of the linked list | O(1) - The size is maintained within the linked list class.
empty() | Returns true if the length of the linked list is zero. | O(1) - The comparison of the length with 0 is all that is needed.
insert_at_position | add value at a specific position | O(n) .
delete_at_position | deletes value at a specific position | O(n) 

