#problem 23
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper 
# divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# 
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# 
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant 
# numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant 
# numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot 
# be expressed as the sum of two abundant numbers is less than this limit.
# 
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import sys
sys.path.append("../SupportFunctions/")
import EulerSupport
import math

CAP = 28124

def isAbundantNumber(n):
   result = EulerSupport.FindProperDivisors(n)
   total = sum(result)
   if (total > n):
      return (total, 1)
   elif (total == n):
      return (total, 0)
   else:
      return (total, -1)

@EulerSupport.printTiming     
def FindAllAbundantNumbers(n):
   result = []
   for i in range(2,n+1):
      total, isAbundant = isAbundantNumber(i)
      if (isAbundant == 1):
         result.append(i)
   #print (result)
   return result

@EulerSupport.printTiming   
def findAllNoneSummations(numbersToAdd, n):
   results = [1] * n
   for x in range(0, len(numbersToAdd)):
      for y in range(x, len(numbersToAdd)):
         # If we are greater than n no sense in continuing inner loop
         sum = numbersToAdd[x]+numbersToAdd[y]
         if sum < n:
            results[sum] = 0
         else:
            break
   
   sum = 0
   for i in range(1, len(results)):
      if results[i] == 1:
         sum += i
      
   #print (sorted(resultsNum))
   print ("Sum = " + str(sum))

if __name__ == "__main__":
   print("Problem 23")
   print("Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.")
   
   numbersToAdd = FindAllAbundantNumbers(CAP)
   findAllNoneSummations(numbersToAdd, CAP)