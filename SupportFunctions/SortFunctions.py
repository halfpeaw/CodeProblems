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

@EulerSupport.printTiming
def MergeSortCall(nums):
  return MergeSort(nums)

#O(n log n) complexity
#Basically break down the big list in to lots of smaller lists a half at a time and then merge them together
#Which becomes trivial when they are ordered.
#I wonder if there's a way I can skip the breaking down step and just start off with individual parts.  
def MergeSort(nums):
  if len(nums) <= 1:
    return nums
  left = []
  right = []
  if len(nums) % 2 == 0:
    middle = int(len(nums)/2)
  else:
    middle = int((len(nums) - 1) / 2)
  for i in range(0,middle):
    left.append(nums[i])
  for i in range(middle, len(nums)):
    right.append(nums[i])
  left = MergeSort(left)
  right = MergeSort(right)
  #Merge the sublists returned from the MergeSort
  #Return the resulting merge sublists
  return Merge(left,right)

#Left and Right are sorted going in to this function
#Since the lists are sorted its an N operation to bring them back together.
def Merge(left,right):
  result = []
  while len(left) > 0 or len(right) > 0: 
    if len(left) > 0 and len(right) > 0:
      if left[0] <= right[0]:
        result.append(left[0])
        left = left[1:]
      else:
        result.append(right[0])
        right = right[1:]
    elif len(left) > 0:
      result.append(left[0])
      left = left[1:]
    elif len(right) > 0:
      result.append(right[0])
      right = right[1:]
  return result
  

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
  nums = [2,4,4,6,1,7,9,8,9,1,0,11]*250
  MergeSortCall(nums)
  nums = [2,4,4,6,1,7,9,8,9,1,0,11]*250
  radixSort(nums)
  nums = [2,4,4,6,1,7,9,8,9,1,0,11]*250
  PythonSort(nums)
  
  
  