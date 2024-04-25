from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    results = {}
    q = [(0, 0, source)]
    visited = set()
    while q:
        weight, edges, vertex = heappop(q)     
        if vertex in visited:
            continue
        visited.add(vertex)
        results[vertex] = (weight, edges)    
        for neighbor, edge_weight in graph[vertex]:
            if neighbor not in visited:
                newWeight = weight + edge_weight
                newEdges = edges + 1
                heappush(q, (newWeight, newEdges, neighbor))
    
    return results
    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    q = deque([source])
    parents = {source: None} 
    while q:
        cNode = q.popleft()
        for neighbor in graph[cNode]:
            if neighbor not in parents:  
                parents[neighbor] = cNode  
                q.append(neighbor)  
    
    return parents

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    path = []
    current = parents.get(destination)
    while current is not None:
        path.append(current)
        current = parents.get(current)
    return ''.join(path[::-1])

