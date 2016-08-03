import uuid

class LL:
   first = None
   def __init__(self, val):
      self.first = Node(val)
   
   def addNode(self, val):
      if (self.isInfinite()):
         print ("LL loops on itself therefore can't append")
         return
      node = Node(val)
      last = self.first
      while(last.next != None):
         last = last.next
      last.next = node
      return node
   
   def printList(self):
      result = []
      if (self.isInfinite()):
         return
      node = self.first
      while(node != None):
         result.append(node.val)
         node = node.next
      print(result)
      return result
   
   def getLast(self):
      node = self.first
      while(node.next != None):
         node = node.next
      print("last {}".format(node.val))
      return node
   
   def reverseList(self):
      if (self.isInfinite()):
         return
      start = self.first
      swap = self.first.next
      start.next = None
      pivot = None
      if (swap != None):
         pivot = swap.next
      #if our second value is also None then our list is only item so nothing to reverse
      else:
         return
         
      while True:
         swap.next = start
         if (pivot == None):
            self.first = swap
            return
         #advance everything by 1
         start = swap
         swap = pivot
         pivot = swap.next
         
      
   
   #go by 1 and go by 2 for two different nodes if infinite should meet eventually   
   def isInfinite(self):
      nodeBy1 = self.first
      if (nodeBy1.next == None):
         return False
      nodeBy2 = self.first.next
      while (nodeBy1.uid != nodeBy2.uid):
         if (nodeBy1.next == None):
            return False
         if (nodeBy2.next == None or (nodeBy2.next).next == None):
            return False
         nodeBy1 = nodeBy1.next
         nodeBy2 = (nodeBy2.next).next
      print ("LL loops on itself therefore it is infinite")
      return True
      
      
class Node:
   val = None
   next = None
   uid = None
   def __init__(self, val):
      self.val = val
      self.uid = str(uuid.uuid1())
      
   def printVal(self):
      print("value is {}".format(self.val))
      

if __name__ == "__main__":
   x = LL(5)
   n1 = x.addNode(10)
   x.addNode(15)
   x.addNode(20)
   n2 = x.addNode(25)
   x.printList()
   n2.next = n1
   x.printList()
   n2.next = None
   x.printList()
   x.getLast()
   x.reverseList()
   x.printList()
   x.getLast()