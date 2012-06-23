#Problem 386
#Let n be an integer and S(n) be the set of factors of n.
#
#A subset A of S(n) is called an antichain of S(n) if A contains only one element or if none of the elements of A divides any of the other elements of A.
#
#For example: S(30) = {1, 2, 3, 5, 6, 10, 15, 30} 
#{2, 5, 6} is not an antichain of S(30). 
#{2, 3, 5} is an antichain of S(30).
#
#Let N(n) be the maximum length of an antichain of S(n).
#
#Find SN(n) for 1  n  10^8#

import sys
sys.path.append("../SupportFunctions/")
import EulerSupport

@EulerSupport.printTiming
def program(n):
  print("Result: %d"%n)
  for i in range (1,n+1):
    result = EulerSupport.countPrimeComponents(i)

@EulerSupport.printTiming
def countStuff():
  x=0
  for i in range (1,10**8):
    x+=1
  print(x)

def findSChain(n):
  None

def findAntiChain(listN):
  None


if __name__ == "__main__":
  print("Problem 386")
  #EulerSupport.printTiming(program(10**1))
  #EulerSupport.printTiming(program(10**2))
  #EulerSupport.printTiming(program(10**3))
  #EulerSupport.printTiming(program(10**4))
  #EulerSupport.printTiming(program(10**5))
  #EulerSupport.printTiming(program(10**6))
  #EulerSupport.printTiming(program(10**7))
  #EulerSupport.printTiming(program(10**8))
  EulerSupport.printTiming(countStuff())