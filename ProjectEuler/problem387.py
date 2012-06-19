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

getNum = lambda nums: sum(digit * 10 ** (len(nums) - 1 - i) for i, digit in enumerate(nums))

#Return the true if it is a harshard as well as the number
def isHarshad(splitNum):
  total = sum(splitNum)
  if total == 0: return True
  num = getNum(splitNum)
  if (num % total != 0):
    return False
  return True
#Currently Finds the sum of all harsah right deliminated numbers that end in prime.
#Needs to find all that end in prime then R deliminate to Harshad, then R Deliminate to Prime
def findSum(n):
  total = 0
  num = [0,0,0,0]
  size = 1
  i = 0
  TOP = len(num)-1
  while num[0] < 10:
    if getNum(num) < 9:
      num[TOP] = 0
      i = TOP - 1
      num[i] = 1
    #cleanup step
    if num[i] > 9:
      num[i] = 0
      i -=1
      num[i]+=1
    elif i == TOP and EulerSupport.miller_rabin(getNum(num)):
      val = getNum(num)
      #print ("Found Prime: " + str(val))
      #print("Total: " + str(total))
      print(num)
      total += val
      num[TOP]+=1
    # Or... Not of an Or
    elif (not i == TOP and not isHarshad(num[:i+1])):
      num[i]+=1
    elif not i == TOP and isHarshad(num[:i+1]):
      #if  getNum(num[:i]) == 0 or EulerSupport.miller_rabin(getNum(num[:i])):
        i += 1
      #else:
      #  #print(num)
      #  num[i] = 0
      #  i-=1
      #  num[i]+=1
    elif i == TOP:
      num[i]+=1
  return total
if __name__ == "__main__":
  
  print ("Problem 387")
  sum = findSum(100)
  print (sum)