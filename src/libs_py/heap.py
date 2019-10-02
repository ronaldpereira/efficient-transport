from heapq import heappop, heappush


class Heap:
    def __init__(self):
        self.h = []

    def __len__(self):
        return len(self.h)

    def push(self, node, node_index):
        heappush(self.h, (node.distance, node_index))

    def pop(self):
        return heappop(self.h)[-1]
