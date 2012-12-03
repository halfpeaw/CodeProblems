#The prime 41, can be written as the sum of six consecutive primes:
#
#41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
#Which prime, below one-million, can be written as the sum of the most consecutive primes?

import sys
sys.path.append("../SupportFunctions/")
import EulerSupport

#Blah blah blah the code is really sloppy I did it super fast way overuse of variables.
@EulerSupport.printTiming
def problem50(n):
  primes = EulerSupport.getPrimes(n)
  #print (primes)
  maxLen = 0
  maxPrime = 0
  firstPrime = 0
  for i in range(0, len(primes)):
    total = 0
    tempTotal = 0
    next = i
    primeLen = 0
    while (tempTotal < n and next < len(primes)):
      tempTotal = tempTotal + primes[next]
      next = next + 1
      if tempTotal in primes:
        primeLen = next-i
        total = tempTotal
    if primeLen > maxLen:
      maxLen = primeLen
      maxPrime = total
      firstPrime = primes[i]
      print("Len: %d, Start: %d, max: %d"%(maxLen,firstPrime,maxPrime))
  print("Len: %d, Start: %d, max: %d"%(maxLen,firstPrime,maxPrime))
if __name__ == "__main__":
  print("Problem 50")
  problem50((10**6))