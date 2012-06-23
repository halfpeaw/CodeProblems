#Problem 74
#The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
#
#1! + 4! + 5! = 1 + 24 + 120 = 145
#
#Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:
#
#169 -> 363601 -> 1454 -> 169
#871 -> 45361 -> 871
#872 -> 45362 -> 872
#
#It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
#
#69 -> 363600 -> 1454 -> 169 -> 363601 ->( 1454)
#78 -> 45360 -> 871 -> 45361 ->( 871)
#540 -> 145 ->( 145)
#
#Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.
#
#How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
import sys
sys.path.append("../SupportFunctions/")
import EulerSupport
import math

global total60
total60 = [0]
class Node:
  def __init__(self, name, nextNode, lastParent = 0, tillEnd=0):
    self.name = name
    self.nextNode = nextNode
    self.lastParent = lastParent #string: Unused for Now
    self.tillEnd = tillEnd #int: Unused for Now
  def setParent(self, lastParent):
    self.lastParent = lastParent
  def toString(self):
    if (self.nextNode > 0):
      print("Self: %d Parent: %d Next: %d Till End: %d"%(self.name,self.lastParent,self.nextNode, self.tillEnd))
    else:
      print("Self: %d Parent: %d Next: END Till End: %d"%(self.name,self.lastParent, self.tillEnd))
@EulerSupport.printTiming
def buildList(n):
  for i in range(69,n+1):
    constructList(i)
  #for node in listNodes:
    #if listNodes[node].tillEnd > 45:
  #    listNodes[node].toString()

def constructList(num):
  orgin = num
  parent = 0
  while not (num in listNodes):
    next = 0
    for x in str(num):
      next += math.factorial(int(x))
    listNodes[num] = Node(num, next, parent)
    if num == next:
      print ("Next: %d set to 0 Parent: %d"%(num,parent))
      next = 0 #Signifies the end
    parent = num
    num = next
  #Update the last parent with the most recent node
  listNodes[num].lastParent = parent
  #get the known till end
  tillEnd = listNodes[num].tillEnd
  #Do I have a parent?
  
  while listNodes[num].lastParent != 0:
    num = listNodes[num].lastParent
    tillEnd+=1
    listNodes[num].tillEnd = tillEnd
    
    #so here's why mine chokes... I force fed dumb endings so I never include the bits before the cycle happens.  Also I end on 0 instead of 1
    if tillEnd >= 57: 
      total60[0]+=1
      #printFullPath(num)
      return

def printFullPath(num):
  tillEnd = 1
  while tillEnd != 0:
    listNodes[num].toString()
    tillEnd = listNodes[num].tillEnd
    num =  listNodes[num].nextNode
  print("---------------------------------------------------")
    
    

    
if __name__ == "__main__":
  print ("Problem 74, solved with a linked arrayish kind of thing")
  global listNodes
  listNodes = {}
  #Stop issues with cycling
  listNodes[169] = Node(169,0,1454)
  listNodes[871] = Node(871,0,45361)
  listNodes[872] = Node(872,0,45362)
  buildList(1000000)
  print(total60)