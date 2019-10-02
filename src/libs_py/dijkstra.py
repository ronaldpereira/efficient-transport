from libs.heap import Heap


class Dijkstra:
    def __init__(self, g):
        self.g = g
        self.heap = Heap()
        self.heap.push(self.g.nodes[self.g.index_initial], self.g.index_initial)

    def execute(self):
        while len(self.heap) > 0:
            u_index = self.heap.pop()

            u = self.g.nodes[u_index]

            # If the search reaches the final node,
            # stop the search
            if u_index == self.g.index_final:
                break

            neighbors = u.generate_next_moves(
                self.g.nodes, self.g.original_weights, self.g.lookup
            )
            for v_index, uv_cost in neighbors:
                v = self.g.nodes[v_index]
                if v.distance > u.distance + uv_cost:
                    v.distance = u.distance + uv_cost
                    v.pi = u # Don't use pi
                    
                    # Check if node[v_index] was already visited in O(1)
                    # by seeing if the config is already inserted in the lookup
                    try:
                        self.g.lookup[self.g.nodes[v_index]]
                    except KeyError:
                        self.heap.push(v, v_index)
