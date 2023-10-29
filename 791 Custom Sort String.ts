/*
791. Custom Sort String
https://leetcode.com/problems/custom-sort-string/

You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

Example 1:

Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

Example 2:

Input: order = "cbafg", s = "abcd"
Output: "cbad"

Constraints:
    1 <= order.length <= 26
    1 <= s.length <= 200
    order and s consist of lowercase English letters.
    All the characters of order are unique.
*/
// Use custom sort
function customSortString(order: string, target: string): string {
    // Use codePointAt, as charCodeAt only returns [0, 65536]
    const toBaseCode = (char: string): number => {
        return char.codePointAt(0)! - 'a'.codePointAt(0)!;
    };

    // Build a histogram of order
    const ranks: number[] = Array(26).fill(0);
    for (let i = 0; i < order.length; ++i) {
        ranks[toBaseCode(order[i])] = i + 1;
    }

    return target
        .split('')
        .sort((a, b) => ranks[toBaseCode(a)] - ranks[toBaseCode(b)])
        .join('');
}

// Another method using Hashmap, without custom sort
function customSortString(order: string, target: string): string {
    const targetMap = new Map<string, number>();
    for (const char of target) {
        targetMap.set(char, (targetMap.get(char) ?? 0) + 1);
    }

    const result: string[] = [];
    for (const char of order) {
        const count = targetMap.get(char);
        if (count) {
            // count !== undefined && count > 0
            result.push(new Array(count).fill(char).join(''));
            targetMap.set(char, 0);
        }
    }

    Array.from(targetMap.entries()).map((entry) => {
        const [char, count] = entry;
        if (count) {
            result.push(new Array(count).fill(char).join(''));
        }
    });

    return result.join('');
}


