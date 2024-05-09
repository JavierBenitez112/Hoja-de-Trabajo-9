import networkx as nx
import matplotlib.pyplot as plt

def GraphCreation(PathFile: str) -> nx.Graph: # Pretty self explanatory ngl
    with open(PathFile, 'r') as f:
        G = nx.Graph()
        for line in f:
            line = line.split(",")
            G.add_edge(line[0], line[1], weight=str(line[2]))
    return G 

def ShowwAllDestinations(G: nx.Graph, source: str) -> None:
    def dfs_with_graph(G, start, end): # dude, is just dfs. Ain't going to explain this. is this class 101 (not braging tho)
        stack = [(start, [start])]
        visited = set()

        while stack:
            (node, path) = stack.pop()
            if node not in visited:
                if node == end:
                    return path
                visited.add(node)
                for neighbor in G.neighbors(node):
                    stack.append((neighbor, path + [neighbor]))

        return None
    def draw_path(G, path): #TODO: Might wanna add something like "From bla to bla path is (path)"
        pos = nx.spring_layout(G) # I just found about this graph layout
        edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)] # Edges from path
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='g', node_size=700) # network x doin magic stuff
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='g', width=2) # doin it twice
        labels = {node: node for node in path}
        nx.draw_networkx_labels(G, pos, labels=labels) # idunno why i can't just graph the labels at once, this is so stupid
        
    for destination in G.nodes(): #the real procedure
        path = dfs_with_graph(G, source, destination) # dfs from the source node
        if path is not None:
            print(f"Path from {source} to {destination}: {path}") 
            draw_path(G, path)





