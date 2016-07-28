from collections import deque

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
   
   def findNode(self, val, currentNode = UseDefault):
      if(currentNode == UseDefault):
         currentNode = self.root
      if (currentNode == None):
         return None
      if (val < currentNode.val):
         return self.findNode(val, currentNode = currentNode.left)
      elif (currentNode.val == val):
         return currentNode
      elif (val > currentNode.val):
         return self.findNode(val, currentNode = currentNode.right)
   
   def deleteNode(self, val):
      nodeToDelete = self.findNode(val)
      if (nodeToDelete == None):
         print("nothing to delete")
         return False
      # No children then its a simple delete
      if (nodeToDelete.left == None and nodeToDelete.right == None):
         self.ActualDelete(nodeToDelete)
      # There's two children, go left, then as far right as you can.  That node becomes what we were deleting, and left of that node replaces it
      elif (nodeToDelete.left != None and nodeToDelete.right != None):
         print("thing")
         someNode = nodeToDelete.left
         while (someNode.right != None):
            someNode = someNode.right
         nodeToDelete.val = someNode.val
         if (someNode.left != None):
            someNode.parent.right = someNode.left
         else:
            self.ActualDelete(someNode)
      #If only one node to delete just replace deleted node with that node
      elif (nodeToDelete.left != None and nodeToDelete.right == None):
         self.ActualReplace(nodeToDelete, nodeToDelete.left)
      elif (nodeToDelete.right != None and nodeToDelete.left == None):
         self.ActualReplace(nodeToDelete, nodeToDelete.right)
      print ("Node was deleted")
      return True

   def ActualDelete(self, node):
      if node.parent == None:
         self.root = None
      else:
         if node.val > node.parent.val:
            node.parent.right = None
         else:
            node.parent.left = None
            
   def ActualReplace(self, nodeOld, nodeNew):
      if nodeOld.parent == None:
         self.root = nodeNew
      else:
         if nodeOld.val > nodeOld.parent.val:
            nodeOld.parent.right = nodeNew
         else:
            nodeOld.parent.left = nodeNew
   
   def traverseTree(self, result, node = UseDefault):
      if (node == UseDefault):
         node = self.root
      if (node == None):
         return
      self.traverseTree(result, node = node.left)
      result.append(node.val)
      self.traverseTree(result, node = node.right)
      return
   
   def DepthFirstTraversal(self, myNode):
      marked = []
      result = []
      if (myNode == None):
         print ("hey I expected a real node")
         return result
      def RecDepthFirst(myNode):
         nonlocal marked
         nonlocal result
         if (myNode == None):
            return
         if (myNode.val not in marked):
            marked.append(myNode.val)
            result.append(myNode.val)
            # If this was a none BST we could have N branches and we would just go from 0..N
            RecDepthFirst(myNode.left)
            RecDepthFirst(myNode.right)
      RecDepthFirst(myNode)
      return result
      
   def BreadthFirstTraversal(self, myNode):
      marked = []
      result = []
      if (myNode == None):
         print("Hey I expected a real node")
         return result
      def RecBreadth(nodeQueue):
         newQueue = deque()
         while(len(nodeQueue) > 0):
            myNode = nodeQueue.popleft()
            if myNode.val not in marked:
               result.append(myNode.val)
               marked.append(myNode.val)
               #If this was a non-bst we would just loop through all children nodes
               if (myNode.left != None):
                  newQueue.append(myNode.left)
               if (myNode.right != None):
                  newQueue.append(myNode.right)
         if (len(newQueue) > 0):
            RecBreadth(newQueue)
      q = deque()
      q.append(myNode)
      RecBreadth(q)
      return result
      
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
   bt.addNode(7)
   result = []
   bt.traverseTree(result)
   print ("result: {}".format(result))
   bt.printTree()
   bt.deleteNode(8)
   bt.printTree()
   print (bt.DepthFirstTraversal(bt.root))
   print (bt.BreadthFirstTraversal(bt.root))
   node = bt.findNode(5)
   node2 = bt.findNode(3)
   node2.left = node
   print (bt.BreadthFirstTraversal(node))
   # set back to none otherwise everything will break
   node2.left = None
   bt.printTree()
   

   