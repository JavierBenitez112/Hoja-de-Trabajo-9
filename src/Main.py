import GraphUtil.Grapher as Graph
import matplotlib.pyplot as plt
import networkx as nx
import GraphUtil.DijktraAlgorithm as djs

if __name__ == "__main__":
    G = Graph.GraphCreation("src/rutas.txt")

    #input_source = input("Enter the source: ")
    input_source = "Pueblo Paleta"
    #input_destination = input("Enter the destination: ")
    input_destination = "Aldea Azalea"

    # Muestra todos los posibles caminos
    Graph.ShowAllDestinations(G, input_source)

    shortest_path = djs.dijkstra(G, input_source, input_destination)
    Graph.draw_paths(G, [shortest_path], "g", "Camino mas corto")

    plt.xlim(-1, 1)  # Se puede ajustar según el grafo
    plt.show()
