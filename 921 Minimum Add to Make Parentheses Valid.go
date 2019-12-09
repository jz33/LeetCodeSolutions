/*
921. Minimum Add to Make Parentheses Valid
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')',
and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.
*/
func minAddToMakeValid(S string) int {
    /*
    Similar to 1249. Minimum Remove to Make Valid Parentheses
    */
    left := 0 // Number of left brackets
    right := 0 // Number of right brackets
    for _, c := range S {
        if c == '(' {
            left += 1
        } else {
            if left > 0 {
                left -= 1 // If left brackets are remaining, close the parentheses pair
            } else {
                right += 1 // Right brackets are outstanding, added to the total cost
            }
        }
    }
    return left + right
}
