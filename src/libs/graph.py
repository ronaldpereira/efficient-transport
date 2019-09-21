from itertools import permutations, zip_longest
from math import factorial

import libs.container as CONTAINER


class Graph:
    def __init__(self, container):
        self.height = container.height
        self.width = container.width
        self.original_weights = container.weights
        self.initial_config = container.initial_config
        self.final_config = container.final_config
        self.nodes = []
        self.lookup = {}
        self.generate_all_nodes()

    def generate_all_nodes(self):
        boxes = []
        for i in range(len(self.initial_config)):
            for j in range(len(self.initial_config[i])):
                boxes.append(self.initial_config[i][j])

        for index, configuration in enumerate(list(permutations(boxes))):
            configuration = list(zip_longest(*[iter(configuration)] * self.width))
            configuration = list(map(lambda x: list(x), configuration))
            self.lookup[str(configuration)] = index
            self.nodes.append(
                Node(
                    index, configuration, self.original_weights, self.nodes, self.lookup
                )
            )

            if configuration == self.initial_config:
                self.index_initial = index

            if configuration == self.final_config:
                self.index_final = index

        self.nodes[self.index_initial].distance = 0


class Node:
    def __init__(self, index, config, original_weights, nodes, lookup, cost=0):
        self.original_weights = original_weights
        self.nodes = nodes
        self.lookup = lookup
        self.next_moves = []
        self.index = index
        self.config = config
        self.distance = float("inf")
        self.cost = cost
        self.pi = -1

    def generate_next_moves(self):
        for next_config, next_cost in CONTAINER.Configuration(
            self.original_weights
        ).generate_configs(self.config):
            next_index = self.lookup[str(next_config)]
            self.nodes[next_index].cost = next_cost
            self.next_moves.append([next_index, next_cost])

        return self.next_moves
