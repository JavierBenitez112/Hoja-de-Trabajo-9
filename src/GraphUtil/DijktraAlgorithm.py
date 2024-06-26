import heapq #heapq GOAT
import networkx as nx

def dijkstra(G, start, end)->list: #Dude, is dijkstra, just search it up
    distances = {node: float('inf') for node in G.nodes()}
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_distance > distances[current_node]:
            continue
        
        if current_node == end:
            break
        
        for neighbor in G.neighbors(current_node):
            distance = current_distance + float(G[current_node][neighbor]['weight'])
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    if distances[end] == float('inf'):
        return None
    
    path = [end]
    current_node = end
    
    while current_node != start:
        for neighbor in G.neighbors(current_node):
            if distances[neighbor] == distances[current_node] - float(G[current_node][neighbor]['weight']):
                path.append(neighbor)
                current_node = neighbor
                break
    
    path.reverse()
    return path
