
class BT:
  root = None
  def __init__(self, val):
    self.root = Node(val = val)
  #can also manually generate a tree
  def addNode(self, val = 0, desVal = None):
    if (desVal == None):
      currentNode = self.root
    #This else statement lets our add be based off a specific node as opposed to always looking at the root
    #This basically exist so I can create a binary tree that violates BST
    else:
      currentNode = self.FindNode(desVal)
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
  
  #This is a breadth first search that will return a node based on a given value
  def FindNode(self, val):
    node = self.root
    mark = {}
    queue = []
    queue.append(node)
    mark[node.val] = True
    while len(queue) > 0:
      n = queue[0]
      queue = queue[1:]
      if (n.val == val):
        return n
      if n.left != None and not n.left.val in mark:
        mark[n.left.val] = True
        queue.append(n.left)
      if n.right != None and not n.right.val in mark:
        mark[n.right.val] = True
        queue.append(n.right)
    print("Node not found returning root")
    return self.root
  #Lets assume BT not BST
  def delNode(self, val):
    None
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
  print("InOrderTraversal")
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
      
#The marking isn't exactly necessary unless the nodes loop back on themselves which in the case 
#Of the BT this doesn't happen.  Leaving it in there in case this ever happens.
def breadthFirst(node):
  print ("BreadthFirst")
  mark = {}
  queue = []
  queue.append(node)
  mark[node.val] = True
  while len(queue) > 0:
    n = queue[0]
    queue = queue[1:]
    print("Val %d"%n.val)
    if n.left != None and not n.left.val in mark:
      mark[n.left.val] = True
      queue.append(n.left)
    if n.right != None and not n.right.val in mark:
      mark[n.right.val] = True
      queue.append(n.right)
    

def depthFirst(node):
  print ("Depth First")
  mark = {}
  mark[node.val] = True
  def depthRec(n):
    print(n.val)
    nonlocal mark
    if n.left != None and not n.left.val in mark:
      mark[n.left.val] = True
      depthRec(n.left)
    if n.right != None and not n.right.val in mark:
      mark[n.right.val] = True
      depthRec(n.right)
  depthRec(node)

  
def isBST(tree):
  node = tree.root
  while node.left != None:
    node = node.left
  current = node.val
  while node != None:
    next = node.val
    if next < current:
      return False
    else:
      current = next
    if node.right != None:
      node = node.right
      while node.left != None:
        node = node.left
    #Can't go right any more
    else:
      while node.parent != None and node.parent.right != None and node.val == node.parent.right.val:
        node = node.parent
      node = node.parent
  return True
if __name__ == "__main__":
  print("Binary Tree Program")
  bt = BT(10)
  bt.addNode(val = 5)
  bt.addNode(val = 15)
  bt.addNode(val = 12)
  bt.addNode(val = 7)
  bt.addNode(val = 2)
  bt.addNode(val = 5)
  bt.addNode(val = 17)
  bt.addNode(val = 20)
  print("Is BST: %s"%isBST(bt))
  print("Lets add a bad node 6 after 20")
  bt.addNode(val = 6, desVal = 20)
  bt.printTree()
  print("Is BST: %s"%isBST(bt))
  #inOrderTraversal(bt.root)
  #breadthFirst(bt.root)
  #depthFirst(bt.root)