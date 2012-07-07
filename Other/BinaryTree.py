
class BT:
  root = None
  def __init__(self, val):
    self.root = Node(val = val)
  #can also manually generate a tree
  def addNode(self, val):
    currentNode = self.root
    while True:
      if val == currentNode.val:
        print("Val: %d is a duplicate"%val)
        return False
      #Look Left
      elif val < currentNode.val:
        if currentNode.left == None:
          currentNode.left = Node(val = val, parent = currentNode)
          return True
        else:
          currentNode = currentNode.left
      #Look Right
      else:
        if currentNode.right == None:
          currentNode.right = Node(val = val, parent = currentNode)
          return True
        else:
          currentNode = currentNode.right
  #Lets assume BT not BST
  def delNode(self, val):
    None
  #Lets assume BT not BST
  def hasNode(self, val):
    return False
  def printTree(self, indent = 0, node = None, branch = "C"):
    space = "  " * indent 
    if node == None:
      node = self.root
    print ("%s%s %d->"%(space,branch,node.val))
    if node.left != None:
      self.printTree(indent = indent+1, node = node.left, branch = "L")
    if node.right != None:
      self.printTree(indent = indent+1, node = node.right, branch = "R")
class Node:
  def __init__(self, val = 0, parent = None):
    self.parent = parent;
    self.left = None
    self.right = None
    self.val = val

    
def inOrderTraversal(node):
  while node.left != None:
    node = node.left
  while node != None:
    print(node.val)
    if node.right != None:
      node = node.right
      while node.left != None:
        node = node.left
    #Can't go right any more
    else:
      while node.parent != None and node.parent.right != None and node.val == node.parent.right.val:
        node = node.parent
      node = node.parent
      

def breadthFirst(node):
  queue = []
  queue.append(node)
  while len(queue) > 0:
    n = queue.pop()
    print(n.val)
    #Check val here if we were doing a search
    #Return if n.val matches
    
  
def isBST(tree):
  print("Is BST Tree");
if __name__ == "__main__":
  print("Binary Tree Program")
  bt = BT(10)
  bt.addNode(5)
  bt.addNode(15)
  bt.addNode(12)
  bt.addNode(7)
  bt.addNode(2)
  bt.addNode(5)
  bt.addNode(17)
  bt.addNode(20)
  bt.printTree()
  inOrderTraversal(bt.root)