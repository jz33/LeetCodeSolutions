'''
743. Network Delay Time

There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node,
v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal?
If it is impossible, return -1.

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
'''
INF = float('inf')

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
            
        nodes = [INF] * (N+1) # node id : total time
        nodes[0] = -1 # 0 is not used
        nodes[K] = 0
        queue = collections.deque()
        queue.append(K)
        while queue:
            node = queue.popleft()
            time = nodes[node]
            for togo, weight in graph[node]:
                if time + weight < nodes[togo]:
                    nodes[togo] = time + weight
                    queue.append(togo)
        
        maxTime = max(nodes)
        return -1 if maxTime == INF else maxTime
