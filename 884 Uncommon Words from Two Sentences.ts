/*
884. Uncommon Words from Two Sentences
https://leetcode.com/problems/uncommon-words-from-two-sentences/

We are given two sentences A and B.  (A sentence is a string of space separated words.
Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]

Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
*/
function buildCounter(A: string): Map<string, number> {
    let ma: Map<string, number> = new Map()
    for (const word of A.split(' ')) {
        let count: number | undefined = ma.get(word)
        if (count === undefined) {
            ma.set(word, 1)
        }
        else {
            ma.set(word, count + 1)
        }
    }
    return ma
}

function getUncommonWords(ca: Map<string, number>, cb: Map<string, number>): string[] {
    let res: string[] = []
    for (const [key, val] of ca.entries()) {
        if (val === 1 && !cb.has(key)) {
            res.push(key)
        }
    }
    return res
}

function uncommonFromSentences(A: string, B: string): string[] {
    let ca = buildCounter(A)
    let cb = buildCounter(B)
    return getUncommonWords(ca, cb).concat(getUncommonWords(cb, ca))
}
