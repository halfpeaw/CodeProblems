using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PracticeCode
{
	class Program
	{
		static void Main(string[] args)
		{
			
			//var value = Problems.TwoSum(new[] { 3, 2, 4 }, 6);

			ListNode node1 = new ListNode(2);
			node1.next = new ListNode(4);
			node1.next.next = new ListNode(3);

			ListNode node2 = new ListNode(9);
			node2.next = new ListNode(6);
			node2.next.next = new ListNode(4);
			node2.next.next.next = new ListNode(1);

			//var result = Problems.AddTwoNumbers(node1, node2);
			///Problems.LengthOfLongestSubstring("ohomm");

			string input = "abc";
			/*
			Debug.WriteLine($"{input}: {Problems.LongestPalindrome(input)}");
			input = "abcba";
			Debug.WriteLine($"{input}: {Problems.LongestPalindrome(input)}");
			input = "abba";
			Debug.WriteLine($"{input}: {Problems.LongestPalindrome(input)}");
			input = "a";
			Debug.WriteLine($"{input}: {Problems.LongestPalindrome(input)}");
			input = "";
			Debug.WriteLine($"{input}: {Problems.LongestPalindrome(input)}");
			input = "aaaacc";
			Debug.WriteLine($"{input}: {Problems.LongestPalindrome(input)}");
			*/

			input = "PAYPALISHIRING";
			Debug.WriteLine($"{input}: {Problems.DiagWords(input, 3)}");
			input = "PAYPALISHIRING";
			Debug.WriteLine($"{input}: {Problems.DiagWords(input, 4)}");

		}
	}
}
