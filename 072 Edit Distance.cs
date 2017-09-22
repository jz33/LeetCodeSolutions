/*
72 Edit Distance
https://oj.leetcode.com/problems/edit-distance/
http://rosettacode.org/wiki/Levenshtein_distance#C.2B.2B
*/
using System.Linq;

public int MinDistance(string word1, string word2)
{
    int width = word1.Length;
    int height = word2.Length;
    var buf = Enumerable.Range(0, width+1).ToArray();
    for (int i = 0; i < height; i++)
    {
	buf[0] = i + 1;
	var upperLeft = i;
	var left = buf[0];
	for (int j = 0; j < width; j++)
	{
	    var upper = buf[j + 1];
	    if (word2[i] == word1[j])
	    {
		buf[j + 1] = upperLeft;
	    }
	    else
	    {
		buf[j + 1] = new int[] { upperLeft, upper, left }.Min() + 1;
	    }
	    upperLeft = upper;
	    left = buf[j + 1]; 
	}
    }
    return buf[width];
}
