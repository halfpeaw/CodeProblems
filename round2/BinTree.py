#This weird hack is so addNode can rely on none without mucking with default variable
UseDefault = object()

class BST:
   root = None
   def __init__(self, val):
      self.root = Node(val = val) 
      self.root.printVal()
   
   #Technically we could do this if currentNode = none then it is a new node and be done
   #by checking if the children are none first then we are able to track the parent
   #which i think will be useful later
   def addNode(self, val = 0, currentNode = UseDefault):
      if (currentNode == UseDefault):
         currentNode = self.root
      if (currentNode.val == val):
          print("Node {} already exists no duplicates allowed".format(val))
          return False
      elif (val < currentNode.val):
         if(currentNode.left == None):
            currentNode.left = Node(val = val, parent = currentNode)
            return True
         else:
            return self.addNode(val = val, currentNode = currentNode.left)
      # if its not equal and its not less than it must be greater than
      else:
         if(currentNode.right == None):
            currentNode.right = Node(val = val, parent = currentNode)
            return True
         else:
            return self.addNode(val = val, currentNode = currentNode.right)
            
   def traverseTree(self, result, node = UseDefault):
      if (node == UseDefault):
         node = self.root
      if (node == None):
         return
      self.traverseTree(result, node = node.left)
      result.append(node.val)
      self.traverseTree(result, node = node.right)
      return
      
      
   def printTree(self, indent = 0, node = UseDefault, branch = "C"):
      space = "  " * indent 
      if node == UseDefault:
         node = self.root
      if self.root == None:
         print("No tree to print its empty...")
         return
      print ("%s%s %d->"%(space,branch,node.val))
      if node.left != None:
         self.printTree(indent = indent+1, node = node.left, branch = "L")
      if node.right != None:
         self.printTree(indent = indent+1, node = node.right, branch = "R")
            
         

class Node:
   def __init__(self, val = 0, parent = None):
      self.parent = parent
      self.val = val
      self.left = None
      self.right = None
   def printVal(self):
      print("Node is: {}".format(self.val))
   
   

if __name__ == "__main__":
   print("Binary Tree")
   bt = BST(10)
   bt.addNode(5)
   bt.addNode(15)
   bt.addNode(12)
   bt.addNode(20)
   bt.addNode(0)
   bt.addNode(3)
   bt.addNode(-3)
   bt.addNode(8)
   result = []
   bt.traverseTree(result)
   print ("result: {}".format(result))
   bt.printTree()
   