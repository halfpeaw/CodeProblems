
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


if __name__ == "__main__":
   list1 = [1,2,3,4]
   target1 = 7
   listCount(list1, target1)
   
   list1 = [1,1,3,4]
   target1 = 8
   listCount(list1, target1)
   
   list1 = [1,-2,3,4]
   target1 = -1
   listCount(list1, target1)
   
   
   list1 = [1,-2,3,1]
   target1 = 2
   listCount(list1, target1)