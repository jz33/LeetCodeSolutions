/*
886. Possible Bipartition
https://leetcode.com/problems/possible-bipartition/

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]

Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false

Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false

Constraints:

1 <= N <= 2000
0 <= dislikes.length <= 10000
dislikes[i].length == 2
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
*/
function possibleBipartition(N: number, dislikes: number[][]): boolean {
    // Build graph matrix. Notice graph[i] can be undefined
    let graph: number[][] = []
    for (const edge of dislikes) {
        let start = edge[0] - 1
        let togo = edge[1] - 1
        if (graph[start] === undefined) {
            graph[start] = [togo]
        }
        else {
            graph[start].push(togo)
        }
        if (graph[togo] === undefined) {
            graph[togo] = [start]
        }
        else {
            graph[togo].push(start)
        }
    }
    
    // Colors of each node, can be undefined / 1 / 0
    let colors: number[] = []
    
    function bfs(node: number): boolean {
        // Assign color to starting node
        colors[node] = 0
        
        let stack: number[] = [node]
        while (stack.length > 0) {
            let newStack: number[] = []
            
            for (const start of stack) {
                let startColor = colors[start]
                let togos = graph[start]
                
                // Notice the start node can have no connections at all
                if (togos != undefined) {
                    for (const togo of togos) {
                        if (colors[togo] === undefined) {
                            colors[togo] = 1 - startColor
                            newStack.push(togo)
                        }
                        else if (colors[togo] + startColor !== 1) {
                            return false
                        }
                    }
                }
            }
            stack = newStack
        }
        return true
    }

    // Notice the graph is not necessarily connected
    for (let i = 0; i < N; ++i) {
        if (colors[i] === undefined) {
            if (!bfs(i)) {
                return false
            }
        }
    }
    return true
};
