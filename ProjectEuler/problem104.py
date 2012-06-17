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
    if ('1' in first and '2' in first and '3' in first and '4' in first 
      and '5' in first and '6' in first and '7' in first and '8' in first and '9' in first):
      print ("Found first: " + str(x))
      last = arg[-9:]
      
      if ('1' in last and '2' in last and '3' in last and '4' in last 
        and '5' in last and '6' in last and '7' in last and '8' in last and '9' in last):
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
  while x < 1000000:
    #Alrighty calculated 1000 (starting at 0) so we start at 10001 so we don't have to be base 0
    x +=1
    arg = fib.__next__()  
    arg = str(arg)
    last = arg[-9:]
    if ('1' in last and '2' in last and '3' in last and '4' in last 
        and '5' in last and '6' in last and '7' in last and '8' in last and '9' in last):
      #print ("Last: " + str(x))
      results += (x,)
  return results

#Quick way of finding fib by index 
def findFib(index):
  fib = fibonacciFastGrow(index)  
  n = 0
  while n < index:
    arg = fib.__next__()
    n = arg[2]
  print("N: " + str(arg[2]))
  first = str(arg[1])[:9]
  if ('1' in first and '2' in first and '3' in first and '4' in first 
      and '5' in first and '6' in first and '7' in first and '8' in first and '9' in first):
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
  
  
    

    
  