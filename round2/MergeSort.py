import sys

def MergeSortCall(items):
   print("Sort this {}".format(items))
   result = MergeSort(items, 0, len(items))
   print ("Result: {}".format(result))

def MergeSort(items,start,end):
   midpoint = (start + end)//2
   
   #if array size is of 1 or empty there's no reason to sort it
   if (end-start<=1):
      return items
      
   MergeSort(items, start,midpoint)
   MergeSort(items, midpoint, end)
   print("list: {}, start: {} end: {}, middle: {}".format(items[start:end], start, end, midpoint))
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
   print ("items: {}".format(items))
   return items

if __name__ == "__main__":
   print("Merge Sort")
   items = [1,4,8,2,6,7,0]
   MergeSortCall(items)
   
   items = [1,4,8,2,6,7,0,2,2,2,2,2,2,-1]
   MergeSortCall(items)
   
   items = [1]
   MergeSortCall(items)
   
   items = []
   MergeSortCall(items)

  