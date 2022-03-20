# Trees

A Tree is a data structure in which data items are conneted using reference in a hierachal manner. 
Each tree consists of a root node in which we can access each element of the tree. Starting from the root node 
each node consists of zero or more nodes connected to it as its children.

## Parts of a tree
1. Root Node:
Root node is the topmost node of a tree. It is always the first node created while creating the tree
and we can access each element of the tree starting from the root node.
2. Parent Node:
The parent of any node is the node which references the current node. In order for you to access the current node
you would have to go through the parent node first.
3. Child Node:
Child nodes of a parent node are the nodes at which the parent node is pointing using the references.
4. Leaf node: 
These are those nodes in the tree which have no children.

We will discuss two types of trees namely: Binary tress and Binary Search Trees

## Binary Trees
A binary tree is a tree that starts from the root node and each node consists of no more than two nodes connected to it as
its children.

## Binary Search Trees
Binary search tree is a data structure that quickly allows us to maintain a sorted list of numbers.
The properties that separate a binary search tree from a regular binary tree is

* All nodes of left subtree are less than the root node
* All nodes of right subtree are more than the root node
* Both subtrees of each node are also BSTs i.e. they have the above two properties

![Binary Search Tree](http://www.csharpstar.com/wp-content/uploads/2015/11/BinarySearchTree_implementation_Csharp.jpg)

### Implementation of a Basic Binary Search Tree Data Structure.

Since a node is a container for data and holds references to other nodes. Being a binary tree node, these references are to the left and the right children. Initially the left and right children are none. Data refers to data that will be contained in the node to establish a parent to children relationships accoriding to the rules of Binary Search Trees.

Initialize a node
``` python


class Node:
  # create a node which has empty left and right childs
  def __init__(self, value):
      self.data = value
      self.left = None
      self.right = None


class Tree:
  def createNode(self, data):
    return Node(data)
  
  def insert(self, node, data):
    if node is None:
      # check if there is a node in the tree or if it is empty
      return self.createNode(data) # if there is no node then you create it
    if data == node.data:
      return   # no duplicates allowed
    if data < node.data:
      # if your number which is data is less than the number in your node
      # add data in left subtree
      node.left = self.insert(node.left, data)  # a tree is a recursive data structure, so you call the insert method recursively
    else:
      # if the value is greater than add data to the right subtree
      node.right = self.insert(node.right, data)
    return node
```

### Traversing a Binary Search Tree

In inorder traversal, you visit the left sub-tree, the parent node, and finally the right sub-tree. There are other orders of traversing the BST such as pre-order, post-order traversal. We will only discuss the in order traversal only. 
  ``` python
  def traverse_inorder(self, root):
    if root is not None:
      # recursively call the inorder method by moving to the next node on the left side 
      self.traverse_inorder(root.left)
      print(root.data)
      # Do the same thing on the right by recursively call the inorder method by moving to the next node on the right side 
      self.traverse_inorder(root.right)

  ```
### Finding Height of the tree

The implementation is similar to the inorder traversal in the sense that we visit the all the nodes in the tree. The difference is that with getting the height, we count the nodes on the left side and right side and then compare which side is greater than the other. The side with the highest height contains the maximum height of the tree.

![Finding height of a Binary Search tree](http://csharpexamples.com/wp-content/uploads/2019/05/binary-tree-2.png)

``` python
  def _get_height(self, node):
        count = 0
        """
        Determine the height of the BST.  The height of a sub-tree 
        (represented by 'node') is 1 plus the height of either the 
        left sub-tree or the right sub-tree (whichever one is bigger).

        """
        if node is None:
          # return o if the tree is empty
            return count
        else:
          # call the left and right side recursively
            left = self._get_height(node.left)
            right = self._get_height(node.right)

        if left > right:
          #Compare left sub tree and right sub tree
            left += 1
            return left
        else:
            right += 1
            return right

   


``` 
Big O Notation

Common BST Operation | Description | Performance
-------- | -------- | --------
insert(value) | Insert a value into the tree. | O(log n) - Recursively search the subtrees to find the next available spot
remove(value)	 | Remove a value from the tree. | 	O(log n) - Recursively search the subtrees to find the value and then remove it. This will require some cleanup of the adjacent nodes.
traverse_forward | Visit all objects from smallest to largest. | O(n) - Recursively traverse the left subtree and then the right subtree.
height(node)| Determine the height of a node. If the height of the tree is needed, the root node is provided.  | 	O(n) - Recursively find the height of the left and right subtrees and then return the maximum height (plus one to account for the root).
size()| Return the size of the BST. |  The size is maintained within the BST class.
empty()| Returns true if the root node is empty. This can also be done by checking the size for 0. |  O(1) - The comparison of the root node or the size.
contains(value) | Determine if a value is in the tree.	 |  O(log n) - Recursively search the subtrees to find the value.


[Problem to Solve](https://github.com/tapzola/cse212-final-project/blob/main/tutorial.py)

 After you have tackled the problem you can view this solution below and compare with your own.
 [Solution](https://github.com/tapzola/cse212-final-project/blob/main/tress_tutorial.py)

     


    
    
        
        
    


