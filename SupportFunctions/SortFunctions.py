import EulerSupport
import math

@EulerSupport.printTiming
#BubbleSort works by looking at two items at a time and then exchanging them if out of order
#Slowly working up the list over and over again untill no changes are required
#O(n^2)
#Space constaint of N
def Bubble(nums):
  swap = True
  while swap:
    swap = False
    for i in range(0,len(nums)-1):
      if nums[i] > nums[i+1]:
        temp = nums[i+1]
        nums[i+1]  = nums[i]
        nums[i] = temp
        swap = True
  return nums


#This function exists so I can do timing without a recursion issue
@EulerSupport.printTiming
def QuickSortCall(num):
  return QuickSort(nums)
#Quick sort extracts a pivot and builds list recursively based on whats left and right of the pivot points
# O(n log (n))
#Space costraint requires an extra Log N
#Fix by not making recursive this causes problems with python when the list is too large
def QuickSort(nums):
  if len(nums) <= 1:
    return nums
  #Figured this way of finding the midpoint was cheaper than using the floor function
  length = len(nums)
  if length % 2 == 0:
    pivotPos = int(length / 2)
  else:
    pivotPos = int((length - 1) / 2)
  less = []
  more = []
  #Extract our pivot point and then del it from our list
  pivot = nums[pivotPos]
  del nums[pivotPos]
  for i in range(0,length-1):
    if nums[i] <= pivot:
      less += [nums[i]]
    else:
      more += [nums[i]]
  return (QuickSort(less) + [pivot] + QuickSort(more))

@EulerSupport.printTiming  
#Check out how fast the built in python sort function works
def PythonSort(nums):
  return sorted(nums)

#Todo
def MergeSort(nums):
  None
  

#Sort by bit, only works when doing positive integers
#Determines greatest in list and use that as our max bit for sorting purposes
#Then recursively solve bit by bit
#O(k*n) where k is how many bits we need to search over.
@EulerSupport.printTiming  
def radixSort(nums):
  biggest = max(nums)
  #Turn to a binary string
  biggest = bin(biggest)[2:]
  #For example if our biggest num is 10 => 1010 then k will be 3 aka 2^3 = 8
  k = len(biggest) - 1 # our range will be k-1 .. 0
  less, greater = radixSplit(nums,k)
  return (less+greater)
  
#This does the recurssion of RadixSort, return when k == 0
#We generate a list based on the current bit we are looking at based on k.  So if Kth bit == 1
#Go to the greater list, else go to the less list
def radixSplit(nums, k):
  less = []
  greater = []
  for num in nums:
    if num & 2**k:
      greater.append(num)
    else:
      less.append(num)
  if k == 0:
    return less, greater
  else:
    lessSmall, lessBig = radixSplit(less,k-1)
    greaterSmall, greaterBig = radixSplit(greater,k-1)
    return (lessSmall + lessBig), (greaterSmall + greaterBig)
  
  
if __name__ == "__main__":
  nums = [2,4,4,6,1,7,9,8,9,1,0,11]*250
  Bubble(nums)
  nums = [2,4,4,6,1,7,9,8,9,1,0,11]*250
  QuickSortCall(nums)
  nums = [2,4,4,6,1,7,9,8,9,1,0,11]*500
  PythonSort(nums)
  nums = [2,4,4,6,1,7,9,8,9,1,11,513]*500
  radixSort(nums)
  
  