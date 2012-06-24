
#Red Black Tree
#A large chunk of this code was stolen because the goal wasn't to reinvent
#Red Black trees but to get a better understanding of it.  So its still a
#Work in progress.

class Node():
  def __init__(self, arg0, parent=None, left=None, right=None):
    self.red=True
    self.value=arg0
    self.parent=parent
    self.left=left
    self.right=right
  def isRed(self):
    return self.red
  def getParent(self):
    return self.parent
  def getGrandParent(self):
    if self.parent == None:
      return None
    else: 
      return self.parent.parent
  def __eq__(self,node2):
    if node2 == None:
      return False
    else:
     return self.value == node2.value
  def getUncle(self):
    if self.getGrandParent() != None:
      if self.getParent() == self.getGrandParent().left:
        return self.getGrandParent().right
      #Else we are the guy on the right
      return self.getGrandParent().left
    return None
  def isredstr(self):
    if self.red:
      return "red"
    else:
      return "black"
  def setBlack(self):
    self.red = False
  def setRed(self):
    self.red = True
  def isLeft(self):
    if self.parent == None:
      return None
    if self.parent.left != None:
      return self.parent.left.value == self.value
    return False
class RBTree():
  def __init__(self):
    self.root=None
  #Adds the root
  def add(self, value):
    if self.root == None:
      self.root = Node(value)
      self.root.setBlack()
      return
    self._add(value, self.root)
  
  #Adds a value with relationship to parent L/R rebalance
  def _add(self, value, node2=None):
    if node2.value > value:
      #Add to the left
      if node2.left == None:
        tmp = Node(value, parent=node2)
        node2.left = tmp
        self.rebalance(tmp)
      else:
        self._add(value,node2.left)
    elif node2.value < value:
        #Add to the right
        if node2.right == None:
          tmp = Node(value, parent=node2)
          node2.right = tmp
          self.rebalance(tmp)
        else:
          self._add(value,node2.right)
    else:
      print("Dup Found")

  def rebalance(self, node2):
    #Am I the root? Set to black
    if node2.parent == None:
      node2.setBlack()
      return
    #Is my parent black, no rebalance
    if not node2.parent.isRed():
      return
    if node2.getUncle() != None and node2.getUncle().isRed():
      node2.getUncle().setBlack()
      node2.parent.setBlack()
      self.rebalance(node2.getGrandParent())
      return
    self.pivotandrebalance(node2)
  
  def pivotandrebalance(self, node):
    if node.isLeft():
      if node.parent.isLeft():
        #left left -> False pivot around parent
        self.pivotRight(node.parent, False)
      else:
        self.pivotLeft(node, True)
    else: #Right
      if node.parent.isLeft():
        self.pivotRight(node, True)
      else:
        # right right -> False pivot around parent
        self.pivotLeft(node.parent, False)

  #How does this work!
  def pivotLeft(self, node, pivot=False):
    M = node
    G = node.parent
    if pivot:
      N = M.parent
      G = N.parent
      G.right = M
      M.parent = G
      N.left = M.right
      if M.right != None:
        M.right.parent = N
      M.right = N
      N.parent = M
    K = G.parent
    X = G.isLeft()
    G.right = M.left
    if G.right != None:
      G.right.parent = G
    M.left = G
    G.parent = M 
    G.setRed()
    M.setBlack()
    if K == None:
      M.parent = None
      self.root = M
    elif K != None and X:
      M.parent = K
      K.left = M
      K.setRed()
      self.rebalance(K)
    else:
      M.parent = K
      K.right = M
      K.setRed()
      self.rebalance(K)
      
  def pivotRight(self, node, pivot=False):
    M=node
    G=M.parent
    if pivot:
      N=M.parent	
      G=N.parent
      N.right=M.left
      if M.left is not None:
        N.right.parent=N
      G.left=M
      M.parent=G
      M.left=N
      N.parent=M
        
    K=G.parent
    X=G.isLeft()
    G.left=M.right
    if M.right is not None:
      M.right.parent=G
    M.right=G
    G.parent=M
    G.sr()
    M.sb()
    if K is None:
      M.parent=None
      self.root=M
    elif K is not None and X:
      M.parent=K
      K.left=M
      K.setRed()
      self.rebalance(K)
    else:
      M.parent=K
      K.right=M
      K.setRed()
      self.rebalance(K)
  
  #todo
  def delete(self, val):
    None
  
  def printtree(self, arg0=None):
    node=arg0
    if arg0 is None:
      node=self.root
    if node.left is not None:
      self.printtree(node.left)
    print ("%s (%s) -> " % ( node.value, node.isredstr()))
    if node.right is not None:
      self.printtree(node.right)	
if __name__ == "__main__":
  print("Red Black Tree")
  rbtree=RBTree()
  rbtree.add(10)
  rbtree.add(20)
  rbtree.add(30)
  rbtree.add(40)
  rbtree.add(10)
  rbtree.add(50)
  rbtree.add(60)
  rbtree.add(70)
  rbtree.add(80)
  rbtree.add(90)
  rbtree.printtree()
