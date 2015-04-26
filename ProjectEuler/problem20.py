# Factorial Digit Sum Problem 20
import sys
sys.path.append("../SupportFunctions/")
import EulerSupport
import math

#This solved so fast it didn't seem worthwhile to add the efficiency but one thing you can do 
#is reduce out 0's so / 10 when %10 = 0 every number you are multiplying. So 90 -> 9 etc 
@EulerSupport.printTiming
def FactorialDigitSum(n):
   total = math.factorial(n)
   print ("{0}! result = {1}".format(n, total))
   splitResult = [int(i) for i in str(total)]
   print ("result {0} ".format(sum(splitResult)))


if __name__ == "__main__":
   print("Problem 20")
   print("What is the digit sum of the result of 100! ?")
   FactorialDigitSum(100)