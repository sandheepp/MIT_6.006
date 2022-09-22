
from collections import defaultdict
import queue


class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_edge(self, src, des):
        self.graph[src].append(des)
    
    def DFSUtil(self, src, visited):
        visited.append(src)
        print(src)
        for neighbour in self.graph[src]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
    
    def DFS(self, vertice):
        visited = []
        graph.DFSUtil(vertice, visited)


graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)
graph.DFS(2)
