import math
import sys
sys.path.append("../SupportFunctions/")
from EulerSupport import fibonacciFastGrow

def fibonacci():
  a, b = 0, 1
  while True:
    yield b
    a,b = b, a+b

def fibLowNine():
  a,b = 0, 1
  while True:
    yield b
    a,b = b, ((a+b) % 1000000000)

#This pretty much won't work the number is WAY too big....
def fibBruteForce():
  fib = fibonacci()
  for x in range(1000):
    arg = fib.__next__()  
  x = 1000
  while True:
    x +=1
    arg = fib.__next__()  
    arg = str(arg)
    first = arg[:9]
    mSet = set('123456789')
    if (set(first) == mSet):
      print ("Found first: " + str(x))
      last = arg[-9:]
      
      if (set(last) == mSet):
        print ("Found both: " + str(x))
        print ("First: "  + first)
        print ("Last: " + last)
        print ("Found both: " + str(x))
        exit()

def fibLower():
  fib = fibLowNine()
  #fib = fibonacci()
  results = ()
  for x in range(1000):
    arg = fib.__next__()  
  x = 1000
  comp = set("123456789")
  while x < 1000000:
    #Alrighty calculated 1000 (starting at 0) so we start at 10001 so we don't have to be base 0
    x +=1
    arg = fib.__next__()  
    arg = str(arg)
    last = arg[-9:]
    if (set(last) == comp):
      #print ("Last: " + str(x))
      results += (x,)
  return results

#Quick way of finding fib by index 
def findFib(index):
  fib = fibonacciFastGrow(index)  
  n = 0
  comp = set("123456789")
  while n < index:
    arg = fib.__next__()
    n = arg[2]
  print("N: " + str(arg[2]))
  first = str(arg[1])[:9]
  if (set(first) == comp):
    print(arg[1],arg[2])
    exit()
  else:
    print("No Match: %d"%(arg[2]))
  
  
def findNext(a,b,n):
  return (b,b+a,n+1)
    
    
if __name__ == "__main__":
  print("Problem 104")
  print("Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.")
  #Calculates a list of fib with the last set to pandigital
  results = fibLower()
  for index in results:
    findFib(index)
  
  
    

    
  