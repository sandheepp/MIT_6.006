
from collections import defaultdict
import queue


class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_edge(self, src, des):
        self.graph[src].append(des)
    
    def TopUtil(self, v, visited, stack):
        # Mark the current node as visited.
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.TopUtil(i, visited, stack)
 
        # Push current vertex to stack which stores result
        stack.append(v)
    
    def Top(self):
        visited = [False]*(max(self.graph)+1)
        stack = []
        for i in range((max(self.graph)+1)):
            if visited[i]== False:
                graph.TopUtil(i, visited, stack)

        print(stack[::-1])


graph = Graph()
graph.add_edge(5, 2)
graph.add_edge(5, 0)
graph.add_edge(4, 0)
graph.add_edge(4, 1)
graph.add_edge(2, 3)
graph.add_edge(3, 1)
graph.Top()
