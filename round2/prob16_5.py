import sys
from functools import reduce
sys.path.append("../SupportFunctions/")
import EulerSupport

def factorial(num):
   if num == 0: return 1
   if num < 0: return None
   val = reduce((lambda x,y: x * y), range(1,num+1))
   return val

   
def leadingZero(num):
   #print("num = {}".format(num))
   if(num == 0): return 1
   if(num < 0): return None
   NumOfZeroes = 0
   while(num>9):
      if (num % 10 == 0):
         NumOfZeroes += 1
         num //= 10
      else:
         return NumOfZeroes
   return NumOfZeroes

@EulerSupport.printTiming    
def Prob16_5(num):
   #print("Prob16_5: {}".format(num))
   bigNum = factorial(num)
   #print("Factorial: {}".format(bigNum))
   result = leadingZero(bigNum)
   #print("Trailing zeroes: {}".format(result))
   return result

@EulerSupport.printTiming       
def Prob16_5Better(num):
   numZeroes = 0
   numTwos = 0
   numFives = 0
   for i in range(1,num+1):
      val = i
      while(val > 1):
         if val % 2 == 0:
            numTwos += 1
            val //= 2
         elif val % 5 == 0:
            numFives += 1
            val //= 5
         else:
            break
   #print("NumTwos {}".format(numTwos))
   #print("NumFives {}".format(numFives))
   result = numTwos if numTwos < numFives else numFives
   #print("Trailing zeroes: {}".format(result))
   return result

def FastAndSlow(num):
   print("Start with: {}".format(num))
   ans1 = Prob16_5(num)
   ans2 = Prob16_5Better(num)
   print("verify: {} equal {} is {}\n".format(ans1, ans2, ans1==ans2))
      
   
if __name__ == "__main__":
   print("misc")
   FastAndSlow(10)
   FastAndSlow(100)
   FastAndSlow(1000)
   FastAndSlow(10000)
   #FastAndSlow(30000)
   FastAndSlow(15)
   FastAndSlow(25)