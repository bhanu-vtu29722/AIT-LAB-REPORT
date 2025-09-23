from collections import deque
class Graph:
    def __init__(self):
        self.adj_list = {}
        self.visited = set()
    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    def bfs_recursive(self, queue):
        if not queue:
            return
        current = queue.popleft()
        print(current, end=" ")
        for neighbour in self.adj_list[current]:
            if neighbour not in self.visited:
                self.visited.add(neighbour)
                queue.append(neighbour)
        self.bfs_recursive(queue)
    def bfs(self, start):
        self.visited = set()
        queue = deque()
        self.visited.add(start)
        queue.append(start)
        print("bfs traversal")
        self.bfs_recursive(queue)
g = Graph()
g.add_edge('1', '2')
g.add_edge('1', '3')
g.add_edge('2', '4')
g.add_edge('2', '5')
g.add_edge('3', '6')
g.bfs('1')
