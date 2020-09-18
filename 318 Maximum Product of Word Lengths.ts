/*
318. Maximum Product of Word Lengths
https://leetcode.com/problems/maximum-product-of-word-lengths/

Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where
the two words do not share common letters. You may assume that each word will contain only lower case letters.
If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".

Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".

Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.

Constraints:

    0 <= words.length <= 10^3
    0 <= words[i].length <= 10^3
    words[i] consists only of lowercase English letters.
*/

const base: number = 'a'.charCodeAt(0)

function wordHash(word: string): number {
    let h: number = 0
    for (let i = 0; i < word.length; ++i) {
        let n: number = word.charCodeAt(i) - base
        h = h | (1 << n)
    }
    return h
}

function maxProduct(words: string[]): number {
    let hashArr: number[] = []
    for (const word of words) {
        hashArr.push(wordHash(word))
    }
    
    let maxLen: number = 0
    for (let i = 0; i < hashArr.length; ++i) {
        for (let j = i + 1; j < hashArr.length; ++j) {
            if ((hashArr[i] & hashArr[j]) === 0) {
                maxLen = Math.max(maxLen, words[i].length * words[j].length)
            }
        }
    }
    return maxLen
}
