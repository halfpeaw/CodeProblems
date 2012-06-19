#Problem 387
#A Harshad or Niven number is a number that is divisible by the sum of its digits. 
#201 is a Harshad number because it is divisible by 3 (the sum of its digits.) 
#When we truncate the last digit from 201, we get 20, which is a Harshad number. 
#When we truncate the last digit from 20, we get 2, which is also a Harshad number. 
#Let's call a Harshad number that, while recursively truncating the last digit, always results in a Harshad number a right truncatable Harshad number.
#
#Also: 
#201/3=67 which is prime. 
#Let's call a Harshad number that, when divided by the sum of its digits, results in a prime a strong Harshad number.
#
#Now take the number 2011 which is prime. 
#When we truncate the last digit from it we get 201, a strong Harshad number that is also right truncatable. 
#Let's call such primes strong, right truncatable Harshad primes.
#
#You are given that the sum of the strong, right truncatable Harshad primes less than 10000 is 90619.
#
#Find the sum of the strong, right truncatable Harshad primes less than 1014.
#
import sys
sys.path.append("../SupportFunctions/")
import EulerSupport
import time

getNum = lambda nums: sum(digit * 10 ** (len(nums) - 1 - i) for i, digit in enumerate(nums))

#
#First Solution is on top, it was a bruteish force way of solving the problem when my fast
#Approach wasn't working.  I did the simplie way first so I could confirm its results against 
#The Fast way.


#Determine if the number is Harshard Prime and all prev number
def isPrimeHarshad(num):
  s_num = str(num)
  list_of_ints = [int(i) for i in s_num]
  total = sum(list_of_ints)
  if total == 0: return True
  if (num % total == 0):
    if EulerSupport.miller_rabin(int(num / total)):
      #print("Test: " + str(num))
      return recursiveHarshad(list_of_ints[:-1])
  return False

#Determine if a number and all previous our Harshard
def recursiveHarshad(listInts):
  #print(listInts)
  if len(listInts) <= 1:
    return True
  val = getNum(listInts)
  total = sum(listInts)
  if val % total == 0:
    return recursiveHarshad(listInts[:-1])
  else:
    #print("reject: " + str(val) + " total: " + str(total))
    return False
  

#only works number n that our modulus 10
def BruteForceSum(n):
  print ("Brute Force For N: %d"%n)
  print ("Start: " + time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
  if n % 10 != 0:
    print("Must end in a 0")
    return(0)
  n = int(n / 10)
  total = 0
  for x in range(1,n,1):
      if (isPrimeHarshad(x)):
        #print(x)
        for c in "1234567890":
          val = int(str(x)+c)
          if (EulerSupport.miller_rabin(val)):
          #if (True):
            total+=val
            #print(val)
  print ("Total %d"%total)
  print ("End: " + time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())+"\n")
  return total
  
#Return True if the number is a Harshard
def isHarshad(splitNum):
  total = sum(splitNum)
  if total == 0: return True
  num = getNum(splitNum)
  if (num % total != 0):
    return False
  return True

#Return True if the number is a Harshard Prime
def isHarshadPrevPrime(splitNum):
  total = sum(splitNum)
  if total == 0: return True
  num = getNum(splitNum)
  if (num % total == 0):
    if (EulerSupport.miller_rabin(int(num / total))):
      return True
  return False
  
def findSumFast(n):
  print ("Fast Way For N: %d"%n)
  print ("Start: " + time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
  total = 0
  num = [0]*20
  # We default to 100 because 0-99 are not valid answers
  num[-3] = 1
  #So we don't have to constantly computer length
  TOP = len(num)-1
  i = TOP - 2
  #while num[0] < 10:
  #Constantly Converting the Array to an int is a 100% time increase.
  #Could write code find the max array value and compares more constantly
  #Or if you use powers of 10 exclusively like below
  #while num[-15] < 10:
  while getNum(num) < n:
    #Clean Up step if we exceed the bounds of where we are set to 0 and go back up a spot
    if num[i] > 9:
      num[i] = 0
      i -=1
      num[i]+=1
    #If our 1-Right deliminated value a Harshad and  Reduces to a prime
    #Then go to the next highest value and check if prime
    #Else no good and increment
    elif i == TOP - 1:
      if isHarshadPrevPrime(num[:i+1]):
        i+=1
      else:
        num[i] += 1
    #If we are at the top check to see if our total number is a prime, else increment
    elif i == TOP:
      if (EulerSupport.miller_rabin(getNum(num))):
        val = getNum(num)
        total += val
        num[TOP]+=1
      else:
        num[i]+=1
    #Every number preceding the TOP must be a Harshad, except 2nd to top thats Harshad Prime
    elif i < TOP - 1:
      if isHarshad(num[:i+1]):
        i += 1
      else:
        num[i]+=1
  print ("Total %d"%total)
  print ("End: " + time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())+ "\n")
  return total  
if __name__ == "__main__":
  
  print ("Problem 387")
  total = BruteForceSum(1000000)
  total = findSumFast(1000000)
  total = BruteForceSum(10000000)
  total = findSumFast(10000000)
  #10**14 = 696067597313468
  total = findSumFast(10**14)
  total = findSumFast(10**12+12)
  total = findSumFast(10**13+13)
  
