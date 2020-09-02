/*
1202. Smallest String With Swaps
https://leetcode.com/problems/smallest-string-with-swaps/

You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.

Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"

Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"

Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"
 

Constraints:

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.
*/
class UnionFind {
    tree: number[]
    
    constructor(nodeCount: number) {
        this.tree = []
        for (let i = 0; i < nodeCount; ++i) {
            this.tree[i] = i
        }
    }

    find(node: number): number {
        let tree = this.tree
        if (tree[node] != node) {
            tree[node] = this.find(tree[node])
        }
        return tree[node]
    }

    union(a: number, b: number) {
        let ra = this.find(a)
        let rb = this.find(b)
        if (ra != rb) {
            this.tree[ra] = rb
        }
    }
};

function smallestStringWithSwaps(s: string, pairs: number[][]): string {
    const size = s.length
    let graph = new UnionFind(size)
    for (const pair of pairs) {
        graph.union(pair[0], pair[1])
    }
    
    let groups: Map<number, string[]> = new Map() // {root : [nodes in char]}
    for (let i = 0; i < size; ++i) {
        let r = graph.find(i)
        
        if (!groups.has(r)) {
            groups.set(r, [])
        }
        groups.get(r)!.push(s[i]) // Use "!" to avoid TS2532 !
    }
    
    // Sort each char group reversely
    for (let nodes of groups.values()) {
        nodes.sort((a, b) => {return a > b ? -1 : b > a ? 1 : 0})
    }
    
    let res: string[] = []
    for (let i = 0; i < size; ++i) {
        let r = graph.find(i)
        res[i] = groups.get(r)!.pop()! // Last "!" to avoid TS2322 !
    }
    
    return res.join('')
};
