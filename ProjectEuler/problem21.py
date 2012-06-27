#Problem 21
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a not equal b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
#Evaluate the sum of all the amicable numbers under 10000.
import sys
sys.path.append("../SupportFunctions/")
import EulerSupport

@EulerSupport.printTiming
def findSum():
  grandTotal = 0
  for n in range(1,(10**4)+1):
    grandTotal+=buildDivList(n)
  print("Final: %d"%grandTotal)

#recursively calculates all the divisors.  Then if the sum of the results is valid recomputes for the sum
#If the sum of the second value ends up equalling N return the the sum of the two otherwise return 0
#
#Definite improvement that I'm too lazy to add atm because I have HW create a binary of list of visited number and 
#check them off as results are discovered save the trouble of calculating the divisors for a number more than once
def buildDivList(n):
  total = 0
  #return a list of tuples containing (prime, #ofPrime) of intenger n
  pList = EulerSupport.countPrimeComponents(n)
  #print(pList)
  #Made nonlocal instead of passing result cause it made so sense to constantly pass a consistent variable
  result = []
  def recursiveCount(vals,total):
    nonlocal result
    #This would only happen if an empty array were passed
    if len(vals) > 0:
      prime, count = vals[0]
    else:
      return [1]
    for i in range(0, count+1):
      tempTotal = total
      tempTotal *= pow(prime,i)
      if (len(vals) == 1):
        result.append(tempTotal)
      else:
        recursiveCount(vals[1:],tempTotal)
    return
  recursiveCount(pList,1)
  #Trim off the last number even though itself is a divisor not valid for this problem
  #Technically last number will always be equal to n
  result = result[:-1]
  firstTotal = sum(result)
  #The ones that divisors sum to itself are not valid...
  if n == firstTotal:
    #total += firstTotal
    print("Onsie: %d"%firstTotal)
  #If its less than then we've already covered it  
  elif firstTotal > n:
    pList = EulerSupport.countPrimeComponents(firstTotal)
    result = []
    recursiveCount(pList,1)
    result = result[:-1]
    if sum(result) == n:
      total += n
      total +=firstTotal
      print ("Twosie: %d %d"%(n,firstTotal))
  return(total)
          
  
if __name__ == "__main__":
  print("Problem 21")
  findSum()