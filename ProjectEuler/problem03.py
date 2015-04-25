# Project Euler Problem 3
import sys
sys.path.append("../SupportFunctions/")
import EulerSupport

@EulerSupport.printTiming
def FindLargestPrimeFactor(n):
   print (max(EulerSupport.listPrimeComponents(n)))

if __name__ == "__main__":
   print("Problem 03")
   print("What is the largest prime factor of the number 600851475143 ?")
   FindLargestPrimeFactor(600851475143)