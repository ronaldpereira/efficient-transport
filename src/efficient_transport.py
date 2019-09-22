from libs.container import Container
from libs.dijsktra import Dijsktra
from libs.graph import Graph


def main():
    container = Container()

    g = Graph(container)

    dijkstra = Dijsktra(g)
    dijkstra.execute()

    # prints the minimum distance found
    # to the final configuration
    print(g.nodes[g.index_final].distance)


if __name__ == "__main__":
    main()
