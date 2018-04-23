using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PracticeCode
{
	class Program
	{
		static void Main(string[] args)
		{
			Console.Write("Hello World");
			var value = TwoSum(new[] { 3, 2, 4 }, 6);
		}



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

			for (int i = 0; i < nums.Length; i ++)
			{
				if (dict.ContainsKey(target - nums[i]))
				{
					if (target - nums[i] == nums[i] )
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
