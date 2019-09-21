import libs.container as CONTAINER
import libs.dijsktra as DIJSKTRA
import libs.graph as GRAPH


def main():
    container = CONTAINER.Container()

    g = GRAPH.Graph(container)

    dijkstra = DIJSKTRA.Dijsktra(g)

    dijkstra.execute()

    print(g.nodes[g.index_final].distance)


if __name__ == "__main__":
    main()
