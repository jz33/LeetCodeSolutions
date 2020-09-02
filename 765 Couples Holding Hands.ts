/*
765. Couples Holding Hands
https://leetcode.com/problems/couples-holding-hands/

N couples sit in 2N seats arranged in a row and want to hold hands.
We want to know the minimum number of swaps so that every couple is sitting side by side.
A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order,
the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:

Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.

Example 2:

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.
Note:

len(row) is even and in the range of [4, 60].
row is guaranteed to be a permutation of 0...len(row)-1.
*/
class UnionFind {
    tree: number[]
    rootCount: number
    
    constructor(nodeCount: number) {
        this.tree = []
        for (let i = 0; i < nodeCount; ++i) {
            this.tree[i] = i
        }
        this.rootCount = nodeCount
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
            this.rootCount--
        }
    }
};

function minSwapsCouples(row: number[]): number {
    /*
    There are N couples, can seen as N nodes each has a couple id.
    For each pair of seat, union the left people and right people
    by their couple id. If their couple ids are different 
    (aka they are not a couple), union them, because they must
    be involved in swapping. Therefore total swapping needed is 
    N - rootCount.
    */
    const size = row.length
    let graph = new UnionFind(size)
    for (let coupleId = 0; coupleId < size; ++coupleId) {
        let left = row[coupleId * 2]
        let right = row[coupleId * 2 + 1]
        graph.union(Math.floor(left / 2), Math.floor(right / 2))
    }
    return size - graph.rootCount
};
