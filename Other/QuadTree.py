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
    self.items = items
    self.limit = limit
    self.NW = None
    self.SW = None
    self.NE = None
    self.SE = None
    self.parent = parent
    self.bounds = bounds
    self.breakUpNode()
  def breakUpNode(self): 
    if (self.items != None and len(self.items) > self.limit):
      newItems = self.CreateSubLists(self.items)
      self.items = None
      self.NW = QNode(self.limit, newItems["NW"], 
        newItems["NWBounds"], self)
      self.SW = QNode(self.limit, newItems["SW"], 
        newItems["SWBounds"], self)
      self.NE = QNode(self.limit, newItems["NE"],
        newItems["NEBounds"], self)
      self.SE = QNode(self.limit, newItems["SE"], 
        newItems["SEBounds"], self)
      
  def addItem(self,entry):
    if entry.x > self.bounds["E"] or entry.x < self.bounds["W"] or entry.y > self.bounds["N"] or entry.y < self.bounds["S"]:
      return -1
    #Really only need to check one you either have 4 children and are empty or no children and have the full list
    node = self.determineQuandrant(entry)
    #If Node is None that implies there are no children
    if node != None:
      node.addItem(entry)
    elif self.items != None:
      self.items.append(entry)
      self.breakUpNode()
    else:
      print ("Something went wrong in AddItem")
  
  def determineQuandrant(self, entry):
    x = entry.x
    y = entry.y
    if (self.NW != None and self.NE != None and self.SW != None  and self.SE != None):
      if (x < self.NW.bounds["E"] and x >= self.NW.bounds["W"] 
            and y >= self.NW.bounds["S"] and y <= self.NW.bounds["N"]):
          return self.NW
      elif (x >= self.NE.bounds["W"] and x <= self.NE.bounds["E"] 
            and y >= self.NE.bounds["S"] and y <= self.NE.bounds["N"]):
          return self.NE
      elif (x < self.SW.bounds["E"] and x >= self.SW.bounds["W"] 
            and y < self.SW.bounds["N"] and y >= self.SW.bounds["S"]):
          return self.SW
      elif (x >= self.SE.bounds["W"] and entry.x <= self.SE.bounds["E"] 
            and y < self.SE.bounds["N"] and y >= self.SE.bounds["S"]):
          return self.SE
      else:
        return None
    else:
      return None
    
      
    
  #bounds = [N,S,W,E]
  #Debating if this would be better to just do this on the fly and load each item one at a time
  def CreateSubLists(self,items):
    N = self.bounds["N"]
    S = self.bounds["S"]
    W = self.bounds["W"]
    E = self.bounds["E"]
    newItems = {}
    newItems["NW"] = []
    newItems["NE"] = []
    newItems["SW"] = []
    newItems["SE"] = []
    newItems["BAD"] = []
    newItems["NWBounds"] = {"N":N, "S":(N+S)/2, "W":W, "E": (W+E)/2} 
    newItems["NEBounds"] = {"N":N, "S":(N+S)/2, "W":(W+E)/2, "E":E}  
    newItems["SWBounds"] = {"N":(N+S)/2, "S":S, "W":W, "E":(W+E)/2}  
    newItems["SEBounds"] = {"N":(N+S)/2, "S":S, "W":(W+E)/2, "E":E}  
    for entry in items:
      if (entry.x < newItems["NWBounds"]["E"] and entry.x >= newItems["NWBounds"]["W"] 
            and entry.y >= newItems["NWBounds"]["S"] and entry.y <= newItems["NWBounds"]["N"]):
          newItems["NW"].append(entry)
      elif (entry.x >= newItems["NEBounds"]["W"] and entry.x <= newItems["NEBounds"]["E"] 
            and entry.y >= newItems["NEBounds"]["S"] and entry.y <= newItems["NEBounds"]["N"]):
          newItems["NE"].append(entry)
      elif (entry.x < newItems["SWBounds"]["E"] and entry.x >= newItems["SWBounds"]["W"] 
            and entry.y < newItems["SWBounds"]["N"] and entry.y >= newItems["SWBounds"]["S"]):
          newItems["SW"].append(entry)
      elif (entry.x >= newItems["SEBounds"]["W"] and entry.x <= newItems["SEBounds"]["E"] 
            and entry.y < newItems["SEBounds"]["N"] and entry.y >= newItems["SEBounds"]["S"]):
          newItems["SE"].append(entry)            
      else:
        newItems["BAD"].append(entry)
        print(self.bounds)
        print("BAD! %s"%entry)
    return newItems
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
  def __init__(self, limit, items, bounds):
    print (limit)
    self.root = QNode(limit, items, bounds)
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
  items = [Entry(0,0,1),Entry(0,2,2),Entry(3,0,1),Entry(-1,-1,1),Entry(1,0,1),
          Entry(0,2.5,2),Entry(3.5,0,1),Entry(-.5,-1,6),Entry(-.7,0,4),Entry(0,2,8),]
          #Entry(3,-2,1),Entry(-1,-1,3),Entry(0,0,5),Entry(0,2,2),Entry(3,0,1),Entry(-1,-1,1)]
  bounds = {"N":10.0, "S":-10.0, "W":-10.0,"E":10.0}
  tree = QuadTree(5, items, bounds)
  tree.printTree()
  tree.addEntry(Entry(1,1,1000))
  tree.printTree()
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  