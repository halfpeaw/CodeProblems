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
def getSumFast(n):
  total = 0
  gen = sieveGen()
  for prime in gen:
    if prime > n:
      print(total)
      return total
    #total += getS(prime)
    total += S(prime)
  print(total)
  return total

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
#Euler Totient Phi(P) is all numbers relatively prime to P since P is prime its P - 1
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

#An answer I found online taking advantage of the reduce williams theory about 8x faster than mine.   See their description below
#Yes. A simple way. -3 == kp-3 (mod p) for any k. As p and 8 are coprime, we can divide by 8 
#(multiply by modInv(8,p)) -3/8 == (kp-3)/8 (mod p). Now for given p, what is the smallest k>0 
#to have (kp-3) being divisible by 8. Since p*p==1 (mod 8) for every prime >2, also 3p*p==3 (mod 8), so smallest such k is k=3p%8.
#
#To complete the presentation, I just slowly repeat, what all of you already said, how to arrive at -3/8 (mod p)...
# 
#In (mod p) we calculate (p-1)! = p-1, (p-2)! = 1, (p-3)! = 1/(p-2), (p-4)! = 1/(p-2)/(p-3), (p-5)! = 1/(p-2)/(p-3)/(p-4).
# Now 1/(p-k) = - 1/k, because 1/(p-k) = (p-k)^(p-2) = (-k)^(p-2) = (-1)^(p-2)*k^(p-2) = - k^(p-2) = - 1/k. 
#
#So S(p) = p-1 + 1 - 1/2 + 1/6 - 1/24 = -3/8. (These basic transformations are all valid in (mod p) as p and 2 and 3 are coprime.) Nice problem.
def S(p):
  k = 3*p % 8
  return (k*p - 3) // 8
  
#Stole this generator when creating primes > 10^6 my normal prime gen gets to burdensome
#Could just steal a pre made library but generating primes seems important and didn't want to optimize away. 
#Additionally wanted my code to not be dependent on non-native libraries 
#This sieve is customized to skip 2,3
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
  print("My Answer...")
  getSum(10**8)
  print("Best Answer I found...")
  getSumFast(10**8)
