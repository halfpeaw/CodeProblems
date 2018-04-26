using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
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
				if (seen.ContainsKey(c)) {
					lastGood = Math.Max(seen[c] + 1, lastGood);
					longest = Math.Max(current, longest);
					current = counter - (lastGood-1);
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

	}

	
}
