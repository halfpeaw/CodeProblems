
# return true if second is one char away
def OneAway(first, second):
   print("\n {} -> {}".format(first, second))
   diffs = 0
   iter1 = 0
   iter2 = 0
   while True:
      spot1 = None
      spot2 = None
      if iter1 >= len(first):
         spot1 = -1
      else:
         spot1 = first[iter1]
      
      if iter2 >= len(second):
         spot2 = -1
      else: 
         spot2 = second[iter2]
         
      if (spot1 != spot2):
         diffs+=1
         #account for deletes/insertions
         if(len(first) > len(second)):
            iter1+=1
         elif(len(second) > len(first)):
            iter2+=1
         #no deletes/grows just different
         else:
            iter1+=1
            iter2+=1
      else:
         iter1+=1
         iter2+=1
      
      if diffs > 1:
         return False
      # we having nothing left to look at
      if spot1 == spot2 == -1:
         return diffs <= 1

# what constitutes unique A->a does whitespace matter? etc
def UniqueChar(words):
   print("\nis {} all unique".format(words))
   dict = {}
   for i in words:
      if i in dict:
         dict[i] += 1
         print("Found Dup in {} it is the {} copy".format(i, dict[i]))
         return False
      else:
         dict[i] = 1
   print("No dup found")
   return True
   
def UniqueCharNoDict(words):
   print("\nis {} all unique".format(words))
   bools = 256*[False]
   for i in words:
      if bools[ord(i)]:
         print("Found Dup: \"{}\"".format(i))
         return False
      else:
         bools[ord(i)] = True
   print("No dup found")
   return True

#TBD string concatenation is slow so you should use a "".join
def compression(words):
   if (words == None or type(words) is not str):
      print ("\nWords not defined properly")
      return
   print("\nCompressing {}".format(words))
   compressed = ""
   i = 0
   while(i < len(words)):
      count = 0
      if (words[i].isdigit()):
         compressed += "+"   
      compressed += words[i]
      # this should always happen at least once since words[i] will always equal the last char we set
      while(i < len(words) and words[i] == compressed[-1]):
         count+=1
         i+=1
      if (compressed[-1].isdigit()):
         if count > 2:
            compressed += "_{}".format(str(count))
         elif (count == 2):
            compressed += compressed[-1]*(count-1) # we already have 1 hence - 1
      elif count > 1:
         compressed += str(count)
   print("compressed: {}".format(compressed))
   return compressed

if __name__ == "__main__":
   print(OneAway("pale", "ple"))
   print(OneAway("", ""))
   print(OneAway("pale", "bake"))
   print(OneAway("pale", "bale"))
   
   
   UniqueChar("Alex")
   UniqueChar(" Alex ")
   UniqueChar("Aalex")
   UniqueChar("AalexA")
   
   UniqueCharNoDict("Alex")
   UniqueCharNoDict(" Alex ")
   UniqueCharNoDict("Aalex")
   UniqueCharNoDict("AalexA")
   
   compression("AAAAAABBBBBBCDEEEEEeeeee")
   compression(1234)
   compression(None)
   compression("AAAAAABBBBBBCDEEEEEeeeee11111111114445alex")
   