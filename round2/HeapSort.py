def HeapSort(A):
   #(Put elements of 'a' in heap order, in-place)
    def heapify(A):
        start = (len(A) - 2) // 2
        while start >= 0:
            siftDown(A, start, len(A) - 1)
            start -= 1

   #(Repair the heap whose root element is at index 'start', assuming the heaps rooted at its children are valid)
    def siftDown(A, start, end):
        root = start
        while root * 2 + 1 <= end:
            child = root * 2 + 1
            if child + 1 <= end and A[child] < A[child + 1]:
                child += 1
            if child <= end and A[root] < A[child]:
                A[root], A[child] = A[child], A[root]
                root = child
            else:
                return

    heapify(A)
    end = len(A) - 1
    while end > 0:
        A[end], A[0] = A[0], A[end]
        siftDown(A, 0, end - 1)
        end -= 1


#def HeapSort(a):
#   #Build the heap in array a so that largest value is at the root
#   def heapify(a):
#      start = (len(A) - 2) // 2

if __name__ == '__main__':
    
    T = [13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10] 

    HeapSort(T)
    print(T)