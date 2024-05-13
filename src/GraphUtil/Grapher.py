import heapq
import networkx as nx
import matplotlib.pyplot as plt

def GraphCreation(PathFile: str) -> nx.Graph:
    with open(PathFile, 'r') as f:
        G = nx.Graph()
        for line in f:
            line = line.split(",") # Separar por coma
            G.add_edge(line[0], line[1], weight=float(line[2]))  # Convertir el peso a float
    return G 


def draw_paths(G, paths, colors, path_label) -> None:
    num_paths = len(paths)
    fig, axes = plt.subplots(1, num_paths, figsize=(5*num_paths, 5))
    
    for i, (path, color) in enumerate(zip(paths, colors)):
        pos = nx.spring_layout(G) #positions for all nodes with cools layout I didn't knew existed
        edges = [(path[j], path[j + 1]) for j in range(len(path) - 1)] #grabs all the edges
        
        ax = axes[i] if num_paths > 1 else axes  # idunno, magic
        ax.set_title(f"{path_label}")
        
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color=color, node_size=700, ax=ax) # draw nodes taken with the DFS
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color=color, width=2, ax=ax) # draw edges taken with the DFS
        labels = {node: node for node in path} # self explanatory
        nx.draw_networkx_labels(G, pos, labels=labels, ax=ax) # also self explanatory

    plt.tight_layout() #for the overlapping nodes (fuck those things)


def ShowAllDestinations(G: nx.Graph, source: str) -> None:
    def dfs_with_graph(G, start, end, path=[]): #classic dfs for graphs (you know how it works)
        path = path + [start]
        if start == end:
            return [path]
        if not G.has_node(start):
            return []
        paths = []
        for node in G.neighbors(start):
            if node not in path:
                newpaths = dfs_with_graph(G, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    all_destinations = G.nodes()
    for destination in all_destinations:
        if destination != source:
            all_paths = dfs_with_graph(G, source, destination) # applies dfs to that node
            if all_paths:
                for path in all_paths:
                    draw_paths(G, [path], 'red', f"camino {source} -> {destination}") #if all_paths returns something it graphs it
