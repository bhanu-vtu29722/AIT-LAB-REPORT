class Graph:
    def __init__(self):
        self.adj_list={}
        self.visited=set()
    def add_edge(self,u,v):
        if u not in self.adj_list:
            self.adj_list[u]=[]
        if v not in self.adj_list:
            self.adj_list[v]=[]
        self.adj_list[u].append(v)         
        self.adj_list[v].append(u)
    def dfs(self,node): 
        if node not in self.visited:
            self.visited.add(node)
            print(node,end=" ")
            for neighbour in self.adj_list[node]:
                self.dfs(neighbour)
g=Graph()
g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('B','D')
g.add_edge('C','E')
print("\n dfs traversal")
g.dfs('A')
