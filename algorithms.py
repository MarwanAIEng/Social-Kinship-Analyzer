from collections import deque


def bfs_social(graph, start, goal):

    queue= deque([[start]])
    
    visited={start}
    
    while queue:
        path = queue.popleft()
        
        if path[-1] == goal: 

            return path 
        
        for friend in graph.get(path[-1], []):
            if friend not in visited:
                visited.add(friend)
                queue.append(path + [friend])
    return None

def dfs_social(graph, start, goal, visited=None, path=None):
    if visited is None: 
        visited  = set()
        path= [start]
    if start == goal: return path
    
    visited.add(start)
    for friend in graph.get(start, []):

        if friend not in visited:

            result = dfs_social(graph, friend, goal, visited, path + [friend])
            if result:
              
              return  result
