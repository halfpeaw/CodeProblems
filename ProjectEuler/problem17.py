text = {}
text[1] = len("one")
text[2] = len("two")
text[3] = len("three")
text[4] = len("four")
text[5] = len("five")
text[6] = len("six")
text[7] = len("seven")
text[8] = len("eight")
text[9] = len("nine")
text[10] = len("ten")
text[11] = len("eleven")
text[12] = len("twelve")
text[13] = len("thirteen")
text[14] = len("fourteen")
text[15] = len("fifteen")
text[16] = len("sixteen")
text[17] = len("seventeen")
text[18] = len("eighteen")
text[19] = len("nineteen")
text[20] = len("twenty")
text[30] = len("thirty")
text[40] = len("forty")
text[50] = len("fifty")
text[60] = len("sixty")
text[70] = len("seventy")
text[80] = len("eighty")
text[90] = len("ninety")
text[100] = len("hundred")
text[1000] = len("thousand")


def countNumbers(low, high):
   print ("Low: {}, High: {}".format(low, high))
   totalCount = 0
   if high >= 10000:
      print("I don't support a high that high")
      return 0
      
   for i in range(low, high+1):
      wordCount = 0
      if (i > 100 and i % 100 != 0):
         wordCount += len("and")
         
      if (i >= 1000):
         wordCount += text[i // 1000]  + text[1000]
         i = i % 1000
      if (i >= 100):
         wordCount += text[i // 100] + text[100]
         i = i % 100
      if (i > 0 and i < 100):
         # special case number
         if i in text:
            wordCount += text[i]
         else:
            wordCount += text[i - (i % 10)] + text[i % 10]
      elif(i == 0):
         #do nothing
         1==1
      else:
         print("something has gone wrong for i: {}".format(i))
      totalCount+=wordCount
      
   print("Total Count: {}\n".format(totalCount))
   return totalCount
         
      
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 
#(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
if __name__ == "__main__":
   print("Project Euler Problem 17")
   print ("Verify text case 1-5 {}".format(countNumbers(1,5)==19))
   print ("Verify text case 998-1000 {}".format(countNumbers(998,1000)== len("onethousand")+len("ninehundredandninetynine")+len("ninehundredandninetyeight")))
   print ("Verify text case 342 {}".format(countNumbers(342,342)== len("threehundredandfortytwo")))
   print ("Verify text case 115 {}".format(countNumbers(115,115)== len("onehundredandfifteen")))
   print ("Verify text case 22 {}".format(countNumbers(22,22)== len("twentytwo")))
   print ("Verify text case 18-21 {}".format(countNumbers(18,21)== len("eighteen")+len("nineteen") + len("twenty")+len("twentyone")))
   print ("Verify text case 9-11 {}".format(countNumbers(9,11)== len("nine")+len("ten")+len("eleven")))
   print ("Verify text case 99-101 {}".format(countNumbers(99,101)== len("ninetynine")+len("onehundred")+len("onehundredandone")))
   print ("Verify text case 990 {}".format(countNumbers(990,990)== len("ninehundredandninety")))
   
   countNumbers(1,1000)
   
   
   