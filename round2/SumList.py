
def listCount(list, target):
   print("List Count")
   list.sort()
   first = 0
   last = len(list)-1
   while (first < last):
      if (list[first] + list[last] == target):
         print ("{} + {} = {}".format(list[first], list[last], target))
         return True
      elif (list[first] + list[last] > target):
         last = last - 1
      else:
         first = first + 1
   print ("no solution found")
   return False
   
def noSpaceCount(list, target):
   print("No Space restraints")
   numbers = {}
   for val in list:
      if(val in numbers):
         numbers[val] = numbers[val] + 1
      else:
         numbers[val]=1
   for val in list:
      temp = target - val
      if (temp in numbers):
         if (val == temp):
            if(numbers[temp] > 1):
               print("{} + {} = {}".format(val, temp, target))
               return True
         else:
            print("{} + {} = {}".format(val, temp, target))
            return True
   print("No Solution Found")
   return False
         
         


if __name__ == "__main__":
   #list1 = [1,2,3,4]
   #target1 = 7
   #listCount(list1, target1)
   #
   #list1 = [1,1,3,4]
   #target1 = 8
   #listCount(list1, target1)
   #
   #list1 = [1,-2,3,4]
   #target1 = -1
   #listCount(list1, target1)
   #
   #
   #list1 = [1,-2,3,1]
   #target1 = 2
   #listCount(list1, target1)
   
   list = [1,2,3,4]
   target = 7
   noSpaceCount(list, target)
   
   list = [1,1,2,7,4,2,5]
   target = 4
   noSpaceCount(list, target)
   
   list = [0,1]
   target = 0
   noSpaceCount(list, target)