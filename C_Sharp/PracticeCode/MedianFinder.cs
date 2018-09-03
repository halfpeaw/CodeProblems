using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PracticeCode
{
	public class MedianFinder
	{
		private List<int> BottomMaxHeap = new List<int>(); // bottom half
		private List<int> TopMinHeap = new List<int>(); // top half		

		//https://leetcode.com/problems/find-median-from-data-stream/description/
		/** initialize your data structure here. */
		public MedianFinder()
		{

		}

		public void AddNum(int num)
		{
			// Set up bottom half
			if (BottomMaxHeap.Count == 0)
			{
				BottomMaxHeap.Add(num);
				return;
			}

			// Set up TopMinHeap
			if (TopMinHeap.Count == 0)
			{
				// The initial value at bottom is greater than the new number it belongs in the top half 
				if (BottomMaxHeap[0] > num)
				{
					TopMinHeap.Add(BottomMaxHeap[0]);
					BottomMaxHeap[0] = num;
				}
				else
				{
					TopMinHeap.Add(num);
				}
				return;
			}

			if (BottomMaxHeap.Count == TopMinHeap.Count)
			{
				if (num > TopMinHeap[0])
				{
					int swap = TopMinHeap[0];
					TopMinHeap[0] = num;
					num = swap;
					// Since we replaced the top recursively rebalance heap;
					MinHeapify(0);
				}
				BottomMaxHeap.Add(num);
				for (int i = (BottomMaxHeap.Count / 2) - 1; i >= 0; i--)
				{
					MaxHeapify(i);
				}
			}
			else
			{
				if (num < BottomMaxHeap[0])
				{
					int swap = BottomMaxHeap[0];
					BottomMaxHeap[0] = num;
					num = swap;

					// Since we've replaced the top recursively rebalance heap;
					MaxHeapify(0);
				}

				TopMinHeap.Add(num);
				for (int i = (TopMinHeap.Count / 2) - 1; i >= 0; i--)
				{
					MinHeapify(i);
				}
			}
			
		}

		private void MinHeapify(int origin)
		{
			int smallest = origin;
			int left = 2 * origin + 1;
			int right = 2 * origin + 2;

			if (left < TopMinHeap.Count && TopMinHeap[left] < TopMinHeap[smallest])
			{
				smallest = left;
			}
			if (right < TopMinHeap.Count && TopMinHeap[right] < TopMinHeap[smallest])
			{
				smallest = right;
			}

			// see if we need to make a change
			if (smallest != origin)
			{
				int swap = TopMinHeap[origin];
				TopMinHeap[origin] = TopMinHeap[smallest];
				TopMinHeap[smallest] = swap;

				// Recurisively Heapify the affect subtrees
				MinHeapify(smallest);
			}
		}

		private void MaxHeapify(int origin)
		{
			int max = origin;
			int left = 2 * origin + 1;
			int right = 2 * origin + 2;

			if (left < BottomMaxHeap.Count && BottomMaxHeap[left] > BottomMaxHeap[max])
			{
				max = left;
			}

			if (right < BottomMaxHeap.Count && BottomMaxHeap[right] > BottomMaxHeap[max])
			{
				max = right;
			}

			if (max != origin)
			{
				int swap = BottomMaxHeap[origin];
				BottomMaxHeap[origin] = BottomMaxHeap[max];
				BottomMaxHeap[max] = swap;

				MaxHeapify(max);
			}
		}

		public double FindMedian()
		{
			// Min should always be equal or one greater than max
			if (BottomMaxHeap.Count == 0)
			{
				return 0;
			}

			if (BottomMaxHeap.Count == TopMinHeap.Count)
			{
				return ((double)BottomMaxHeap[0] + (double)TopMinHeap[0]) / 2;
			}
			else
			{
				return BottomMaxHeap[0];
			}
		}
	}
}
