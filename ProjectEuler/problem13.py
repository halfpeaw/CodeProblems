#Problem 13
#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

import sys
sys.path.append("../SupportFunctions/")
import EulerSupport


@EulerSupport.printTiming
def cheatway(nums):
  val = 0
  for item in nums:
    val+=int(item[0])
  print(str(val)[:10])
  return(str(val)[:10])

@EulerSupport.printTiming
#This function works by cylcing through each least significant digit and adding that number
#Then taking the mod 10 of that number and making it the result and then carry the sum over to 
#the next column of digits
def addSplit(nums):
  word = ""
  length = len(nums[0][0])
  print("Length: " + str(length))
  carry = 0
  for pos in range(length-1,-1,-1): #49..0
    for num in nums:
      carry += int(num[0][pos])
    dangle = carry % 10
    carry -= dangle
    carry = int(carry / 10)
    word = str(dangle) + word
  word = str(carry) + word
  print(word[:10])
  return(word[:10])
  
  

if __name__ == "__main__":
  print("Problem 13")
  filePath = "./InputFiles/numbersP13.txt"
  nums = EulerSupport.parseUnicodeSepFile(filePath, False)
  #This way solved it more cleverly and would be useful in a larger system
  EulerSupport.printTiming(addSplit(nums))
  #This is the way that just summed all the numbers using python
  EulerSupport.printTiming(cheatway(nums))
  