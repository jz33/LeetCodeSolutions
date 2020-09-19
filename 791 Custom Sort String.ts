/*
791. Custom Sort String
https://leetcode.com/problems/custom-sort-string/

S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously.
We want to permute the characters of T so that they match the order that S was sorted.
More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input: 
S = "cba"
T = "abcd"
Output: "cbad"

Explanation: 
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
 
Note:

S has length at most 26, and no character is repeated in S.
T has length at most 200.
S and T consist of lowercase letters only.
*/
const BaseCharCode: number = 'a'.charCodeAt(0)

function toBaseCode(char: string): number {
    return char.charCodeAt(0) - BaseCharCode
}

function customSortString(S: string, T: string): string {
    let ranks: number[] = []
    for (let i = 0; i < 26; ++i) {
        ranks[i] = 0
    }

    for (let i = 0; i < S.length; ++i) {
        ranks[toBaseCode(S[i])] = i + 1
    }

    let ls: string[] = T.split('').sort(function(a: string, b: string): number {
        return ranks[toBaseCode(a)] - ranks[toBaseCode(b)]
    })

    return ls.join('')
}
