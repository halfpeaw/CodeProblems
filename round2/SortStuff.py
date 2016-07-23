import sys
sys.path.append("../SupportFunctions/")
import EulerSupport

#O(n log n) complexity
#Basically break down the big list in to lots of smaller lists a half at a time and then merge them together
#Which becomes trivial when they are ordered.
def MergeSort(items,start,end):
   midpoint = (start + end)//2
   
   #if array size is of 1 or empty there's no reason to sort it
   if (end-start<=1):
      return items
      
   MergeSort(items, start,midpoint)
   MergeSort(items, midpoint, end)
   #print("list: {}, start: {} end: {}, middle: {}".format(items[start:end], start, end, midpoint))
   left = items[start:midpoint]
   right = items[midpoint:end]
   leftCounter=0
   rightCounter=0
   for i in range(start,end):
      if (rightCounter >= len(right) and leftCounter >= len(left)):
         print("Something terrible has happened");
         sys.exit(0)
      elif(rightCounter >= len(right) or (leftCounter < len(left) and left[leftCounter]<=right[rightCounter])):
         items[i] = left[leftCounter]
         leftCounter+=1
      elif(leftCounter >= len(left) or (rightCounter < len(right) and left[leftCounter]>right[rightCounter])):
         items[i] = right[rightCounter]
         rightCounter+=1
      else:
         print("uh...");
   return items
   
#Quick sort extracts a pivot and builds list recursively based on whats left and right of the pivot points
# O(n log (n))
#Space costraint requires an extra Log N
#Fix by not making recursive this causes problems with python when the list is too large
def QuickSort(l):
   if not isinstance(l, (tuple, dict, list)):
      print("not a list")
      return
   elif (len(l) <= 1):
      return(l)
   # Find Pivot
   pivot = l[len(l)-1]
   lowerHalf = list(filter(lambda x : x <= pivot, l[:len(l)-1]))
   upperHalf = list(filter(lambda x : x > pivot, l[:len(l)-1]))
   result = QuickSort(lowerHalf) + [pivot] + QuickSort(upperHalf)
   return result
   
@EulerSupport.printTiming  
#Check out how fast the built in python sort function works
def PythonSort(nums):
  return sorted(nums)

@EulerSupport.printTiming  
def MergeSortCall(items):
   #print("Sort this {}".format(items))
   items = MergeSort(items, 0, len(items))
   #print ("Result: {}".format(items))
   return items
   
@EulerSupport.printTiming    
def QuickSortCall(items):
   #print ("start: {}".format(items))
   items = QuickSort(items)
   #print ("result: {}".format(items))
   return items
   
if __name__ == "__main__":
   nums = [2,4,4,6,1,7,9,8,9,1,0,11,2**8]*10000
   Expected = PythonSort(nums)
   nums = [2,4,4,6,1,7,9,8,9,1,0,11,2**8]*10000
   QuickResult = QuickSortCall(nums)
   nums = [2,4,4,6,1,7,9,8,9,1,0,11,2**8]*10000
   MergeResult = MergeSortCall(nums)
   print("Quick = {}".format(Expected==QuickResult))
   print("Merge = {}".format(Expected==MergeResult))
   
   
   
   