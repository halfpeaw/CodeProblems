#bilateral.py
import operator
import fileinput
import os
import re

teams = []
numTeams = 0

def parseList(fileName):
   global teams
   global numTeams
   teams = []
   readFile = open(fileName,'r')
   for line in readFile:
      input = re.findall(r'\w+', line)
      if len(input) == 2:
         teams.append( (int(input[0]),int(input[1])) )
      elif len(input) == 1:
         #Meh not sure why I care about this field but its provided
         numTeams = int(input[0])
      else:
         print("Failure bad input")
         return


#This could be done in the parselist function but doing it here to create simplicty
def buildDictPairing():
   result = {}
   for pair in teams:
      for item in pair:
         if not (item in result):
            result[item] = []
         for i in pair:
            if i != item:
               result[item].append(i)
   print(result)
   return result

def buildFinalList(teamDict, pref):
   result = []
   teamDict = sorted(teamDict, key=lambda name: len(teamDict[name]), reverse = True)
   for key in teamDict:
      result.append(key)
      for item in teamDict[key]:
         del teamDict[item]
   
            
if __name__ == "__main__":
   parseList("./BilateralSimple.txt")
   print(teams)
   print(numTeams)
   buildDictPairing()

              