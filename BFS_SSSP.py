#Single source shortest path

from asyncio import FastChildWatcher
from dis import dis
from math import inf


def add_edge(adj, src, des ):
    adj[src].append(des)
    adj[des].append(src)


def bfs(adj, no_of_v, src, des, pred, dist):

    queue = []
    visited = [False for i in range(no_of_v)]

    for i in range(no_of_v):
        pred[i] = -1
        dist[i] = inf

    visited[src] = True
    dist[src] = 0
    queue.append(src)

    while(len(queue) != 0):
        u = queue.pop(0)
        for i in range(len(adj[u])):
            if (visited[adj[u][i]] == False):
                visited[adj[u][i]] = True
                dist[adj[u][i]] = dist[u] + 1
                pred[adj[u][i]] = u
                queue.append(adj[u][i])

                if (adj[u][i]) == des:
                    return True
    return False


def print_path(adj, no_of_v, src, des):
    
    pred = [0 for i in range(no_of_v)]
    dist = [0 for i in range(no_of_v)]

    if (bfs( adj, no_of_v, src, des , pred, dist) == False):
        print("Not connected")
    
    path = []
    crawl = des
    path.append(crawl)

    while(pred[crawl] != -1):
        path.append(pred[crawl])
        crawl = pred[crawl] 

    for i in range(len(path)-1,-1,-1):
        print(path[i], " ")


if __name__ == "__main__":
    no_of_v = 8
    adj = [[] for i in range(no_of_v)]
    add_edge(adj, 0, 1);
    add_edge(adj, 0, 3);
    add_edge(adj, 1, 2);
    add_edge(adj, 3, 4);
    add_edge(adj, 3, 7);
    add_edge(adj, 4, 5);
    add_edge(adj, 4, 6);
    add_edge(adj, 4, 7);
    add_edge(adj, 5, 6);
    add_edge(adj, 6, 7);

    src = 0
    des = 7

    print_path(adj, no_of_v, src, des)