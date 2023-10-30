/*
249. Group Shifted Strings
https://leetcode.com/problems/group-shifted-strings/

We can shift a string by shifting each of its letters to its successive letter.

    For example, "abc" can be shifted to be "bcd".

We can keep shifting the string to form a sequence.

    For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".

Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

 
Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

Example 2:

Input: strings = ["a"]
Output: [["a"]]

Constraints:

    1 <= strings.length <= 200
    1 <= strings[i].length <= 50
    strings[i] consists of lowercase English letters.
*/
/**
 * Build the hash string 'a...'
 */
function getHash(word: string): string {
    const diff = word.charCodeAt(0) - 'a'.charCodeAt(0);
    return word
        .split('')
        .map((char) => {
            let newCode = char.codePointAt(0)! - diff;
            if (newCode < 'a'.charCodeAt(0)) {
                newCode += 26;
            }
            return String.fromCharCode(newCode);
        })
        .join('');
}

function groupStrings(strings: string[]): string[][] {
    const histogram = new Map<string, string[]>();
    strings.map((word) => {
        const hash = getHash(word);
        histogram.set(hash, (histogram.get(hash) ?? []).concat([word]));
    });
    return Array.from(histogram.values());
}
