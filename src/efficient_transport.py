import libs.container as CONTAINER
import libs.graph as GRAPH


def main():
    container = CONTAINER.Container()

    print(container.initial_conf)
    print(container.final_conf)

    graph = GRAPH.Graph(container.initial_conf, container.weights)

    for move in graph.start.moves:
        print(move)

if __name__ == "__main__":
    main()
