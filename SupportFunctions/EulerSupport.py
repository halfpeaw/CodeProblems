#Python Helper Class
import re


# This function will read in a file that's seperated by none A-Za-z0-9
def parseUnicodeSepFile(filePath):
  readFile = open(filePath,'r')
  results = []
  for line in readFile:
    list = []
    input = re.findall(r'\w+', line)
    for node in input:
      list.append(node) 
  results.append(list)
  return results
  
def isPrime(num):
  print("isPrime")

def listPrimeComponents(num):
  print("List of Prime Components")
  
def countPrimeComponents(num):
  print("Count of each prime component")
