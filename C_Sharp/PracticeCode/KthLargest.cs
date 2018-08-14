using System;
using System.Collections.Generic;

public class KthLargest
{
	private int[] minHeap;
	public KthLargest(int k, int[] nums)
	{
		this.minHeap = new int[k];

		Array.Sort(nums);
		Array.Reverse(nums);

		for (int i = 0; i<k; i++)
		{
			if (i < nums.Length)
			{
				minHeap[i] = nums[i];
			}
			else
			{
				minHeap[i] = int.MinValue;
			}
		}
		
		// Build heap (rearrange array)
		for (int i = (minHeap.Length / 2) - 1; i >= 0; i--)
			Heapify(minHeap, i);

	}

	// To heapify a subtree rooted with node i which is
	// an index in arr[]. n is size of heap
	private void Heapify(int[] arr, int i)
	{
		int smallest = i;  // Initialize largest as root
		int l = 2 * i + 1;  // left = 2*i + 1
		int r = 2 * i + 2;  // right = 2*i + 2

		// If left child is smaller than root
		if (l < arr.Length && arr[l] < arr[smallest])
			smallest = l;

		// If right child is smaller than smallest so far
		if (r < arr.Length && arr[r] < arr[smallest])
			smallest = r;

		// If smallest is not root
		if (smallest != i)
		{
			int swap = arr[i];
			arr[i] = arr[smallest];
			arr[smallest] = swap;

			// Recursively heapify the affected sub-tree
			Heapify(arr, smallest);
		}
	}

	public int Add(int val)
	{
		if (val > minHeap[0])
		{
			minHeap[0] = val;
			Heapify(minHeap, 0);
		}
		if (minHeap[0] == int.MinValue) return -1;
		return minHeap[0]; 
	}
}