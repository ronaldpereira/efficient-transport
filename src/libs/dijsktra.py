import libs.graph as GRAPH
import libs.heap as HEAP


class Dijsktra:
    def __init__(self, graph):
        self.d_src = 0

        self.heap = HEAP.Heap()
        graph.node.distance = 0
        self.heap.push(graph.node)

        graph.node.expand()

    def execute(self):
        while len(self.heap) > 0:
            cost, _, u = self.heap.pop()

            u.expand()
            for v in u.next_moves:
                if v.distance > u.distance + cost:
                    v.distance = u.distance + v.cost
                    v.pi = u
                self.heap.push(v)
