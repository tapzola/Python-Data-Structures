


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

  def traverse_inorder(self, root):
    if root is not None:
      # recursively call the inorder method by moving to the next node on the left side 
      self.traverse_inorder(root.left)
      print(root.data)
      # Do the same thing on the right by recursively call the inorder method by moving to the next node on the right side 
      self.traverse_inorder(root.right)

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

  def __contains__(self, data):
        """ 
        Checks if data is in the BST.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_bst:
            ("5 is in the bst")

        """
        return self._contains(data, root)  # Start at the root

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
print("\n=========== PROBLEM 1 TESTS ===========")
tree = Tree()
root = tree.createNode(5)
print(root.data)
tree.insert(root, 2)
tree.insert(root, 10)
tree.insert(root, 7)
tree.insert(root, 15)
tree.insert(root, 12)
tree.insert(root, 20)
tree.insert(root, 30)
tree.insert(root, 6)
tree.insert(root, 8)

tree.traverse_inorder(root)

print(tree._get_height(root)) # 3
tree.insert(root, 9)
print(tree._get_height(root)) # 3
tree.insert(root, 40)
print(tree._get_height(root)) # 4
    
    
        
print("\n=========== PROBLEM 2 TESTS ===========")
print(3 in tree) # False
print(2 in tree) # True
print(7 in tree) # True
print(6 in tree) # True
print(9 in tree) # False
       
    


