from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

# Make the adjacency list
    def add_edge(self,u,v):
        self.graph[u].append(v)

    def print_BFS(self,s):
        visited = [False]*(max(self.graph)+1)
        print(self.graph)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s)
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(1,2)
    graph.add_edge(1,3)
    graph.add_edge(2,3)
    graph.add_edge(3,4)
    graph.add_edge(4,5)
    graph.add_edge(5,1)
    graph.print_BFS(1)
    
    