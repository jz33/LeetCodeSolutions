/*
834. Sum of Distances in Tree
https://leetcode.com/problems/sum-of-distances-in-tree/

There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi]
indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances
between the ith node in the tree and all other nodes.

Example 1:

Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.

Example 2:

Input: n = 1, edges = []
Output: [0]

Example 3:

Input: n = 2, edges = [[1,0]]
Output: [1,1]

Constraints:
    1 <= n <= 3 * 104
    edges.length == n - 1
    edges[i].length == 2
    0 <= ai, bi < n
    ai != bi
    The given input represents a valid tree.
*/
/**
 * Calculate the total distance on each node to the root
 */
function getDistanceSum(graph: number[][], root: number): number {
    let totalDistance = 0;
    let distance = 0; // A single distance from root to a node
    let nodes: number[][] = [[root, root]]; // [[node, parent]]
    while (nodes.length) {
        totalDistance += distance * nodes.length;
        const newNodes: number[][] = [];
        for (const [node, parent] of nodes) {
            const children = graph[node].filter((child) => child !== parent);
            for (const child of children) {
                newNodes.push([child, node]);
            }
        }
        distance++;
        nodes = newNodes;
    }
    return totalDistance;
}

/**
 * Total nodes count on each node of a tree.
 */
function getNodesCounts(graph: number[][], root: number): number[] {
    const result: number[] = new Array(graph.length);
    const postorder = (node: number, parent: number): number => {
        let childCount = 1;
        const children = graph[node].filter((child) => child !== parent);
        for (const child of children) {
            childCount += postorder(child, node);
        }
        result[node] = childCount;
        return childCount;
    };
    postorder(root, root);
    return result;
}

function sumOfDistancesInTree(n: number, edges: number[][]): number[] {
    // 1. Build the undirected graph
    const graph: number[][] = new Array(n);
    for (let i = 0; i < n; i++) {
        graph[i] = [];
    }
    for (const edge of edges) {
        const [src, tag] = edge;
        graph[src].push(tag);
        graph[tag].push(src);
    }
    // 2. Set 0 as root.
    // Get total distance sums for 0.
    const result = new Array(n);
    result[0] = getDistanceSum(graph, 0);

    // 3. Calculate total nodes count for each node, including all grand-children and self
    const nodesCounts = getNodesCounts(graph, 0);

    // 4. Lever order traverse on other nodes
    let row: number[][] = graph[0].map((child) => [child, 0]); // [[node, parent]]
    while (row.length) {
        const newRow: number[][] = [];
        for (const [node, parent] of row) {
            // The distance sum on a node is related to its parent's result.
            // Say parent is 0, node is 2. From 0 to 2,
            // the distances on 2 and 2's children nodes are reduced by 1,
            // while the distances on 0 and 0's parents node, other children nodes except 2,
            // are increased by 1.
            result[node] =
                result[parent] - nodesCounts[node] + (n - nodesCounts[node]);

            const children = graph[node].filter((child) => child !== parent);
            for (const child of children) {
                newRow.push([child, node]);
            }
        }
        row = newRow;
    }
    return result;
}
