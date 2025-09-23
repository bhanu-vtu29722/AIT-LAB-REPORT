import random
class Graph:
    def __init__(self, num_nodes, directed=True):
        self.num_nodes = num_nodes
        self.directed = directed
        self.adj_matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]

    def add_edge(self, u, v, cost):
        self.adj_matrix[u][v] = cost
        if not self.directed:
            self.adj_matrix[v][u] = cost

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(row)

    def print_all_costs(self):
        print("\nCost from every node to every other node:")
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                print(f"Cost from {i} to {j}: {self.adj_matrix[i][j]}")
            print()

    def calculate_route_cost(self, route):
        total = 0
        for i in range(len(route)):
            u = route[i]
            v = route[(i + 1) % len(route)]  
            total += self.adj_matrix[u][v]
        return total


    def generate_neighbors(self, route):
        neighbors = []
        for i in range(len(route)):
            for j in range(i + 1, len(route)):
                neighbor = route.copy()
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append(neighbor)
        return neighbors
    def generate_random_solution(self):
        route = list(range(self.num_nodes))
        random.shuffle(route)
        return route

    def hill_climbing(self):
        current_route = self.generate_random_solution()
        current_cost = self.calculate_route_cost(current_route)

        while True:
            neighbors = self.generate_neighbors(current_route)
            best_neighbor = None
            best_cost = current_cost

            for neighbor in neighbors:
                cost = self.calculate_route_cost(neighbor)
                if cost < best_cost:
                    best_cost = cost
                    best_neighbor = neighbor

            if best_neighbor:
                current_route = best_neighbor
                current_cost = best_cost
            else:
                break  

        return current_route, current_cost

g = Graph(num_nodes=4, directed=True)
g.add_edge(A, B,2)
g.add_edge(B, C, 3)
g.add_edge(C, D, 1)
g.add_edge(D, A, 1)



g.print_graph()

g.print_all_costs()

best_route, total_cost = g.hill_climbing()
print("\nBest Route Found:", best_route)
print("Total Cost of Best Route:", total_cost)
