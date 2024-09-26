import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Read nodes and edges from Excel files
nodes_df = pd.read_csv(r"C:\Users\abhip\OneDrive\Documents\Rutgers Study\DS\project\3d-force-graph-master\3d-force-graph-master\json\nodes.csv")
edges_df = pd.read_csv(r"C:\Users\abhip\OneDrive\Documents\Rutgers Study\DS\project\3d-force-graph-master\3d-force-graph-master\json\edges.csv")

def dfs_highlight_path(G, start, end):

    path = []

    # Perform DFS
    visited = set()
    stack = [(start, [start])]
    while stack:
        (node, current_path) = stack.pop()
        if node not in visited:
            visited.add(node)
            if node == end:
                path = current_path
                break
            for neighbor in G[node]:
                stack.append((neighbor, current_path + [neighbor]))

    # Highlight the path on the graph
    edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    pos = nx.spring_layout(G)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=2)  # Highlighted edges
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_labels(G, pos)

    # Show the plot
    plt.title('Force-Directed Graph with Highlighted Path')
    plt.axis('off')  # Turn off axis
    plt.show()

    return path

# Create a graph
G = nx.Graph()

# Add nodes to the graph
for _, node_data in nodes_df.iterrows():
    # print(node_data)
    G.add_node(node_data['id'], name=node_data['name'])

# Add edges to the graph
for _, edge_data in edges_df.iterrows():
    # print(edge_data)
    G.add_edge(edge_data['source'], edge_data['target'])

# Plot the graph using a force-directed layout
pos = nx.spring_layout(G)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=500)

# Draw edges
nx.draw_networkx_edges(G, pos)

# Draw node labels
nx.draw_networkx_labels(G, pos)

# Show the plot
plt.title('Force-Directed Graph')
plt.axis('off')  # Turn off axis
plt.show()

path = dfs_highlight_path(G, 19, 105)
print("Path IDs :" , path )
print("Path:")
for i in range(len(path)):
    print(nodes_df.loc[nodes_df['id'] == path[i]]['name'][path[i]],end='')
    if i < len(path)-1:
        print("->",end='')