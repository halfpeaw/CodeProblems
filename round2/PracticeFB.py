import functools

def SmallLarge(n):
   if (n == 0):
      print("error")
      return
   i = 1;
   while not(isSet(n, i) and not isSet(n,i-1)):
      i = i+1
   if (2**i > n):
      print("error")
      return
   
   smaller = n | (1 << (i-1))
   smaller = smaller & ~(1 << (i))
   print("From {} {}: {} = {}".format(n, bin(n), smaller, bin(smaller)))
   
   i = 0
   while not (isSet(n,i) and not isSet(n,i+1)):
      i = i+1
   largest = n|(1 << (i+1))
   largest = largest & (~(1 << i))
   print("From {} {}: {} = {}".format(n, bin(n), largest, bin(largest)))
   
   
def isSet(n, offset):
   mask = 1 << offset
   return (n & mask) > 0

def lonelyinteger(b):
    answer = 0
    storage = {}
    for item in b:
        if item in storage:
            storage[item] = 1
        else:
            storage[item] = 0
    for key in storage:
        if storage[key] == 0:
            return key
    return -1

def maxXor(l, r):
  largest = 0
  for i in range(l, r+1):
    for j in range(l, r+1):
        if (i ^ j > largest):
            largest = i ^ j
  print("From {} {}: {} = {}".format(l, r, largest, bin(largest)))
  return largest

#!/bin/python3

#import sys
#size = 256
#a = [0] + [-1]*(size - 1)
#builtTo = 0;
#
#Q = int(input().strip())
#for a0 in range(Q):
#    L,R = input().strip().split(' ')
#    L,R = [int(L),int(R)]
#    
#    # Build more array to new upperbounds
#    while (builtTo <= R):
#        if builtTo >= size:
#            a = a + size*[-1]
#            size = size*2
#        builtTo = builtTo  + 1
#        a[builtTo] = a[builtTo - 1] ^ builtTo
#    
#    sum = a[L]
#    for i in range(L+1,R+1):
#        sum = a[i] ^ sum
#    print(sum)
#            
##!/bin/python3
#
#import sys
#
#Q = int(input().strip())
#for a0 in range(Q):
#    L,R = input().strip().split(' ')
#    L,R = [int(L),int(R)]
#    
#    # Build more array to new upperbounds
#    builtTo = 0
#    current = 0
#    while (builtTo < L):
#        builtTo = builtTo + 1
#        # Current on the right side is one iteration old
#        current = current ^ builtTo 
#        #print ("current0: {}, builtTo {} L: {}".format(current, builtTo, L))
#        
#    sum = current
#    for i in range(L+1,R+1):
#        builtTo = builtTo + 1
#        # Current on the right side is one iteration old
#        current = current ^ builtTo 
#        #print ("current1: {}, builtTo {}".format(current, builtTo))
#        sum = current ^ sum
#    print(sum)

def mycmp(a, b):
    #remove leading 0s
    #for i in range(len(a)):
    #    if a[i] != "0":
    #        a = a[i:]
    #        break
    #    if (i == (len(b)-1)): a = ""
    #for i in range(len(b)):
    #    if b[i] != "0":
    #        b = b[i:]
    #        break
    #    if (i == (len(b)-1)): b = ""
    if (len(a) > len(b)): return 1 
    if (len(b) > len(a)): return -1 
    #if equal length
    for i in range(len(a)):
        if (a[i] > b[i]): return 1 
        if (b[i] > a[i]): return -1 
    # Equal
    return 0

class compare(object):
    def __init__(self, obj, *args):
        self.obj = obj
    def __lt__(self, other):
        return mycmp(self.obj, other.obj) < 0
    def __gt__(self, other):
        return mycmp(self.obj, other.obj) > 0
    def __eq__(self, other):
        return mycmp(self.obj, other.obj) == 0
    def __le__(self, other):
        return mycmp(self.obj, other.obj) <= 0
    def __ge__(self, other):
        return mycmp(self.obj, other.obj) >= 0
    def __ne__(self, other):
        return mycmp(self.obj, other.obj) != 0

#!/bin/python3

#def XorSum(L, R):
#    start = L
#    while (start % 4 != 0):
#        start = start - 1
#    current = start
#    sum = current
#    for i in range (start+1, R+1):
#        current = current ^ i
#        if i < L:
#            #print ("not checking for {} < {}...".format(i, L))
#            continue
#        if i == L:
#            sum = current
#            print ("{} \tat {} for sum: {}".format(current, i, sum))
#            continue
#        sum = sum ^ current
#        print ("{} \tat {} for sum: {}".format(current, i, sum))
#    print(sum)
# 
#def sumVsXor(n):
#   for x in range(0,n+1):
#      if (x+n == n^x):
#         print("{},{}:\n{}\n{}\n{}\n---------------------------------------".format(x,n, getToEight(bin(n)[2:]), getToEight(bin(x)[2:]), getToEight(bin(x+n)[2:])))
#         
#def getToEight(item):
#   while len(item) < 8:
#      item = "0" + item
#   return item
#   
#   
#def findMaxBit(n):
#   i = 0
#   while (2**i < n):
#      i = i + 1
#   return i - 1;
#
#def Combination(binN, i):
#   if (i >= len(binN)):
#         return 1
#   while(binN[i] == "1"):
#      i = i+1
#      if (i >= len(binN)):
#         return 1
#   return 2 * Combination(binN, i+1)
#   
#   
#def CombinationStart(n):
#   binN = bin(n)[2:]
#   i = 0
#   if (n == 0):
#     print("1")
#     return
#   print("Start: " + bin(n)[2:])
#   print("result " + str(Combination(binN, i)))

def findCombos(s, depth):
   print(s)
   total = 0
   if len(s) > 0 and (int(s[0]) > 0):
         total += findCombos(s[1:], depth+1) + depth
   if len(s) > 1 and int(s[0:2]) <= 26 and int(s[0:2]) > 0:
         total += findCombos(s[2:], depth+1) + depth
   print("Total {} depth {}".format(total, depth))
   return total
   
def findSpaces(s):
   total = findCombos(s,1) #in case single character
   for i in range(1, len(s)):
      if i < len(s)-1 and s[i:i+2] == "00":
         print("new iteration")
         total+= findCombos(s[i+2:], 1)
   return total
   
         


if __name__ == "__main__":
   a = ["5", "1", "2"]
   print(sorted(a, key=functools.cmp_to_key(mycmp)))
   #SmallLarge(13)
   #SmallLarge(26)
   #SmallLarge(14)
   #SmallLarge(13948)
   #lonelyinteger([1,2,2,3,3])
   #maxXor(5,6)
   #XorSum(98, 120)
   #current = 0
   #for i in range(1,100):
   #   current = i ^ current
   #   print("current {}\t at {}".format(str(current), str(i)))
   #sumVsXor(100) 
   #CombinationStart(5)
   #CombinationStart(10)
   #CombinationStart(0)
   print(findSpaces("123001"))
   
