import libs.container as CONTAINER


class Graph:
    def __init__(self, config, cost, original_weights):
        self.weights = original_weights
        self.node = Node(config, cost, original_weights)
        self.node.distance = 0


class Node:
    def __init__(self, config, cost, original_weights):
        self.original_weights = original_weights
        self.config = config
        self.cost = cost
        self.distance = float("inf")
        self.pi = -1

    def expand(self):
        self.next_moves = []
        for config, next_cost in CONTAINER.Configuration(
            self.original_weights
        ).generate_configs(self.config):
            self.next_moves.append(
                Node(config, next_cost, self.original_weights)
            )
