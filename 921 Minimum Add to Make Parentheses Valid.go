/*
921. Minimum Add to Make Parentheses Valid
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

A parentheses string is valid if and only if:

    It is the empty string,
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

You are given a parentheses string s. In one move,
you can insert a parenthesis at any position of the string.

    For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or
    a closing parenthesis to be "())))".

Return the minimum number of moves required to make s valid.

Example 1:

Input: s = "())"
Output: 1

Example 2:

Input: s = "((("
Output: 3

Constraints:
    1 <= s.length <= 1000
    s[i] is either '(' or ')'.
*/
func minAddToMakeValid(s string) int {
    /*
    Similar to 1249. Minimum Remove to Make Valid Parentheses
    */
    left := 0 // Number of left brackets
    right := 0 // Number of right brackets
    for _, c := range s {
        if c == '(' {
            left += 1
        } else if left > 0 {
            left -= 1 // If left brackets are remaining, close the parentheses pair
        } else {
            right += 1 // Right brackets are outstanding, added to the total cost
        }
    }
    return left + right
}
