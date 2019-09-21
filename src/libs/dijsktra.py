import libs.graph as GRAPH
import libs.heap as HEAP


class Dijsktra:
    def __init__(self, g):
        self.g = g
        self.heap = HEAP.Heap()
        self.heap.push(self.g.nodes[self.g.index_initial])

    def execute(self):
        visited_nodes = []
        while len(self.heap) > 0:
            u_index = self.heap.pop()

            # If the search reaches the final node,
            # stop the search
            if u_index == self.g.index_final:
                break

            u = self.g.nodes[u_index]

            neighbors = u.generate_next_moves()
            for v_index, uv_cost in neighbors:
                v = self.g.nodes[v_index]
                if v.distance > u.distance + uv_cost:
                    v.distance = u.distance + uv_cost
                    v.pi = u
                    if v.index not in visited_nodes:
                        self.heap.push(v)
                        visited_nodes.append(v.index)
