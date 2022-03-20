


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

  def __contains__(self, data):
        """ 
        Checks if data is in the BST.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_bst:
            ("5 is in the bst")

        """
        return self._contains(data, root)  # Start at the root
  ###################
    # Solution #
  ###################
  def _contains(self, data, node):
        """
        This funciton will search for a node that contains
        'data'.  The current sub-tree being search is 
        represented by 'node'.  This function is intended
        to be called the first time by the __contains__ function.
        """
        if data == node.data:
            return True
        elif data < node.data:
            if node.left is None:
                return False
            else:
                return self._contains(data, node.left)
        
        else:
            if node.right is None:
                return False
            else:
                return self._contains(data, node.right)





#Testing code
tree = Tree()
root = tree.createNode(5)
# print(root.data)
tree.insert(root, 2)
tree.insert(root, 10)
tree.insert(root, 7)
tree.insert(root, 15)
tree.insert(root, 12)
tree.insert(root, 20)
tree.insert(root, 30)
tree.insert(root, 6)
tree.insert(root, 8)


    
    
        
print("\n=========== Solution TESTS ===========")
print(3 in tree) # False
print(2 in tree) # True
print(7 in tree) # True
print(6 in tree) # True
print(9 in tree) # False
       
    


