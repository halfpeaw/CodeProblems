using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace PracticeCode
{
	public class ListNode
	{
		public int val;
		public ListNode next;
		public ListNode(int x)
		{
			val = x;
		}
	}


	public class TreeNode {
	public int val;
	public TreeNode left;
	public TreeNode right;
	public TreeNode(int x) { val = x; }
	 }
 

	static class Problems
	{
		// https://leetcode.com/problems/path-sum-ii/description/
		public static IList<IList<int>> PathSum(TreeNode root, int sum)
		{
			IList<IList<int>> result = new List<IList<int>>();
			var queue = new List<int>();
			if (root == null) return result;
			HasPathSumRec2(root, sum, 0, queue, result);
			return result;
		}

		// https://leetcode.com/problems/path-sum-ii/description/
		public static void HasPathSumRec2(TreeNode node, int sum, int current, List<int> queue, IList<IList<int>> result)
		{
			current += node.val;
			queue.Add(node.val);
			if (node.left != null)
			{
				HasPathSumRec2(node.left, sum, current, queue, result);
			}

			if (node.right != null)
			{
				HasPathSumRec2(node.right, sum, current, queue, result);
			}

			if (current == sum && node.left == null && node.right == null)
			{
				result.Add(new List<int>(queue));
			}
			
			// This should always be node.val since we do this at every node we visit before returning
			queue.RemoveAt(queue.Count - 1);
			return;
		}

		public static bool HasPathSum(TreeNode root, int sum)
		{
			if (root == null) return false;
			return HasPathSumRec(root, sum, 0);
		}

		public static bool HasPathSumRec(TreeNode node, int sum, int current)
		{
			current += node.val;
			if (node.left != null)
			{
				if (HasPathSumRec(node.left, sum, current)) return true;
			}

			if (node.right != null)
			{
				if (HasPathSumRec(node.right, sum, current)) return true;
			}

			if (current == sum && node.left == null && node.right == null) return true;
			return false;
		}


		// https://leetcode.com/problems/repeated-dna-sequences/description/
		public static IList<string> FindRepeatedDnaSequences(string s)
		{
			var result = new HashSet<string>();
			var allDNA = new Dictionary<string, bool>();

			for (int i = 9; i < s.Length; i++)
			{
				string dna = s.Substring(i - 9, 10);
				if (allDNA.ContainsKey(dna))
				{
					result.Add(dna);
				}
				else
				{
					allDNA[dna] = true;
				}
			}

			return result.ToList();
		}

		// https://leetcode.com/problems/binary-tree-right-side-view/description/
		public static IList<int> RightSideView(TreeNode root)
		{
			IList<int> results = new List<int>();
			var nodes = new Queue<TreeNode>();

			// Deal with first
			if (root == null)
			{
				return results;
			}

			nodes.Enqueue(root);
			while (nodes.Count > 0)
			{
				results.Add(nodes.Last<TreeNode>().val);
				var newNodes = new Queue<TreeNode>();
				while (nodes.Count > 0)
				{
					var node = nodes.Dequeue();
					if (node.left != null)
					{
						newNodes.Enqueue(node.left);
					}
					if (node.right != null)
					{
						newNodes.Enqueue(node.right);
					}
				}
				nodes = newNodes;
			}

			return results;
		}


		// https://leetcode.com/problems/surrounded-regions/description/
		public static void SolveSurroundedBoard(char[,] board)
		{
			int maxW = board.GetLength(0) - 1;
			int maxH = board.GetLength(1) - 1;
			int minW = 0;
			int minH = 0;

			var oldMarked = new Dictionary<int, Dictionary<int, bool>>();
			var potentialMarked = new Dictionary<int, Dictionary<int, bool>>();

			bool outer = true;
			while (minW <= maxW && minH <= maxH )
			{
				
				// Horizontal
				for (int i = minW; i <= maxW; i++)
				{
					AddPotentialMatch(potentialMarked, board, i, minH);
					AddPotentialMatch(potentialMarked, board, i, maxH);
				}

				// Vertical
				for (int j = minH; j <= maxH; j++)
				{
					AddPotentialMatch(potentialMarked, board, minW, j);
					AddPotentialMatch(potentialMarked, board, maxW, j);
				}

				bool success = true;
				while (success)
				{
					success = false;
					foreach (int potentialW in potentialMarked.Keys.ToList())
					{
						foreach (int potentialH in potentialMarked[potentialW].Keys.ToList())
						{
							if (isMatch(oldMarked,  potentialW, potentialH, outer))
							{
								success = true;
								potentialMarked[potentialW].Remove(potentialH);
								if (potentialMarked[potentialW].Count == 0)
								{
									potentialMarked.Remove(potentialW);
								}
							}
						}
					}
				}

				minW++;
				maxW--;
				minH++;
				maxH--;
				outer = false;
			}

			// Set all remaining potential to Xs
			foreach (int potentialW in potentialMarked.Keys)
			{
				foreach (int potentialH in potentialMarked[potentialW].Keys)
				{
					board[potentialW, potentialH] = 'X';
				}
			}
		}

		private static void AddPotentialMatch(Dictionary<int, Dictionary<int, bool>> potential, char[,] board, int w, int h)
		{
			if (board[w, h] == 'O')
			{
				if (!potential.ContainsKey(w))
				{
					potential[w] = new Dictionary<int, bool>();
				}
				potential[w][h] = true;
			}
		}

		// Also updates matches if we find a match
		// Return true on success
		private static bool isMatch(Dictionary<int, Dictionary<int, bool>> matches, int w, int h, bool outer)
		{
			bool success = false;
			if (outer)
			{
				success = true;
			}

			if (matches.ContainsKey(w))
			{
				if (matches[w].ContainsKey(h - 1) || matches[w].ContainsKey(h + 1))
				{
					success = true;
				}
			}
			if (matches.ContainsKey(w - 1))
			{
				if (matches[w - 1].ContainsKey(h))
				{
					success = true;
				}
			}
			if (matches.ContainsKey(w + 1))
			{
				if (matches[w + 1].ContainsKey(h))
				{
					success = true;
				}
			}
			if (success)
			{
				if (!matches.ContainsKey(w))
				{
					matches[w] = new Dictionary<int, bool>();
				}
				matches[w][h] = true;
			}
			return success;
		}

		//https://leetcode.com/problems/search-in-rotated-sorted-array/description/
		public static int Search(int[] nums, int target)
		{
			if (nums.Length == 0) return -1;

			// always need at least two entries for my code
			if (nums.Length == 1)
			{
				return nums[0] == target ? 0 : -1;

			}

			int minFirst = nums[0];
			int AbsoluteMinIndex = 0;
			int start = 0;
			int end = nums.Length;
			int pivot = (start + end) / 2;
			while (true)
			{
				// When we've narrowed down to one entry we must be done
				if (start == end - 1)
				{
					// Make sure our last entry isn't the closest
					if (nums[start] < minFirst)
					{
						AbsoluteMinIndex = start;
					}
					break;
				}
				if (nums[pivot] < minFirst) // Go left if pivot is smaller than minFirst
				{
					AbsoluteMinIndex = pivot;
					end = pivot;
				}
				else // go right if arr[pivot] is greater or equal to our minimum First Value
				{
					start = pivot;
				}
				pivot = (start + end) / 2;
			}
			// At this point I realized C# doesn't have a good way of returning a sub-array without having to do an entire copy which add unnecessary memory cost
			// return target < minFirst ? Array.BinarySearch(arr[AbsoluteMinIndex:], target) : Array.BinarySearch(arr[:AbsoluteMinIndex], target)
			if (target >= nums[AbsoluteMinIndex] && target <= nums[nums.Length - 1])
			{
				return BinarySearch(nums, AbsoluteMinIndex, nums.Length, target);
			}
			else
			{
				return BinarySearch(nums, 0, AbsoluteMinIndex, target);
			}
		}

		public static int BinarySearch(int[] arr, int start, int end, int target)
		{
			if (start >= end)
			{
				return -1;
			}
			if (start < 0 || end < 0 || start >= arr.Length || end > arr.Length)
			{
				return -1;
			}

			int pivot = (start + end) / 2;
			if (arr[pivot] == target)
			{
				return pivot;
			}
			else if (arr[pivot] > target)
			{
				return BinarySearch(arr, start, pivot, target);
			}
			else
			{
				return BinarySearch(arr, pivot+1, end, target);
			}
		}



			// https://leetcode.com/problems/add-binary/description/
			public static string AddBinary(string a, string b)
		{
			string result = String.Empty;
			int i = a.Length - 1;
			int j = b.Length - 1;
			int carry = 0;
			while (i >= 0 || j >= 0 || carry == 1)
			{
				int aVal = 0;
				int bVal = 0;
				if (i >= 0)
				{
					aVal = a[i] - '0';
					i--;
				}
				if (j >= 0)
				{
					bVal = b[j] - '0'; ;
					j--;
				}

				if (aVal + bVal + carry == 3)
				{
					carry = 1;
					result = $"1{result}";
				}
				else if ((aVal + bVal + carry == 2))
				{
					carry = 1;
					result = $"0{result}";
				}
				else if ((aVal + bVal + carry == 1))
				{
					carry = 0;
					result = $"1{result}";
				}
				else
				{
					carry = 0;
					result = $"0{result}";
				}
			}

			return result;
		}

		//https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
		private static int preOrderLoc;
		private static int inOrderLoc;
		public static TreeNode BuildTree(int[] preorder, int[] inorder)
		{

			if (preorder.Length == 0 || inorder.Length == 0)
			{
				return null;
			}
			TreeNode root = new TreeNode(preorder[0]);
			preOrderLoc = 0;
			inOrderLoc = 0;
			validateTree(preorder, inorder, new HashSet<int>() { preorder[0] }, root);
			return root;
		}

		public static void validateTree(int [] preorder, int[] inorder, HashSet<int> seen, TreeNode root )
		{

			if (preOrderLoc+1 >= preorder.Length || inOrderLoc >= preorder.Length)
			{
				return;
			}

			if ((preorder[preOrderLoc] != inorder[inOrderLoc]))
			{
				preOrderLoc++;
				var leftNode = new TreeNode(preorder[preOrderLoc]);
				seen.Add(preorder[preOrderLoc]);
				root.left = leftNode;
				validateTree(preorder, inorder, seen, leftNode);
			}

			if (preOrderLoc + 1 >= preorder.Length || inOrderLoc >= inorder.Length)
			{
				return;
			}

			// Do right stuff
			if (seen.Contains(inorder[inOrderLoc+1]) && root.val != inorder[inOrderLoc+1])
			{
				inOrderLoc++;
				return;
			}

			if (preorder[preOrderLoc] == inorder[inOrderLoc] || root.val == inorder[inOrderLoc])
			{
				if (root.val == inorder[inOrderLoc + 1])
				{
					
				}
				preOrderLoc++;
				inOrderLoc++;
				var rightNode = new TreeNode(preorder[preOrderLoc]);
				seen.Add(preorder[preOrderLoc]);
				root.right = rightNode;
				validateTree(preorder, inorder, seen, rightNode);
			}
		}



		// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
		public static IList<IList<int>> ZigzagLevelOrder(TreeNode root)
		{

			IList<IList<int>> results = new List<IList<int>>();
			if (root == null)
			{
				return results;
			}
			var next = new List<TreeNode>();
			next.Add(root);

			ZigzagLevelOrderRec(next, results, true);
			return results;
		}

		public static void ZigzagLevelOrderRec(IList<TreeNode> current, IList<IList<int>> results, bool leftToRight)
		{
			if (current.Count == 0) return;
			var next = new List<TreeNode>();
			var result = new List<int>();
			foreach (var node in current)
			{
				result.Add(node.val);
				if (node.left != null)
				{
					next.Add(node.left);
				}
				if (node.right != null)
				{
					next.Add(node.right);
				}
			}
			if (!leftToRight)
			{
				result.Reverse();
			}
			results.Add(result);

			ZigzagLevelOrderRec(next, results, !leftToRight);
		}

		// https://leetcode.com/problems/search-a-2d-matrix/description/
		public static bool SearchMatrix(int[,] matrix, int target)
		{
			if (matrix.Length == 0) return false;
			int midRow = matrix.GetLength(0) / 2;
			int bottom = 0;
			int top = matrix.GetLength(0) - 1;

			while (true)
			{
				if (target >= matrix[midRow, 0])
				{
					// Bounded or top
					if ((midRow <= top - 1 && target < matrix[midRow+1,0]) || midRow == top)
					{
						break;
					}
					bottom = midRow+1;
					midRow = (bottom + top) / 2;
				}
				else
				{
					// bounded or bottom
					if (midRow == bottom)
					{
						if (target < matrix[midRow, 0])
						{
							return false;
						}
						break; 
					}
					if ((midRow >= bottom + 1 && target > matrix[midRow - 1, 0]))
					{
						midRow--;
						break;
					}
					top = midRow;
					midRow = (bottom + top) / 2;
				}
			}

			int midColumn = matrix.GetLength(1) / 2;
			bottom = 0;
			top = matrix.GetLength(1) - 1;

			while (true)
			{
				if (target == matrix[midRow, midColumn])
				{
					return true;
				}
				else if (target > matrix[midRow, midColumn])
				{

					if (midColumn == top)
					{
						return false;
					}
					bottom = midColumn + 1;
					midColumn = (bottom + top) / 2;
				}
				else
				{
					if (midColumn == bottom)
					{
						return false;
					}
					top = midColumn;
					midColumn = (bottom + top) / 2;
				}
			}
		}


		public static IList<string> GenerateParenthesis(int n)
		{
			var result = new List<string>();
			GenerateParenthesisRec(n, 0, 0, "", result);
			return result;
		}

		private static void GenerateParenthesisRec(int n, int open, int closed, string prev, List<string> result)
		{
			if (open == closed && n == open)
			{
				result.Add(prev);
			}
			if (closed > open)
			{
				Console.WriteLine($"Something has gone terribly wrong {prev}");
				return;
			}
			if (closed < open)
			{
				GenerateParenthesisRec(n, open, closed + 1, prev + ")", result);
			}
			if (open < n)
			{
				GenerateParenthesisRec(n, open + 1, closed, prev + "(", result);
			}
		}



			public static int Divide(int dividend, int divisor)
			{
			bool isNegative = (divisor < 0 && dividend > 0) || (divisor > 0 && dividend < 0);
			
			if (divisor == 0 || dividend == 0)
			{
				return 0;
			}

			long top = Math.Abs((long)dividend);
			long bottom = Math.Abs((long)divisor);

			if (bottom > top) return 0;


			int mostSigTop = 0;
			int mostSigBottom = 0;
			long mask = 1;
			while (mask <= top)
			{
				mask = mask << 1;
				mostSigTop++;
			}

			mask = 1;
			while (mask <= bottom)
			{
				mask = mask << 1;
				mostSigBottom++;
			}
			int result = 0;

			long bottomShift = bottom << (mostSigTop - mostSigBottom);

			while (bottomShift >= bottom)
			{
				if (top >= bottomShift)
				{
					top = top - bottomShift;
					result = (result << 1) + 1;

				}
				else
				{
					result = result << 1;
				}
				bottomShift = bottomShift >> 1;
			}
			if (result == int.MinValue && !isNegative)
			{
				result = int.MaxValue;
			}

			return isNegative ? -result : result; 
		}

		public static ListNode SwapPairs(ListNode head)
		{
			if (head == null || head.next == null)
			{
				return head;
			}

			ListNode first = head;
			ListNode second = head.next;
			ListNode third = second.next;

			first.next = third;
			second.next = first;
			ListNode orgin = second;
			ListNode prev = first;

			while (third != null && third.next != null)
			{
				first = third;
				second = third.next;
				third = third.next.next;

				// swap
				first.next = third;
				second.next = first;

				// conect old value
				prev.next = second;
				prev = first;
			}

			return orgin;
		}

		// https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
		private static string[] letters = new string[] { " ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" }; // pos 0,1 never used

		public static IList<string> LetterCombinations(string digits)
		{
			if (digits.Length == 0)
			{
				return new List<string>();
			}
			return LetterCombinationsRec(digits, "");
		}

		public static IList<string> LetterCombinationsRec(string digits, string current)
		{
			if (digits.Length == 0)
			{
				return new List<string>() { current };
			}
			var result = new List<string>();

			int loc = Convert.ToInt32(digits[0]) - 48;
			foreach (char c in letters[loc])
			{
				result.AddRange(LetterCombinationsRec(digits.Substring(1), current + c));
			}

			return result;
		}

		// https://leetcode.com/contest/weekly-contest-90/problems/score-of-parentheses/
		public static int ScoreOfParenthesesRec(string S)
		{
			if (S.Length == 0 || S.Length == 1)
			{
				return 0;
			}
			List<string> subs = new List<string>();

			for (int i = 0; i < S.Length; i++)
			{
				int open = 1;
				if (S[i] != '(')
				{
					Console.WriteLine("Something went wrong at " + i);
				}
				int closed = 0;
				int j = i;
				while (open != closed && j < S.Length)
				{
					j++;
					if (S[j] == '(')
					{
						open++;
					}
					else // ')'
					{
						closed++;
					}
					
				}
				if (j >= S.Length)
				{
					Console.WriteLine("Something went wrong at " + i);
				}
				string item = S.Substring(i, (j - i) + 1);
				subs.Add(item);
				i = j;
			}

			int total = 0;
			foreach (var item in subs)
			{
				if (item.Length == 2)
				{
					total += 1;
				}
				else
				{
					total += 2 * ScoreOfParenthesesRec(item.Substring(1,item.Length-2));
				}
			}
			return total;
		}

		public static bool BuddyStrings(string A, string B)
		{
			if (A.Length != B.Length)
			{
				return false;
			}

			int mismatch = 0;
			int first = -1;
			int second = -1;
			int[] seen = new int[26];
			for (int i = 0; i < A.Length; i++)
			{
				if (mismatch > 2)
				{
					return false;
				}
				if (A[i] != B[i])
				{
					mismatch++;
					if (mismatch == 1)
					{
						first = i;
					}
					else
					{
						second = i;
					}
				}
				else
				{
					seen[A[i] - 97]++;
				}
			}

			if ((mismatch == 2 && A[first] == B[second] && A[second] == B[first]) || (seen.Any(x => x > 1) && mismatch == 0))
			{
				return true;
			}
			return false;
		}


		public static bool ThreeSumContains(int a, int b, int c, IList<IList<int>> result)
		{
			return result.Any(m => m[0] == a && m[1] == b && m[2] == c); 
		}
		public static bool ThreeSumContains(int[] sorted, IList<IList<int>> result)
		{
			return result.Any(m => m[0] == sorted[0] && m[1] == sorted[1] && m[2] == sorted[2]);
		}

		public static IList<IList<int>> ThreeSum(int[] nums)
		{
			IList<IList<int>> result = new List<IList<int>>();
			Array.Sort(nums);
			for (int i = 0; i < nums.Length; i++)
			{
				int j = i + 1;
				int k = nums.Length - 1;
				while (j < k)
				{
					double a = nums[i];
					double b = nums[j];
					double c = nums[k];
					if (b + c == -a)
					{
						if (!ThreeSumContains(nums[i], nums[j], nums[k], result))
						{
							result.Add(new List<int>() { nums[i], nums[j], nums[k] });
						}
						j++;
					}
					else if (b + c > -a) 
					{
						k--;
					}
					else if (b + c < -a)
					{
						j++;
					}
				}
			}
			return result;
		}

		public static IList<IList<int>> ThreeSum2(int[] nums)
		{
			IList<IList<int>> result = new List<IList<int>>();
			for (int i = 0; i < nums.Length; i++)
			{
				int iVal = -nums[i];
				var dict = new Dictionary<double, int>();
				for (int j = i+1; j < nums.Length; j++)
				{
					
					if (dict.ContainsKey(iVal - nums[j]))
					{
						dict[iVal - nums[j]] += 1;
					}
					else
					{
						dict[iVal - nums[j]] = 1;
					}
				}

				for (int j = i + 1; j < nums.Length; j++)
				{
					if (dict.ContainsKey(nums[j]))
					{
						if (2 * nums[j] != iVal || dict[nums[j]] > 1 )
						{
							var sortedArray = new int[] { nums[i], nums[j], iVal - nums[j] };
							Array.Sort(sortedArray);
							if (!ThreeSumContains(sortedArray, result))
							{
								result.Add(sortedArray);
							}
						}
					}
				}
			}
			return result;
		}



		public static HashSet<HashSet<int>> Combos(HashSet<int> items)
		{
			var result = new HashSet<HashSet<int>>();
			CombosRec(items, ref result);
			return result;
		}

		public static  void CombosRec(HashSet<int> items, ref HashSet<HashSet<int>> result)
		{
			if (result.Contains(items))
			{
				return;
			}
			if (items.Count == 0)
			{
				return;
			}
			result.Add(items);
			foreach (int item in items)
			{
				var newItems = new HashSet<int>(items);
				newItems.Remove(item);
				CombosRec(newItems, ref result);
			}
		}



			// https://leetcode.com/problems/merge-k-sorted-lists/description/
			// TODO: Reimplement with priority queue
			public static int? findNode(ListNode[] lists)
		{
			if (lists.Length == 0)
			{
				return null;
			}

			int min = -1;
			for (int i = 0; i< lists.Length; i++)
			{
				if (lists[i] == null)
				{
					continue;
				}

				if (min == -1)
				{
					min = i;
				}
				else if (lists[i].val < lists[min].val)
				{
					min = i;
				}
			}
			if (min == -1)
			{
				return null;
			}
			int result = lists[min].val;
			lists[min] = lists[min].next;
			return result;
		}

		public static ListNode MergeKLists(ListNode[] lists)
		{
			ListNode pointer = null;
			ListNode first = null;

			var node = findNode(lists);
			while (node != null)
			{
				
				if (first == null)
				{
					first = new ListNode(node.Value);
					pointer = first;
				}
				else
				{
					pointer.next = new ListNode(node.Value);
					pointer = pointer.next;
				}
				node = findNode(lists);
			}
			return first;
		}

		public static bool IsMatch(string s, string p)
		{
			var past = new HashSet<string>();
			return IsMatchRec(s, p, past);
		}

		public static bool IsMatchRec(string s, string p, HashSet<string> past)
		{
			if (past.Contains($"{s}:{p}"))
			{
				return false;
			}
			else
			{
				past.Add($"{s}:{p}");
			}

			if (p.Length == 0 && s.Length == 0)
			{
				return true;
			}
			if (p.Length == 0)
			{
				return false;
			}

			bool many = false;
			char reg = p[0];
			if (p.Length > 1)
			{
				if (p[1] == '*')
				{
					many = true;
				}
			}

			if (many)
			{
				if (IsMatchRec(s, p.Substring(2), past))
				{
					return true;
				}

			}

			if (s.Length > 0 && (s[0] == reg || reg == '.'))
			{
				if (many)
				{
					if (IsMatchRec(s.Substring(1), p, past))
					{
						return true;
					}
					if (IsMatchRec(s.Substring(1), p.Substring(2), past))
					{
						return true;
					}
						
				}
				else
				{
					if (IsMatchRec(s.Substring(1), p.Substring(1), past))
					{
						return true;
					}
				}
			}

			return false;
		}

		//https://leetcode.com/problems/container-with-most-water/description/
		public static  int MaxArea(int[] height)
		{
			int i = 0;
			int j = height.Length - 1;
			int max = 0;
			while (i < j)
			{
				max = Math.Max(max, Math.Min(height[i], height[j]) * (j - i));
				if (height[j] < height[i])
				{
					j--;
				}
				else
				{
					i++;
				}
			}
			return max;
		}

		/// <summary>
		/// https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
		/// </summary>
		/// <param name="s"></param>
		/// <returns></returns>
		public static int LengthOfLongestSubstring(string s)
		{
			var seen = new Dictionary<char, int>();
			int longest = 0;
			int counter = 0;
			int lastGood = 0;
			int current = 0;
			foreach (char c in s)
			{
				if (seen.ContainsKey(c))
				{
					lastGood = Math.Max(seen[c] + 1, lastGood);
					longest = Math.Max(current, longest);
					current = counter - (lastGood - 1);
				}
				else
				{
					current++;
				}
				seen[c] = counter;
				counter++;
			}
			longest = Math.Max(current, longest);
			return longest;
		}

		#region AddTwoNumbers
		public static ListNode AddTwoNumbers(ListNode l1, ListNode l2)
		{
			return AddTwoNumbersRec(0, l1, l2);
		}

		public static ListNode AddTwoNumbersRec(int carry, ListNode l1, ListNode l2)
		{
			if (l1 == null && l2 == null && carry == 0)
			{
				return null;
			}
			int val = 0;
			val += l1 == null ? 0 : l1.val;
			val += l2 == null ? 0 : l2.val;
			val += carry;
			carry = val > 9 ? 1 : 0;
			val = val % 10;
			ListNode final = new ListNode(val);
			final.next = AddTwoNumbersRec(carry, l1 == null ? null : l1.next, l2 == null ? null : l2.next);
			return final;
		}
		#endregion

		public static int[] TwoSum(int[] nums, int target)
		{
			var dict = new Dictionary<int, List<int>>();

			for (int i = 0; i < nums.Length; i++)
			{
				if (dict.TryGetValue(nums[i], out List<int> loc))
				{
					dict[nums[i]].Add(i);
				}
				else
				{
					dict[nums[i]] = new List<int>() { i };
				}
			}

			for (int i = 0; i < nums.Length; i++)
			{
				if (dict.ContainsKey(target - nums[i]))
				{
					if (target - nums[i] == nums[i])
					{
						if (dict[nums[i]].Count > 1)
						{
							var locs = dict[nums[i]];
							return new int[] { locs[0], locs[1] };
						}
						else
						{
							continue;
						}

					}
					else
					{
						var locs = dict[target - nums[i]];
						return new int[] { i, locs[0] };
					}
				}
			}

			return new[] { -1, -1 };
		}


		public static string LongestPalindrome(string s)
		{
			string longest = "";
			for (int i = 0; i < s.Length; i++)
			{
				// Odd Check
				int down = i;
				int up = i;
				int tempLength = 0;
				int start = i;
				while (down >= 0 && up < s.Length && s[down] == s[up])
				{
					tempLength = (up - down) + 1;
					start = down;
					down--;
					up++;
				}
				if (tempLength > longest.Length)
				{
					longest = s.Substring(start, tempLength);
				}

				// Even Check
				down = i;
				up = i + 1;
				tempLength = 0;
				start = i;
				while (down >= 0 && up < s.Length && s[down] == s[up])
				{
					tempLength = (up - down) + 1;
					start = down;
					down--;
					up++;
				}
				if (tempLength > longest.Length)
				{
					longest = s.Substring(start, tempLength);
				}
			}
			return longest;
		}

		public static string DiagWords(string s, int numRows)
		{
			if (numRows <= 1)
			{
				return s;
			}
			string result = "";
			List<char>[] rows = new List<char>[numRows];

			for (int i = 0; i < rows.Length; i++)
			{
				rows[i] = new List<char>();
			}

			int row = 0;
			bool isDown = true;
			for (int i = 0; i < s.Length; i++)
			{
				rows[row].Add(s[i]);
				if (isDown && row < numRows - 1)
				{
					row++;
				}
				else if (isDown && row == numRows - 1)
				{
					isDown = false;
					row--;
				}
				else if (!isDown && row == 0)
				{
					row++;
					isDown = true;
				}
				else if (!isDown && row > 0)
				{
					row--;
				}
				else
				{
					Debug.WriteLine("Something went wrong");
				}
			}

			foreach (var list in rows)
			{
				result += new string(list.ToArray());
			}
			return result;
		}

		public static IList<IList<int>> LargeGroupPositions(string S)
		{
			var result = new List<IList<int>>();

			char lastSeen = '\0';
			int size = 0;
			int start = 0;
			for (int i = 0; i < S.Length; i++)
			{
				if (lastSeen == S[i])
				{
					size++;
				}
				else
				{
					if (size >= 3)
					{
						result.Add(new List<int> { start, i - 1 });
					}
					size = 1;
					lastSeen = S[i];
					start = i;
				}
			}
			// One last check
			if (size >= 3)
			{
				result.Add(new List<int> { start, S.Length - 1 });
			}
			return result;
		}

		public static string MaskPII(string S)
		{
			// Email
			if (S.Contains("@"))
			{
				S = S.ToLower();
				string pattern = @"([a-zA-Z])([a-zA-Z]*)([a-zA-Z])(@[a-zA-Z]{2,}\.[a-zA-Z]{2,})";
				var m = Regex.Match(S, pattern);
				if (m.Success)
				{
					return $"{m.Groups[1].Value}*****{m.Groups[3].Value}{m.Groups[4].Value}";
				}
			}
			// Phone
			else
			{
				// THis could be done sooooo much better but was under time crunch
				string pattern = @"([^\D]+)";
				var m = Regex.Matches(S, pattern);
				string result = "";
				foreach (Match match in m)
				{
					result += match.Groups[1].Value;
				}
				if (result.Length == 10)
				{
					return $"***-***-{result.Substring(result.Length - 4)}";
				}
				else if (result.Length > 10)
				{
					string code = "+";
					int country = result.Length - 10;
					for (int i = 0; i < country; i++)
					{
						code += "*";
					}
					return $"{code}-***-***-{result.Substring(result.Length - 4)}";
				}
			}
			return "";
		}

	// Actual Answer
	// int consecutiveNumbersSum(int N)
	// {
	// 	int ans = 0;
	// 	for (int i = 2; i <= sqrt(2 * N); i++)
	// 		if ((2 * N - i * (i - 1)) % (2 * i) == 0) ans++;
	// 	return ans + 1;
	// }

	//https://leetcode.com/problems/consecutive-numbers-sum/submissions/1
	public static int ConsecutiveNumbersSum(int N)
		{
			int count = 1;
			if (N == 1 || N == 2)
			{
				return 1;
			}
			int high = (N / 2) + 1;
			for (int i = 1; (((long)N / i) * ((N / i) + 1)) / 2 >= N; i++)
			{
				for (long j = N/(i+1); j < N/i; j++)
				{
					long total = (j * (j + 1)) / 2;
					
					int index = BinarySumSearch(0, high, total - N);
					if (index >= 0)
					{
						// Debug.WriteLine($"{j} - {index}: Div {(double)N/j}");
						count++;
					}
				}
				
			}

			return count;
		}

		public static int BinarySumSearch(int low, int high, long target)
		{
			if (high >= low)
			{
				int mid = low + ((high - low) / 2);
				long sum = ((long)mid * ((long)mid + 1)) / 2;
				if ( sum == target)
				{
					return mid;
				}

				if (sum > target)
				{
					return BinarySumSearch(low, mid - 1, target);
				}
				else
				{
					return BinarySumSearch(mid + 1, high, target);
				}
					
			}
			return -1;
		}

		public static ListNode convertListNode(int[] ints)
		{
			if (ints.Length == 0)
			{
				return null;
			}
			ListNode first = null;
			ListNode pointer = null;

			foreach (int i in ints)
			{

				if (first == null)
				{
					first = new ListNode(i);
					pointer = first;
				}
				else
				{
					pointer.next = new ListNode(i);
					pointer = pointer.next;
				}
			}
			return first;
		}
	}
}
