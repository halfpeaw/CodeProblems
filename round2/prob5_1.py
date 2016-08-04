#source and insert in to target at i,j (j starts at 0) and i, j is inclusive
def binInsertion(target, source, i, j):
   print("\ntarget: {} source: {}, from {} to {}".format(bin(target), bin(source), i, j))
   # eliminate least signficiant
   if (i < j):
      print("i must be greater than j")
      return target
   source = source >> j
   mask = 1
   # range isn't inclusive so we'll also grab at least one spot
   for offset in range(j,i):
      mask = mask << 1
      mask = mask | 1
   # remove top bits
   source = mask & source
   #print("source is now {}".format(bin(source)))
   mask = mask << j
   # change everythging at specific spot in target to 0
   newMask = target & mask
   target = target ^ newMask
   #print("target is now {}".format(bin(target)))
   source = source << j
   target = target ^ source
   print("result is now {}".format(bin(target)))
   return target
   
   
   

if __name__ == "__main__":
   print("Problem 5_1 binary insertion")
   binInsertion(13,2,1,1)
   binInsertion(12,3,1,1)
   binInsertion(28,3,2,0)
   binInsertion(0,17,2,0)
   binInsertion(2,17,6,0)