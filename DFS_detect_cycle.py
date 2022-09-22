
from collections import defaultdict
from itertools import cycle
import queue


class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_edge(self, src, des):
        self.graph[src].append(des)
    
    def CycleUtil(self, v, visited, stack):
        visited[v] = True
        stack[v] = True
        for neighbour in self.graph[v]:
            if visited[v] == False:
                if self.CycleUtil(neighbour, visited, stack) == True:
                    return True
            elif stack[v]== True:
                return True
        stack[v] = False
    
    def Cycle(self):
        visited = [False]*(max(self.graph)+1)
        stack = [False]*(max(self.graph)+1)

        for neighbour in range(max(self.graph)+1):
            if visited[neighbour] == False:
                if self.CycleUtil(neighbour, visited, stack) == True:
                    return True
        return False

graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)
print(graph.Cycle())
