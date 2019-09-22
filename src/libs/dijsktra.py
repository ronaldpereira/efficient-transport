from libs.heap import Heap


class Dijsktra:
    def __init__(self, g):
        self.g = g
        self.heap = Heap()
        self.heap.push(self.g.nodes[self.g.index_initial], self.g.index_initial)

    def execute(self):
        visited_nodes = []
        while len(self.heap) > 0:
            u_index = self.heap.pop()

            u = self.g.nodes[u_index]

            # If the search reaches the final node,
            # stop the search
            if u.config == self.g.nodes[self.g.index_final].config:
                self.g.nodes[self.g.index_final].distance = u.distance
                break

            neighbors = u.generate_next_moves(
                self.g.nodes, self.g.original_weights, self.g.lookup
            )
            for v_index, uv_cost in neighbors:
                v = self.g.nodes[v_index]
                if v.distance > u.distance + uv_cost:
                    v.distance = u.distance + uv_cost
                    v.pi = u
                    if v_index not in visited_nodes:
                        self.heap.push(v, v_index)
                        visited_nodes.append(v_index)
