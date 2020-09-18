/*
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters?
How would you adapt your solution to such case?
*/

const base: number = 'a'.charCodeAt(0)

function getHisto(s: string): number[] {
    let arr: number[] = [] // size of 26
    for (let i = 0; i < s.length; ++i) {
        const n: number = s.charCodeAt(i) - base
        arr[n] = (arr[n] === undefined)? 1 : arr[n] + 1
    }
    return arr
}

function isAnagram(s: string, t: string): boolean {
    if (s.length != t.length) {
        return false
    }

    const arr = getHisto(t)
    for (let i = 0; i < s.length; ++i) {
        const n: number = s.charCodeAt(i) - base
        if (arr[n] === undefined || arr[n] === 0) {
            return false
        }
        arr[n] -= 1
    }
    return true
}
