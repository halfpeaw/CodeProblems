#Python Helper Class
import re
import math
import random
import sys
import time

def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1


def miller_rabin(n):
    if n < 2: return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
	
    for repeat in range(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True


# This function will read in a file that's seperated by none A-Za-z0-9
def parseUnicodeSepFile(filePath, isInt):
  readFile = open(filePath,'r')
  results = []
  for line in readFile:
    list = []
    input = re.findall(r'\w+', line)
    for node in input:
      if isInt:
        list.append(int(node))
      else:
        list.append(node)
    results.append(list)
  return results

  
#First calculates a smaller fib number and then using doubling to get a larger fib number.
#The index is the location of the fib number you are searching for this is used to grow as
#Quickly as possible
def fibonacciFastGrow(index):
  a, b = 0, 1
  n = 1
  #Need a better way to coming to this number
  num = index
  while num > 250:
    num = num / 2
  whenStart = math.floor(num)
  while n < whenStart:
    yield (a,b,n)
    a,b = b, a+b
    n += 1
  
  while 2*n < index:
    yield (a,b,n)
    aN = a*a + b*b
    bN = b*(2*a+b)
    a = aN
    b = bN
    n = 2*n
  
  while True:
    yield (a,b,n)
    a,b = b, a+b
    n+=1
  
#Returns a list of all primes up to n
def getPrimes(n):
  list = [2]
  for x in range(3,n+1,2):
    isPrime = True
    for prime in list:
      if prime < (x ** .5)+1:
        if x % prime == 0:
          isPrime = False
      else:
        break
    if isPrime:
      list.append(x)
  return list

def getPrimeGen(n):
  yield 2
  list = [2]
  for x in range(3,n+1,2):
    if (miller_rabin(x)):
      list.append(x)
      yield x
  yield None

#Instead of getting all the primes in advance I should build this as a generating functions
def isPrime(num):
  return miller_rabin(num)


def printTiming(func):
    def wrapper(*arg):
        t1 = time.time()
        res = func(*arg)
        t2 = time.time()
        print ('%s took %0.3f ms' % (func.__name__, (t2-t1)*1000.0))
        return res
    return wrapper
  
def listPrimeComponents(num):
  if isPrime(num):
    return [num]
  p_list = []
  if (num % 2 == 0):
    p_list = [2]
  while (num % 2 == 0):
    num = int(num / 2)
  for n in range(3,num+1,2):
    if isPrime(num):
      p_list.append(num)
      return p_list
    if isPrime(n):
      isPart = False
      while (num % n == 0):
        isPart = True
        num = int(num / n)
      if isPart:
        p_list.append(n)
  #print (p_list)
  return p_list

  #Returns a list of primes and their counts
#So ((prime1,count1) (prime2, count2))
def countPrimeComponents(num):
  p_list = listPrimeComponents(num)
  components = []
  for prime in p_list:
    count = 0
    while num % prime == 0:
      count +=1
      num = int(num / prime)
    components.append((prime,count))
  return components
