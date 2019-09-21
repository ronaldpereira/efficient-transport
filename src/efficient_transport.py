import libs.container as CONTAINER
import libs.dijsktra as DIJSKTRA
import libs.graph as GRAPH


def main():
    container = CONTAINER.Container()

    print("initialconf:")
    print(container.initial_conf)
    print("finalconf:")
    print(container.final_conf)
    print("weights:")
    print({i + 1: w for i, w in enumerate(container.weights)})
    print()

    graph = GRAPH.Graph(container.initial_conf, 0, container.weights)

    dijkstra = DIJSKTRA.Dijsktra(graph)
    dijkstra.execute()


if __name__ == "__main__":
    main()
