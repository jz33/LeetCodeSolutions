/*
886. Possible Bipartition
https://leetcode.com/problems/possible-bipartition/

We want to split a group of n people (labeled from 1 to n) into two groups of any size.
Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi,
return true if it is possible to split everyone into two groups in this way.

Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: The first group has [1,4], and the second group has [2,3].

Example 2:

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Explanation: We need at least 3 groups to divide them. We cannot put them in two groups.

Constraints:
    1 <= n <= 2000
    0 <= dislikes.length <= 104
    dislikes[i].length == 2
    1 <= ai < bi <= n
    All the pairs of dislikes are unique.

*/
function possibleBipartition(n: number, dislikes: number[][]): boolean {
    let dislikeGraph: number[][] = [];
    for (const edge of dislikes) {
        let start = edge[0] - 1;
        let togo = edge[1] - 1;
        dislikeGraph[start] = (dislikeGraph.at(start) ?? []).concat(togo);
        dislikeGraph[togo] = (dislikeGraph.at(togo) ?? []).concat(start);
    }

    // Mark colors on each node:
    // 0: unvisited
    // 1: red
    // -1: blue
    const colors = new Array(n).fill(0);

    for (let start = 0; start < n; start++) {
        if (colors[start] === 0) {
            colors[start] = 1;
            let stack: number[] = [start];
            while (stack.length) {
                const newStack: number[] = [];
                for (const node of stack) {
                    const togos = dislikeGraph[node] ?? [];
                    for (const togo of togos) {
                        if (colors[togo] === 0) {
                            colors[togo] = colors[node] * -1;
                            newStack.push(togo);
                        } else if (colors[togo] + colors[node] !== 0) {
                            return false;
                        }
                    }
                }
                stack = newStack;
            }
        }
    }
    return true;
}

