/*
383. Ransom Note
https://leetcode.com/problems/ransom-note/

Given an arbitrary ransom note string and another string containing letters from all the magazines,
write a function that will return true if the ransom note can be constructed from the magazines ;
otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
*/
function canConstruct(ransomNote: string, magazine: string): boolean {
    let book: Map<string, number> = new Map()
    for (let c of magazine) {
        let i = book.has(c) ? book.get(c) : 0
        book.set(c, i!+1)
    }

    for (let c of ransomNote) {
        let i = book.has(c) ? book.get(c) : 0
        if (i === 0) {
            return false
        }
        book.set(c, i!-1)
    }

    return true
}
