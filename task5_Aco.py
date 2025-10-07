import numpy as np

# Given distance matrix
d = np.array([
    [0, 10, 12, 11, 14],
    [10, 0, 13, 15, 8],
    [12, 13, 0, 9, 14],
    [11, 15, 9, 0, 16],
    [14, 8, 14, 16, 0]
])

iteration = 100
n_ants = 5
n_cities = 5

# Parameters
evaporation = 0.5    # evaporation rate
alpha = 1            # pheromone importance
beta = 2             # visibility importance

# Initialize visibility matrix (1/distance)
visibility = 1 / (d + np.eye(n_cities))  # avoid division by zero
visibility[d == 0] = 0  # ensure diagonal remains 0

# Initialize pheromone matrix
pheromone = 0.1 * np.ones((n_cities, n_cities))

# Initialize ant routes (including return to start)
rute = np.ones((n_ants, n_cities + 1))

for ite in range(iteration):
    rute[:, 0] = 1  # All ants start at city 1

    for ant in range(n_ants):
        visited = set()
        visited.add(0)  # Starting from city 0 (indexing from 0)

        for j in range(n_cities - 1):
            current_city = int(rute[ant, j]) - 1

            prob = np.zeros(n_cities)
            for k in range(n_cities):
                if k not in visited:
                    prob[k] = (pheromone[current_city, k] ** alpha) * (visibility[current_city, k] ** beta)
                else:
                    prob[k] = 0

            total = np.sum(prob)
            if total == 0:
                next_city = list(set(range(n_cities)) - visited)[0]
            else:
                prob = prob / total
                cum_prob = np.cumsum(prob)
                r = np.random.rand()
                next_city = np.where(cum_prob >= r)[0][0]

            rute[ant, j + 1] = next_city + 1
            visited.add(next_city)

        # Complete the tour by returning to start
        rute[ant, -1] = rute[ant, 0]

    # Evaluate cost of each ant's tour
    dist_cost = np.zeros(n_ants)
    for ant in range(n_ants):
        cost = 0
        for j in range(n_cities):
            from_city = int(rute[ant, j]) - 1
            to_city = int(rute[ant, j + 1]) - 1
            cost += d[from_city, to_city]
        dist_cost[ant] = cost

    # Find the best route
    best_index = np.argmin(dist_cost)
    best_route = rute[best_index]
    best_cost = dist_cost[best_index]

    # Update pheromone
    pheromone *= (1 - evaporation)
    for ant in range(n_ants):
        for j in range(n_cities):
            from_city = int(rute[ant, j]) - 1
            to_city = int(rute[ant, j + 1]) - 1
            pheromone[from_city, to_city] += 1.0 / dist_cost[ant]

print("Route of all the ants at the end:")
print(rute.astype(int))
print()
print("Best path:", best_route.astype(int))
print("Cost of the best path:", int(best_cost))
