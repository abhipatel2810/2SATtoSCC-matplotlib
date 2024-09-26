import pandas as pd
import json

# Read nodes and edges from Excel files
nodes_df = pd.read_csv(r"C:\Users\abhip\OneDrive\Documents\Rutgers Study\DS\project\3d-force-graph-master\3d-force-graph-master\json\nodes.csv")
edges_df = pd.read_csv(r"C:\Users\abhip\OneDrive\Documents\Rutgers Study\DS\project\3d-force-graph-master\3d-force-graph-master\json\edges.csv")


given_ids = [23, 26, 18, 40, 24, 104, 69, 97, 66, 12, 53, 34, 63, 32, 15, 42, 41, 36, 4, 35, 33, 8, 72, 93, 95, 90, 103, 108, 107, 105, 92, 94, 91, 3, 102, 2, 48, 86, 75, 68, 1, 50, 52, 51, 0, 29]
nodes_json = []
for _, row in nodes_df.iterrows():
    nodes_json.append({"id": str(row['id']), "name": row['name']} )

links_json = []
for _, row in edges_df.iterrows():
    links_json.append({"source": str(row['source']), "target": str(row['target'])})


json_data = {"nodes": nodes_json, "links": links_json}

#feed the path to given_ids

for node in json_data['nodes']:
    if int(node['id']) in given_ids:
        node["group"] = 1

print(len(json_data))

with open(r'C:\Users\abhip\OneDrive\Documents\Rutgers Study\DS\project\3d-force-graph-master\3d-force-graph-master\json\starwars.json', 'w') as outfile:
    json.dump(json_data, outfile)