#Python Helper Class
import re
import math

# This function will read in a file that's seperated by none A-Za-z0-9
def parseUnicodeSepFile(filePath, isInt):
  readFile = open(filePath,'r')
  results = []
  for line in readFile:
    list = []
    input = re.findall(r'\w+', line)
    for node in input:
      if isInt:
        list.append(int(node))
      else:
        list.append(node)
    results.append(list)
  return results

  
#First calculates a smaller fib number and then using doubling to get a larger fib number.
#The index is the location of the fib number you are searching for this is used to grow as
#Quickly as possible
def fibonacciFastGrow(index):
  a, b = 0, 1
  n = 1
  #Need a better way to coming to this number
  num = index
  while num > 250:
    num = num / 2
  whenStart = math.floor(num)
  while n < whenStart:
    yield (a,b,n)
    a,b = b, a+b
    n += 1
  
  while 2*n < index:
    yield (a,b,n)
    aN = a*a + b*b
    bN = b*(2*a+b)
    a = aN
    b = bN
    n = 2*n
  
  while True:
    yield (a,b,n)
    a,b = b, a+b
    n+=1
  
#Returns a list of all primes up to n
def getPrimes(n):
  list = [2]
  for x in range(3,n+1,2):
    isPrime = True
    for prime in list:
      if prime < (x / 2)+1:
        if x % prime == 0:
          isPrime = False
      else:
        break
    if isPrime:
      list.append(x)
  return list
  
def isPrime(num):
  n = math.ceil(num/2)+1
  list = getPrimes(n)
  for prime in list:
    if num % prime == 0:
      return False
  return True

def listPrimeComponents(num):
  print("List of Prime Components")
  
def countPrimeComponents(num):
  print("Count of each prime component")
