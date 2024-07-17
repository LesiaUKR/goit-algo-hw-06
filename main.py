# TASK 1
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from graph_search import dfs_path, bfs_path, calculate_distance
from data import stations, edges_with_lines, positions
from dijkstra import save_dijkstra_results_to_md

# Створення графа
G = nx.Graph()
G.add_nodes_from(stations)
for station1, station2, weight, line_color in edges_with_lines:
    G.add_edge(station1, station2, weight=weight, line_color=line_color)

# Кольори ребер для візуалізації
edge_colors = [G[u][v]['line_color'] for u, v in G.edges]

# Вага ребер для позначення
edge_weights = {(u, v): G[u][v]['weight'] for u, v in G.edges}

# Візуалізація графа
plt.figure(figsize=(14, 10))
nx.draw(
    G, 
    pos=positions, 
    with_labels=True, 
    node_color="lightblue", 
    edge_color=edge_colors, 
    node_size=500, 
    font_size=8, 
    font_weight="bold"
)

# Вивід позначок ребер (ваг)
nx.draw_networkx_edge_labels(G, pos=positions, edge_labels=edge_weights, font_color='red')

plt.title("Kyiv Metro Network")
plt.show()

# Calculate and print basic graph properties
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")

# Convert degrees to a pandas DataFrame and print as a table
degrees_df = pd.DataFrame(list(degrees.items()), columns=['Station', 'Degree'])
print(degrees_df)

# Convert NetworkX graph to adjacency list
adjacency_list = nx.to_dict_of_lists(G)

# Example usage of DFS and BFS
start_station = "Akademmistechko"
end_station = "Kontraktova Ploshcha"

dfs_result = dfs_path(adjacency_list, start_station, end_station)
bfs_result = bfs_path(adjacency_list, start_station, end_station)

dfs_distance = calculate_distance(G, dfs_result)
bfs_distance = calculate_distance(G, bfs_result)

print("DFS path from {} to {}: {}".format(start_station, end_station, dfs_result))
print("DFS distance: {}".format(dfs_distance))
print("BFS path from {} to {}: {}".format(start_station, end_station, bfs_result))
print("BFS distance: {}".format(bfs_distance))

# Save Dijkstra results to markdown file
save_dijkstra_results_to_md(G, "dijkstra_results.md")