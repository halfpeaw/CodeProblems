import re
ORD_NAME = 96
def parseFile(filePath):
  readFile = open(filePath,'r')
  results = []
  for line in readFile:
    line = line.lower()
    input = re.findall(r'\w+', line)
    for node in input:
      results.append(node) 
  return results
  
def calcSum(myList):
  myList = sorted(myList)
  count = 1
  totalSum = 0
  for name in myList:
    sum = 0
    for char in name:
      sum += ord(char)- ORD_NAME
    totalSum += sum * count
    count += 1
  print(totalSum)
if __name__ == "__main__":
  filePath = "C:/Workspace/PythonProblems/ProjectEuler/InputFiles/namesP22.txt"
  results = parseFile(filePath)
  calcSum(results)
  