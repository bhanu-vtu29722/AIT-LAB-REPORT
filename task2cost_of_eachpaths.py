
graph = {
    'A': {'B': 2, 'D': 4},
    'B': {'A': 2, 'C': 3},
    'C': {'B': 3, 'D': 1},
    'D': {'A': 4, 'C': 1}
}

print(f"Cost from A to B: {graph['A']['B']}")
print(f"Cost from B to C: {graph['B']['C']}")
print(f"Cost from C to D: {graph['C']['D']}")
print(f"Cost from D to A: {graph['D']['A']}")

total_cost = 0
visited_edges = set()

for start_node, edges in graph.items():
    for end_node, cost in edges.items():
        edge = tuple(sorted([start_node, end_node]))
        if edge not in visited_edges:
            total_cost += cost
            visited_edges.add(edge)
  
print(f"Total cost of the closed graph: {total_cost}")
total=graph['A']['B']+graph['B']['C']+graph['C']['D']
print("cost from A to D:",total)
