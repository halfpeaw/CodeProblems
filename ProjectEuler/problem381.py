#Problem 381
#For a prime p let S(p) = Sigma((p-k)!) mod(p) for 1  k  5.
#
#For example, if p=7,
#(7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! = 720+120+24+6+2 = 872.
#As 872 mod(7) = 4, S(7) = 4.
#
#It can be verified that SigmaS(p) = 480 for 5 <p <100.
#
#Find S(p) for 5 <= p <= 10**8.

import itertools as it
import math
import sys
sys.path.append("../SupportFunctions/")
import EulerSupport

@EulerSupport.printTiming
def getSum(n):
  total = 0
  gen = sieveGen()
  for prime in gen:
    if prime > n:
      print(total)
      return total
    total += getS(prime)
  print(total)
  return total

#Though this algorithm appears simple it actually took a bit of research to come up with it
#When working with prime modulus  You can solve factorial modulus results via the following equation
#Euler Totient (P) is all numbers relatively prime to P since P is prime its P - 1
#b1 = P-1 (P-1)! % P = P-1
#b2 = 1 (P-2)! % P = 1
#bi+1 = bi*(p-i)^(phi(p) - 1) % p) % p
#Then you add them all up and take mod p of that result.
#Its important that you use Pow with a modulus other wise the a ** b % m is incredibly slow

def getS(p):
  b1 = p-1
  b2 = 1
  total = b1 + b2
  bi = b2
  for i in range (3,5+1):
    bi=(bi*pow((p-i+1),(p-1)-1,p))%p
    total+=bi
  total %= p
  return total

#Stole this generator when creating primes > 10^6 my normal prime gen gets to burdensome
#Could just steal a pre made library but generating primes seems important and didn't want to optimize away.  
#Also this sieve is customized to skip 2,3
def sieveGen( ):
    D = { 9: 3, 25: 5 }
    #yield 2
    #yield 3
    yield 5
    MASK= 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
    MODULOS= frozenset( (1, 7, 11, 13, 17, 19, 23, 29) )

    for q in it.compress(
            it.islice(it.count(7), 0, None, 2),
            it.cycle(MASK)):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = q + 2*p
            while x in D or (x%30) not in MODULOS:
                x += 2*p
            D[x] = p
  
if __name__ == "__main__":
  print("Problem 381")
  print("Last run 360 Seconds")
  #139602943319822
  getSum(10**8)
