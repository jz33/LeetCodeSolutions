'''
444. Sequence Reconstruction
https://leetcode.com/problems/sequence-reconstruction/

Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs.
The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104.
Reconstruction means building a shortest common supersequence of the sequences in seqs
(i.e., a shortest sequence so that all sequences in seqs are subsequences of it).
Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example 1:

Input:
org: [1,2,3], seqs: [[1,2],[1,3]]

Output:
false

Explanation:
[1,2,3] is not the only one sequence that can be reconstructed,
because [1,3,2] is also a valid sequence that can be reconstructed.
Example 2:

Input:
org: [1,2,3], seqs: [[1,2]]

Output:
false

Explanation:
The reconstructed sequence can only be [1,2].
Example 3:

Input:
org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]

Output:
true

Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
Example 4:

Input:
org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]

Output:
true
'''
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        graph = {} # {from : set(togos)}
        for seq in seqs:
            for i in range(len(seq)):
                node = seq[i]
                # Add node
                if node not in graph:
                    graph[node] = set()
                # Add edge
                if i < len(seq) - 1:
                    togo = seq[i+1]
                    graph[node].add(togo)
                
        if len(graph) != len(org):
            return False
        
        # Compute in degrees
        ranks = [0] * (len(graph)+1)
        ranks[0] = -1 # rank[0] not used    
        for togos in graph.values():
            for togo in togos:
                ranks[togo] += 1
                        
        # Build the path one by one
        zeros = [i for i in range(1, len(ranks)) if ranks[i] == 0]
        if len(zeros) != 1:
            return False
        
        curr = zeros[0]
        for _ in range(1, len(graph)):
            next = None
            for togo in graph[curr]:
                ranks[togo] -= 1
                if ranks[togo] == 0:
                    # There should only be 1 "next"
                    if next is not None:
                        return False
                    next = togo
            if not next:
                # No next 0 in degree node
                return False
            curr = next
        return True
