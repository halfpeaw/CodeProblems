def fib():
   a, b = 1,1
   yield a
   yield b
   while True:
      a, b = b, a + b
      yield b

#The 12th term, F12, is the first term to contain three digits.
#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
if __name__ == "__main__":
   print("Problem 25")
   count = 0
   for i in fib():
      count+=1
      if len(str(i)) >= 1000:
         print("result {}".format(count))
         break
      #else:
         #print(i)