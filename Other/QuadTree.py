import sys
sys.path.append("../SupportFunctions/")
import EulerSupport

class Entry:
  def __init__(self, x, y, val):
    self.x = x
    self.y = y
    self.val = val
  def __repr__(self):
    return "[(%.1f,%.1f):%d]"%(self.x,self.y,self.val)

class QNode:
  #bounds = [N,S,W,E]
  def __init__(self, limit, items, bounds, parent = None):
    if limit < 1:
      sys.exit("Limit needs to be atleast 1")
    if items == None:
      sys.exit("Bad initialization")
    self.items = items
    self.limit = limit
    self.NW = None
    self.SW = None
    self.NE = None
    self.SE = None
    self.parent = parent
    self.bounds = bounds
    
    self.CreateSubNodes()
  def __repr__(self):
    return "Node Bounds: %s"%self.bounds
  #Debating if this would be better to just do this on the fly and load each item one at a time
  def CreateSubNodes(self):
    if (self.items != None and len(self.items) > self.limit):
      if self.NW != None or self.NE != None or  self.SW != None or  self.SE != None:
        sys.exit("Something is wrong in CreateSubNodes")
      N = self.bounds["N"]
      S = self.bounds["S"]
      W = self.bounds["W"]
      E = self.bounds["E"]
      self.NW = QNode(self.limit, [], {"N":N, "S":(N+S)/2, "W":W, "E": (W+E)/2} , self)
      self.NE = QNode(self.limit, [], {"N":N, "S":(N+S)/2, "W":(W+E)/2, "E":E} , self)
      self.SW = QNode(self.limit, [], {"N":(N+S)/2, "S":S, "W":W, "E":(W+E)/2} , self)
      self.SE = QNode(self.limit, [], {"N":(N+S)/2, "S":S, "W":(W+E)/2, "E":E}, self)
      for entry in self.items:
        if (self.within(self.NW.bounds, entry)):
            self.NW.addItem(entry)
        elif (self.within(self.NE.bounds, entry)):
            self.NE.addItem(entry)
        elif (self.within(self.SW.bounds, entry)):
            self.SW.addItem(entry)
        elif (self.within(self.SE.bounds, entry)):
            self.SE.addItem(entry)
        else:
          print(self.bounds)
          print("BAD! %s"%entry)
      self.items = None
    return
      
  def within(self, bounds, entry):
    if entry.x >= bounds["W"] and entry.x <= bounds["E"] and entry.y <= bounds["N"] and entry.y >= bounds["S"]:
      return True
    return False
  #determine which node a entry would belong.  May make this recursive so it returns the actual node instead of the next level
  def determineQuandrant(self, entry):
    if (self.NW != None and self.NE != None and self.SW != None  and self.SE != None):
      if (self.within(self.NW.bounds, entry)):
          return self.NW
      elif (self.within(self.NE.bounds, entry)):
          return self.NE
      elif (self.within(self.SW.bounds, entry)):
          return self.SW
      elif (self.within(self.SE.bounds, entry)):
          return self.SE
      else:
        return None
    else:
      return self
     
  def addItem(self,entry):
    if not self.within(self.bounds, entry):
      print("Item not within bounds")
      return -1
    #Search through the nodes until you find a node that is accepting items aka items != None
    node = self
    while (node != None and node.items == None):
      node = node.determineQuandrant(entry)
    if node != None:
      node.items.append(entry)
      #Since we just added an item to our node we run createSubNodes.  
      #If we have violated our node.limit it will break that node is to smaller parts
      node.CreateSubNodes()
    else:
      print("Error in addItem")
      sys.exit()
    
      
  def determineIntersect(self, bounds):
    None
    

  
  def printTree(self, indent = 0):
    space = " "*indent
    if (self.items != []):
      print ("%s->(%s): %s"%(space,self.bounds,self.items))
    if (self.NW != None):
      self.NW.printTree(indent+1)
    if (self.SW != None):
      self.SW.printTree(indent+1)
    if (self.NE != None):
      self.NE.printTree(indent+1)
    if (self.SE != None):
      self.SE.printTree(indent+1)
  
    
  
class QuadTree:
  #bounds = [N,S,W,E]
  @EulerSupport.printTiming 
  def __init__(self, limit, items, bounds):
    print (limit)
    self.root = QNode(limit, items, bounds)
  @EulerSupport.printTiming 
  def addEntry(self, entry):
    self.root.addItem(entry)
  def findEntry(self, entry):
    None
  #Need to think of a good way to do this since my entries aren't unique
  def removeEntry(self, value):
    None
  def updateLimit(self, limit):
    self.limit = limit
  def printTree(self):
    self.root.printTree()
  def adjustSingleLimit(self, node):
    None
  def queryRange(self, bounds):
    None

if __name__ == "__main__":
  print ("Quad Tree")
  items = [Entry(0,0,1),Entry(0,2,2),Entry(3,0,1),Entry(-1,-1,1),Entry(1,3,1),
          Entry(0,2.5,2),Entry(3.5,0,1),Entry(-.5,-1,6),Entry(-.7,0,4),Entry(7,2,8),]
          #Entry(3,-2,1),Entry(-1,-1,3),Entry(0,0,5),Entry(0,2,2),Entry(3,0,1),Entry(-1,-1,1)]
  bounds = {"N":10.0, "S":-10.0, "W":-10.0,"E":10.0}
  tree = QuadTree(2, items, bounds)
  #tree.printTree()
  tree.addEntry(Entry(1,1,1000))
  tree.printTree()
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  