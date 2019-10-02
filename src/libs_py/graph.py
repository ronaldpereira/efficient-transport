from libs.container import Configuration


class Graph:
    def __init__(self, container):
        self.height = container.height
        self.width = container.width
        self.original_weights = container.weights
        self.initial_config = container.initial_config
        self.final_config = container.final_config
        self.nodes = []
        self.lookup = {}
        self.generate_source_target_nodes()

    def generate_source_target_nodes(self):
        self.index_initial = len(self.nodes)
        self.lookup[str(self.initial_config)] = self.index_initial
        self.nodes.append(Node(self.initial_config))
        self.nodes[self.index_initial].distance = 0

        # if initial configuration is not the final configuration
        # insert it in a different node
        if self.initial_config != self.final_config:
            self.index_final = len(self.nodes)
            self.lookup[str(self.final_config)] = self.index_final
            self.nodes.append(Node(self.final_config))

        else:
            self.index_final = self.index_initial
            self.lookup[str(self.final_config)] = self.index_initial


class Node:
    def __init__(self, config):
        self.config = config
        self.cost = 0
        self.distance = float("inf")
        self.pi = -1
        self.next_moves = []

    def generate_next_moves(self, nodes, original_weights, lookup):
        for next_config, next_cost in Configuration(original_weights).generate_configs(
            self.config
        ):
            if str(next_config) not in lookup.keys():
                next_index = len(nodes)
                lookup[str(next_config)] = next_index
                nodes.append(Node(next_config))
            else:
                next_index = lookup[str(next_config)]

            nodes[next_index].cost = next_cost
            self.next_moves.append([next_index, next_cost])

        return self.next_moves
