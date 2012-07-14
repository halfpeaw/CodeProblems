import sys
import time
sys.path.append("../SupportFunctions/")
import EulerSupport
print (time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
result = EulerSupport.getPrimes(103)
print(len(result))
print(result[-3:])
print (time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
result = EulerSupport.getPrimes(1000)
print(len(result))
print(result[-3:])
print (time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
print(EulerSupport.isPrime(17))
print(EulerSupport.miller_rabin(19))
print (time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
print (1066340417491710595814572169)
print(EulerSupport.miller_rabin( 10663404174917))
print (time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
print(EulerSupport.miller_rabin( 1066340417491710595814572171))
print (time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
print(EulerSupport.miller_rabin(  19134702400093278081449423917))
print (time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))

