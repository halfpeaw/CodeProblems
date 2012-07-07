#Problem 34
#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.
#

import sys
sys.path.append("../SupportFunctions/")
import EulerSupport
import math

factList = {"0":1,"1":1,"2":2,"3":6,"4":24,"5":120,"6":720,"7":5040,"8":40320,"9":362880}
#Upper limit of 3,000,000 is arbituary basically can't ever have more than 7*9! just wanted to be safe
#This problem was super easy after solving problem 74.  Used the dictionary for fast look up.
@EulerSupport.printTiming
def findTotal():
  grandTotal = 0
  for num in range(3,3000000):
    total = 0
    for x in str(num):
      total += factList[x]
    if total == num:
      print(num)
      grandTotal += num
  print("Final: %d"%grandTotal)
  

if __name__ == "__main__":
  print ("Problem 34")
  #findTotal took 6509.000 ms
  findTotal()