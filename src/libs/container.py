class Container:
    def __init__(self):
        height, width = input().split()
        self.height = int(height)
        self.width = int(width)

        weights = input().split()
        weights = list(map(lambda x: int(x), weights))

        self.initial_conf = [[]] * self.height
        for i in range(self.height):
            boxes = input().split()
            boxes = list(map(lambda x: int(x), boxes))
            self.initial_conf[i] = boxes

        self.final_conf = [[]] * self.height
        for i in range(self.height):
            boxes = input().split()
            boxes = list(map(lambda x: int(x), boxes))
            self.final_conf[i] = boxes
