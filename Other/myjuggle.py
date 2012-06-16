#C:\EclipseWorkspaces\CodeQuestions\PythonCode
#Juggle Problem
#Written by Alex Halfpenny at alex.halfpenny@gmail.com

import operator
import fileinput
import os
import re
from optparse import OptionParser


jugglers = []
circuits = []

class Circuit:
   
   def __init__(self, name, vec):
      self.name = name
      self.vec = vec
      self.players = []
   def toString(self):
      print ("------------------------------------------")
      print (self.name + " " + str(self.vec))
      for j in self.players:
         j[0].toString()
   
   #Adds the player to a to the following circuit if it works great otherwise it returns the juggler or the one being booted
   def addPlayer(self, juggler):
      #Circuits not full let em have their fun
      if (len(self.players) < numJugPerCirc):
         self.players.append((juggler,dotProd(juggler.vec,self.vec)))
         return None
      else:
         #Are you greater than your competition
         if dotProd(juggler.vec,self.vec) > min(self.players, key=lambda x: x[1])[1]:
            #print ("Append here " + self.name)
            self.players.append((juggler,dotProd(juggler.vec,self.vec)))
         #Weakest link no room at the cool kids table
         else:
            return juggler
      #Uh oh too many players in the circuit need to boot
      if len(self.players) > numJugPerCirc: 
         #find index of smallest player
         #print("Popping a player!")
         i = self.players.index(min(self.players, key=lambda x: x[1]))
         #self.toString()
         juggler = self.players.pop(i)[0]
         #print(juggler.name)
         return juggler
      else:
         return None
class Juggler:
   def __init__(self, name, vec, prefs):
      self.name = name
      self.vec = vec
      self.prefs = prefs
      self.listPos = 0
      self.prefPos = 0
      self.list = []
   def toString(self):
      print (self.name + " " + str(self.vec) + " pref: " + str(self.prefs))
   
   #The True Parameter means we are looking at preferred, False just working the total list
   def returnKey(self):
      if (self.prefPos < len(self.prefs)):
         return (self.prefPos,True)
      else:
         return (self.listPos,False)

   #Increment the key be it for the preferred list or the list of all entries
   def incrementKey(self):
      #print ("List Size: %d"%len(self.prefs))
      if (self.prefPos < len(self.prefs)):
         self.prefPos += 1
         return
      else:
         #print ("list pos %d"%self.listPos)
         self.listPos += 1
         return
   #generate the list of all circuits if needed
   def generateList(self):
      for circuit in circuits:
         self.list.append((circuit,dotProd(circuits[circuit].vec,self.vec)))
      #print("List: ",self.list)
      self.list = sorted(self.list,key=lambda x: x[1],reverse=True)  
   #Return the prefered items name based on pos
   def getPrefs(self,pos):
      return self.prefs[pos]
   #Find the next entry on the list
   def getList(self,pos):
      if (self.listPos == 0):
         self.generateList()
         #print (self.list)
      return self.list[pos][0]

def dotProd(vec1, vec2):
   return sum(map( operator.mul, vec1, vec2))

#Read in the input
#Format of input files
#C C0 H:7 E:7 P:10
#J J0 H:3 E:9 P:2 C2,C0,C1
def parseInput(fileName):
   global jugglers
   global circuits
   circuits = {}
   readFile = open(fileName,'r')
   for line in readFile:
      line = line.upper()
      #The regular expressions could probably be prettier but this gets the job done, just don't mess with the unicode or you'll be sorry
      #Highly dependent on input format be warned.
      if line.startswith("C"):
         x = re.findall(r'\w+', line)
         if len(x) < 8:
            print("Woh Woh Woh string is not properly formated")
            return 
         #Note the default storage of the vector within the list
         #Format: Name, Vec  Create the dictionary for the circuits
         circuits[x[1]] = (Circuit(x[1],(int(x[3]),int(x[5]),int(x[7]))))
      if line.startswith("J"):
         #breaks stuff up based on [A-Za-z0-9]
         x = re.findall(r'\w+', line)
         if len(x) < 8:
            print("Woh Woh Woh string is not properly formated")
            x[8] = ""
         #Note the default storage of the vector within the list
         #Format = Name, Vec, List of Pref
         jugglers.append(Juggler(x[1],(int(x[3]),int(x[5]),int(x[7])),x[8:]))
      #other data objects could work like a dictionary, but a simple list of list returns seemed easiest
   return

#Define the circuits list by cycling through all the jugglers
def constructBigList():
   for juggler in jugglers:
      isNewJuggler = addJugglers(juggler)
      while (isNewJuggler != None):
         isNewJuggler = addJugglers(isNewJuggler)
   for circuit in circuits:
      circuits[circuit].players = sorted(circuits[circuit].players ,key=lambda x: x[1],reverse=True)

#This was made recursively but the depth was too deep :(
def addJugglers(juggler):
   (pos,isPreferred) = juggler.returnKey()
   if isPreferred:
      circuit = circuits[juggler.getPrefs(pos)]
   else:
      circuit = circuits[juggler.getList(pos)]
   newJuggler = circuit.addPlayer(juggler)
   if newJuggler != None:
      newJuggler.incrementKey()
      #print ("None!")
   return newJuggler

#Take the existing built list of circuits and jugglers and create our output   
def genResult(fileName):
   writeFile = open(fileName,'w')
   #Example Format
   #C2 J6 C2:128 C1:31 C0:188, J3 C2:120 C0:171 C1:31, J10 C0:120 C2:86 C1:21, J0 C2:83 C0:104 C1:17 
   for circuit in sorted(circuits, key=lambda name: int(name[1:]), reverse=True):#sorted(circuits, key=lambda circuit: int(circuits[circuit].name[1:]), reverse=True):
      line = circuits[circuit].name + " "
      for (juggler,x) in circuits[circuit].players:
         line += juggler.name + " "
         for pref in juggler.prefs:
            line += pref + ":" + str(dotProd(circuits[pref].vec,juggler.vec)) + " "
         line =  line[:-1] + ", " #Yeah I know cheating by removing the excess space
      line = line[:-2] #cheating again by removing tailing space and ','
      #print(line)
      writeFile.write(line + "\n")

if __name__ == "__main__":
   global numJugPerCirc
   #fileName = '''C:/EclipseWorkspaces/CodeQuestions/PythonCode/JuggleInput.txt'''
   #outName = '''C:/EclipseWorkspaces/CodeQuestions/PythonCode/JuggleOutput.txt'''
   intro = '''Welcome to the fantastical juggle calculator, it may take a while to run...
Code works by cycling through a list of jugglers and then placing them in 
circuits. If a juggler no longer belongs in a circuit they are popped and 
they search again first search through the preferred list then sorted list, 
sorted list could be made more efficient without preferred items included.  
Once the popped find a home, we move to next juggler unless another had to 
be popped then we repeat. Code has been left relatively raw so you could see 
thought process before any optimizing and cleaning...

Plus I've been watching a Castle marathon which has been quite distracting 
and seriously wondering if every crime drama takes place in NYC.
But I digress let the function run...'''

   print (intro)
   print ("\nLimitations: ties go to the first entry, must have evenly divisible circuits and jugglers, and properly formated input\nAlso all input is uppered...")
   print ("-------------  Running --------------------")   
   parser = OptionParser()
   parser.add_option("-f", "--file", dest="fileName", default="./JuggleInput.txt",
                  help="Directory Source Path, default: ./JuggleInput.txt")
   parser.add_option("-d", "--des", dest="outName", default="./out.txt",
                  help="Directory Destination Path, default: ./out.txt")
   (options, args) = parser.parse_args()
   fileName = options.fileName
   outName = options.outName
   print ("Input: %s"%fileName)
   print ("Output: %s"%outName)
   if os.path.isfile(fileName):
      parseInput(fileName)
      #Violates constraint of the problem
      if (len(jugglers)%len(circuits)!=0):
         print("games size has been violated")
         exit()
   else:
      print("File %s doesn't exist"%fileName)
      exit()
   numJugPerCirc = len(jugglers) / len(circuits)
   constructBigList()
   #for circuit in circuits:
   #   circuit.toString()
   genResult(outName)
   print ("And done...")
   
   
   
   
   
   