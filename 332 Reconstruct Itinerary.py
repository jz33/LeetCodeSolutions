'''
Reconstruct Itinerary
https://leetcode.com/problems/reconstruct-itinerary/
Deep first search
Record visited status on node
'''
def rec(graph,step_total,step_ctr,itinerary):
    if step_ctr == step_total:
        return True
    f = itinerary[-1]
    if f in graph:
        for t in graph[f]:
            if t[1] == False:
                itinerary.append(t[0])
                t[1] = True
                if rec(graph,step_total,step_ctr+1,itinerary):
                    return True
                else:
                    itinerary.pop()
                    t[1] = False
    return False
    
def findItinerary(tickets):
    graph = {} # {from : [[togo,visited]]}
    for f,t in tickets:
        if f not in graph:
            graph[f] = []
        graph[f].append([t,False])
    
    for k in graph.iterkeys():
        graph[k].sort(key = lambda x : x[0])
    
    total = len(tickets)
    itinerary = ['JFK']
    rec(graph,total,0,itinerary)
    return itinerary
