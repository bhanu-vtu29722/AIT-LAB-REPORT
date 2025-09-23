class Graph:
    def __init__(self, adjacency_list, heuristic):
        self.adjacency_list = adjacency_list
        self.heuristic = heuristic

    def get_neighbors(self, node):
        return self.adjacency_list.get(node, [])

    def a_star(self, start, goal):
        open_list = set([start])
        closed_list = set()

        g = {start: 0} 
        parents = {start: None}  

        while open_list:
            current = min(open_list, key=lambda n: g[n] + self.heuristic.get(n, float('inf')))

            if current == goal:
                path = []
                while current is not None:
                    path.append(current)
                    current = parents[current]
                path.reverse()
                return path, g[goal] 

            open_list.remove(current)
            closed_list.add(current)

            for neighbor, cost in self.get_neighbors(current):
                if neighbor in closed_list:
                    continue
                tentative_g = g[current] + cost

                if neighbor not in open_list:
                    open_list.add(neighbor)
                elif tentative_g >= g.get(neighbor, float('inf')):
                    continue

                parents[neighbor] = current
                g[neighbor] = tentative_g

        return None, float('inf')  


if __name__ == "__main__":
    adjacency_list = {
        'A': [('B', 2), ('C', 4),('D', 1)],
         'B': [('E', 7), ('F', 3)],
         'C': [('F', 1)],
         'D': [('G', 5)],
        'E': [('G', 2)],
        'F': [('G', 2),('G', 1)],
        'G':[]
    }

    heuristic = {
        'A': 7, 'B': 6, 'C': 2, 'D':3,'E':1,'G':0,'F':1
    }

    graph = Graph(adjacency_list, heuristic)
    start_node = 'A'
    goal_node = 'G'

    path, cost = graph.a_star(start_node, goal_node)
    if path:
        print(f"Path found: {path}")
        print(f"Total cost: {cost}")
    else:
        print("No path found.")
