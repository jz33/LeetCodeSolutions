/*
936. Stamping The Sequence
https://leetcode.com/problems/stamping-the-sequence/

You want to form a target string of lowercase letters.

At the beginning, your sequence is target.length '?' marks.  You also have a stamp of lowercase letters.

On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the corresponding letter from the stamp.
You can make up to 10 * target.length turns.

For example, if the initial sequence is "?????", and your stamp is "abc",  then you may make "abc??", "?abc?", "??abc" in the first turn.
(Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)

If the sequence is possible to stamp, then return an array of the index of the left-most letter being stamped at each turn.
If the sequence is not possible to stamp, return an empty array.

For example, if the sequence is "ababc", and the stamp is "abc", then we could return the answer [0, 2],
corresponding to the moves "?????" -> "abc??" -> "ababc".

Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within 10 * target.length moves.
Any answers specifying more than this number of moves will not be accepted.


Example 1:

Input: stamp = "abc", target = "ababc"
Output: [0,2]
([1,0,2] would also be accepted as an answer, as well as some other answers.)

Example 2:

Input: stamp = "abca", target = "aabcaca"
Output: [3,0,1]
 

Note:

1 <= stamp.length <= target.length <= 1000
stamp and target only contain lowercase letters.
*/
function movesToStamp(stamp: string, target: string): number[] {
    if (stamp[0] !== target[0] || stamp[stamp.length - 1] !== target[target.length-1]) {
        return []
    }

    let result: number[] = []
    let targetArr: string[] = target.split('')

    /**
     * If stamp === targetArr[start: start + stamp.length]
     * @param start
     */
    function matched(start: number): boolean {
        for (let i = 0; i < stamp.length; ++i) {
            if (targetArr[start + i] !== '?' && targetArr[start + i] !== stamp[i]) {
                return false
            }
        }
        return true
    }

    function mark(start: number): number {
        let count: number = 0
        for (let i = 0; i < stamp.length; ++i) {
            if (targetArr[start + i] !== '?') {
                targetArr[start + i] = '?'
                count++
            }
        }
        return count
    }

    let markCount: number = 0 // Count of question mark
    let seen: boolean[] = [] // Visited indexes
 
    // Keep looping the target string, find matching,
    // and mark as '?'
    while (markCount < target.length) {
        let newMarkCount: number = 0
        for (let i = 0; i <= target.length - stamp.length; ++i) {
            if (seen[i] === undefined && matched(i)) {
                seen[i] = true
                const count = mark(i)
                if (count > 0) {
                    newMarkCount += count
                    result.push(i)
                }
            }
        }
        if (newMarkCount === 0) {
            return []
        }
        markCount += newMarkCount
    }
    
    return result.reverse()
}
