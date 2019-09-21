from heapq import heappop, heappush


class Heap:
    def __init__(self):
        self.h = []

    def __len__(self):
        return len(self.h)

    def print(self):
        print(" ".join([str(i) for i in self.h]))

    def push(self, node):
        # The id(node) is used for cost tie-breaking
        heappush(self.h, (node.distance, id(node), node))

    def pop(self):
        return heappop(self.h)
