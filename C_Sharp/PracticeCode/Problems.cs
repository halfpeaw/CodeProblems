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

	static class Problems
	{
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
