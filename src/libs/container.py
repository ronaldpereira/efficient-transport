from copy import deepcopy


class Container:
    def __init__(self):
        height, width = input().split()
        self.height = int(height)
        self.width = int(width)

        weights = input().split()
        self.weights = list(map(lambda x: int(x), weights))

        config = Configuration(self.weights)
        self.initial_conf = config.read_config(self.height)
        self.final_conf = config.read_config(self.height)


class Configuration:
    def __init__(self, weights):
        self.weights = weights

    def read_config(self, height):
        conf = [[]] * height
        for i in range(height):
            boxes = input().split()
            boxes = list(map(lambda x: int(x), boxes))
            conf[i] = boxes

        return conf

    def generate_configs(self, base_config):
        configs = []
        for box_x in range(len(base_config)):
            for box_y in range(len(base_config[box_x])):
                # Try to move the box vertically
                if box_x - 1 >= 0:
                    configs.append(self.move_up(deepcopy(base_config), box_x, box_y))

                # Try to move the box horizontally
                if box_y - 1 >= 0:
                    configs.append(
                        self.move_left(deepcopy(base_config), box_x, box_y)
                    )
        return configs

    def move_up(self, config, box_x, box_y):
        config[box_x][box_y], config[box_x - 1][box_y] = (
            config[box_x - 1][box_y],
            config[box_x][box_y],
        )
        cost = (
            self.weights[config[box_x][box_y] - 1]
            + self.weights[config[box_x - 1][box_y] - 1]
        )
        return config, cost

    def move_left(self, config, box_x, box_y):
        config[box_x][box_y], config[box_x][box_y - 1] = (
            config[box_x][box_y - 1],
            config[box_x][box_y],
        )
        cost = (
            self.weights[config[box_x][box_y] - 1]
            + self.weights[config[box_x][box_y - 1] - 1]
        )
        return config, cost
