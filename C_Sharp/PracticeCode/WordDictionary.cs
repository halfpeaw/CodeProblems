// https://leetcode.com/problems/add-and-search-word-data-structure-design/description/
using System.Collections.Generic;

public class WordDictionary
{

	public class Node
	{
		public Dictionary<char, Node> children = new Dictionary<char, Node>();
		public char? val;
		public Node(char? val)
		{
			this.val = val;
		}
	}

	public Node root;
	/** Initialize your data structure here. */
	public WordDictionary()
	{
		root = new Node(null);
	}

	/** Adds a word into the data structure. */
	public void AddWord(string word)
	{
		Node loc = this.root;
		Node newLoc;
		foreach (char c in word)
		{
			if (loc.children.TryGetValue(c, out newLoc))
			{
				loc = newLoc;
			}
			else
			{
				newLoc = new Node(c);
				loc.children.Add(c, newLoc);
				loc = newLoc;
			}
		}
		if (!loc.children.ContainsKey('+')) {
			loc.children.Add('+', null);
		}
		

	}

	/** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
	public bool Search(string word)
	{
		return Search(word, root);
	}

	public bool Search(string word, Node cur)
	{
		if (word.Length == 0)
		{
			return cur != null && cur.children.ContainsKey('+');
		}
		for (int i = 0; i < word.Length; i++)
		{
			if (word[i] == '.')
			{
				// This shouldn't be a problem since we just validated we are not on the last character
				string remainder = word.Substring(i + 1);
				bool tempResult = false;
				foreach (var child in cur.children.Values)
				{
					tempResult |= Search(remainder, child);
				}
				return tempResult;
			}
			else if (!cur.children.TryGetValue(word[i], out cur))
			{
				return false;
			}
		}
		return cur != null && cur.children.ContainsKey('+');
	}
}