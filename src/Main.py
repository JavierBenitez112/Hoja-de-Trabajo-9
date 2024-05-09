import GraphUtil.Grapher as Graph
import matplotlib.pyplot as plt

#TODO: doc this shit (sorry for the curse word, ain't my best time)
if __name__ == "__main__":
    G = Graph.GraphCreation("src/rutas.txt")

    input_source = input("Enter the source: ")
    Graph.ShowwAllDestinations(G, input_source)

    #TODO: Do Djikstra's in here

    plt.xlim(-1, 1)
    plt.show()