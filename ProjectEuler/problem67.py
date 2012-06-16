import os
import re


def parseFile(filePath):
  readFile = open(filePath,'r')
  tree = []
  for line in readFile:
    line = line.upper()
    input = re.findall(r'\w+', line)
    list = []
    for node in input:
      list.append(int(node)) 
    tree.append(list)
  return tree

def findTreeSum(tree):
	#tree = [[3],[7,4],[2,4,6],[8,5,9,3]]   
  tree.reverse()
  for tRow,bRow in (tree[i:i+2] for i in range(0,len(tree)-1,1)):
    i = 0
    for item in bRow:
      if tRow[i] > tRow[i+1]:
        bRow[i] =  bRow[i] + tRow[i]
      else:
        bRow[i] = bRow[i] + tRow[i+1]
      i += 1
    if len(bRow) == 1:
      print(bRow[0])
	
if __name__ == "__main__":
   
   print("Triangle Euler Project Problem 67 and 18")
   problem = '''Find the maximum path down a triange of interconnected nodes'''
   filePath = "C:/Workspace/PythonProblems/ProjectEuler/InputFiles/smallTriangleP18.txt"
   filePath = "C:/Workspace/PythonProblems/ProjectEuler/InputFiles/triangleP67.txt"
   tree = parseFile(filePath)
   findTreeSum(tree)