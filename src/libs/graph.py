import libs.container as CONTAINER


class Graph:
    def __init__(self, initial_config, weights):
        self.start = Node(initial_config, weights)


class Node:
    def __init__(self, config, weights):
        self.config = config

        self.moves = []
        for config, weight in CONTAINER.Configuration.generate_configs(
            self.config, weights
        ):
            self.moves.append((config, weight))
