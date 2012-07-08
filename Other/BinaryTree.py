
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
    #Even root is None just make the new node root
    if currentNode == None:
      self.root = Node(val = val)
      return True
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
    if (node == None):
      return None
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
  
  #Need to assume BST otherwise it will be weird...
  def delNode(self, val):
    node = self.FindNode(val)
    parent = node.parent
    isRight = node.isRight()
    #Its root
    if isRight == None:
      if node.left == None and node.right == None:
        print("Warning you now have an empty tree")
        self.root = None
      elif node.left == None: #therefore right isn't None
        self.root = node.right
        self.root.parent = None
      elif node.right == None: #therefor left isn't None
        self.root = node.left
        self.root.parent = None
      else:
       self.root = node.right
       self.root.parent = None
       lastNode = node.right
       while lastNode.left != None:
        lastNode = lastNode.left
       lastNode.left = node.left
       node.left.parent = lastNode
       node = None
    elif isRight:
      if node.left == None and node.right == None:
        parent.right = None
      elif node.left == None: #therefore right isn't None
        parent.right = node.right
        node.right.parent = parent
        node = None
        print (parent.right.val)
        print (parent.right.left)
      elif node.right == None: #therefor left isn't None
        parent.right = node.left
        node = None
      else: # We have two children so a bit more complicated
        #Always replace the deleted node with the right node and the
        #left node of the deleted node becomes the farthest left node on the replacement node
        parent.right = node.right
        node.right.parent = parent
        lastNode = node.right
        while lastNode.left != None:
          lastNode = lastNode.left
        lastNode.left = node.left
        lastNode.left.parent = lastNode
        node = None
    else:
      if node.left == None and node.right == None:
        parent.left = None
      elif node.left == None: #therefore right isn't None
        parent.left = node.right
        node = None
      elif node.right == None: #therefor left isn't None
        parent.left = node.left
        node.left.parent = parent
        node = None
      else: # We have two children so a bit more complicated
        #Always replace the deleted node with the right node and the
        #left node of the deleted node becomes the farthest left node on the replacement node
        parent.left = node.right
        lastNode = node.right
        while lastNode.left != None:
          lastNode = lastNode.left
        lastNode.left = node.left
        node.left.parent = lastNode
      
  def printTree(self, indent = 0, node = None, branch = "C"):
    space = "  " * indent 
    if node == None:
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
    self.parent = parent;
    self.left = None
    self.right = None
    self.val = val
  #Returns None if root, otherwise true if the right node and false if the left node of the parent
  def isRight(self):
    if self.parent == None:
      return None
    elif self.parent.right != None and self.parent.right.val == self.val:
      return True
    else:
      return False

#Start in the Far left and work your way to the far right
def inOrderTraversal(node):
  print("InOrderTraversal")
  result = []
  if (node == None):
    return result
  while node.left != None:
    node = node.left
  while node != None:
    result.append(node.val)
    if node.right != None:
      node = node.right
      while node.left != None:
        node = node.left
    #Can't go right any more
    else:
      while node.parent != None and node.parent.right != None and node.val == node.parent.right.val:
        node = node.parent
      node = node.parent
    #print(result)
  return result
      
#The marking isn't exactly necessary unless the nodes loop back on themselves which in the case 
#Of the BT this doesn't happen.  Leaving it in there in case this ever happens.
def breadthFirst(node):
  print ("BreadthFirst")
  mark = {}
  queue = []
  result = []
  if node == None:
    return result
  queue.append(node)
  mark[node.val] = True
  while len(queue) > 0:
    n = queue[0]
    queue = queue[1:]
    result.append(n.val)
    if n.left != None and not n.left.val in mark:
      mark[n.left.val] = True
      queue.append(n.left)
    if n.right != None and not n.right.val in mark:
      mark[n.right.val] = True
      queue.append(n.right)
  return result

#depth first search track the explored though really doesn't matter since we don't loop in BST
def depthFirst(node):
  result = []
  if (node == None):
    return result
  print ("Depth First")
  mark = {}
  mark[node.val] = True
  def depthRec(n):
    nonlocal mark
    nonlocal result
    result.append(n.val)
    
    if n.left != None and not n.left.val in mark:
      mark[n.left.val] = True
      depthRec(n.left)
    if n.right != None and not n.right.val in mark:
      mark[n.right.val] = True
      depthRec(n.right)
  depthRec(node)
  return result

  
#Do an inorder traversal determining that we got smallest to largest
def isBST(tree):
  node = tree.root
  #Empty Tree
  if (node == None):
    return True
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
  bt.addNode(val = 8)
  bt.printTree()
  x = 10
  print ("Deleting Node: %d"%x)
  bt.delNode(x)
  bt.printTree()
  print("Is BST: %s"%isBST(bt))
  print(inOrderTraversal(bt.root))
  print(breadthFirst(bt.root))
  print(depthFirst(bt.root))
  print("Lets add a bad node 6 after 20")
  bt.addNode(val = 6, desVal = 20)
  print("Is BST: %s"%isBST(bt))
  print(inOrderTraversal(bt.root))