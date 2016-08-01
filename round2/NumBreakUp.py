from collections import deque

def errorCheck(num):
   if not isinstance(num, int):
      print("not an int")
      return False
   return True
   
def breakUp(num):
   if not errorCheck(num): return None
   result = []
   for c in str(num):
      result.append(int(c))
   return result
   
def breakUpMath(num):
   if not errorCheck(num): return None
   result = deque()
   addNegative = False
   if (num < 0):
      addNegative = True
      num = abs(num)
   if (num == 0):
      return [0]
   pwr = 0 
   while (10**pwr <= num):
      pwr += 1
      # num 1024, pwr 2 ->  (24 - 4)//10 = 2
      val = (num%(10**pwr) - (num % 10**(pwr-1))) // (10 ** (pwr-1))
      result.appendleft(val)
   # Need to track if negative or positive
   if addNegative: 
      result.appendleft("-")
   else:
      result.appendleft("+")
      
   result = list(result)
   print("output {}".format(result))
   return result

def addNum(l, num):
   l = list(l) #copy value of l in to l so its no longer referencing argument passed in
   if ((num < 0 and l[0] == "+") or (num > 0 and l[0] == "-")):
      return subNum(l, num)
   bothNegative = False
   if (num < 0 and l[0] < 0):
      bothNegative = True
   digits = breakUpMath(num);
   digits = digits[1:]
   l = l[1:]
   if len(digits) > len(l):
      top = digits
      bottom = l
   else:
      top = l
      bottom = digits
   bottom.reverse()
   top.reverse()
   carryOver = 0
   for i in range(len(top)):
      toAdd = 0
      if(i < len(bottom)):
         toAdd = bottom[i]
      newNum = toAdd + carryOver + top[i]
      if newNum > 9:
         carryOver = 1
         newNum = newNum % 10
      else:
         carryOver = 0
      top[i] = newNum
   if (carryOver == 1):
      top = top + [1]
   top.reverse()
   if(bothNegative):
      top = ["-"] + top
   print("add: {}".format(top))
   return top

def subNum(l, num):
      print("balls")

# Take a number  convert it to an array and then add a taget number
# 123 + 11 => [1,2,3] + 11 => [1,3,4]
#How do we handle negatives?
if __name__ == "__main__":
   print("Num Breakup")
   breakUp(1234)
   result = breakUpMath(1234)
   breakUpMath(0)
   breakUpMath(1)
   print(912+1234)
   addNum(result, 912)
   
   print(99999+1234)
   print(result)
   addNum(result, -99999)
   
   