
def QuickSort(l):
   if not isinstance(l, (tuple, dict, list)):
      print("not a list")
      return
   elif (len(l) == 0):
      return([])
   elif (len(l) == 1):
      return(l)
   # Find Pivot
   pivot = l[len(l)-1]
   lowerHalf = list(filter(lambda x : x <= pivot, l[:len(l)-1]))
   upperHalf = list(filter(lambda x : x > pivot, l[:len(l)-1]))
   result = QuickSort(lowerHalf) + [pivot] + QuickSort(upperHalf)
   return result
   

if __name__ == "__main__":
   print ("QuickSort")
   mylist = [1,6,5,2,3]
   print ("start: " + str(mylist))
   print ("result: " + str(QuickSort(mylist)))
   mylist = 1
   print ("start: " + str(mylist))
   print ("result: " + str(QuickSort(mylist)))
   mylist = []
   print ("start: " + str(mylist))
   print ("result: " + str(QuickSort(mylist)))
   
   mylist = [2,2,2,2,2,2]
   print ("start: " + str(mylist))
   print ("result: " + str(QuickSort(mylist)))
   
   mylist = [2,2,2,100,2,-2]
   print ("start: " + str(mylist))
   print ("result: " + str(QuickSort(mylist)))