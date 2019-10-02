from libs.container import Container
from libs.dijkstra import Dijkstra
from libs.graph import Graph


def main():
    container = Container()

    g = Graph(container)

    dijkstra = Dijkstra(g)
    dijkstra.execute()

    # prints the minimum distance found
    # to the final configuration
    print(g.nodes[g.index_final].distance)


if __name__ == "__main__":
    main()
