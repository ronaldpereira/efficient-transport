from copy import deepcopy


class Container:
    def __init__(self):
        height, width = input().split()
        self.height = int(height)
        self.width = int(width)

        weights = input().split()
        self.weights = list(map(lambda x: int(x), weights))

        self.initial_conf = Configuration.read_config(self.height)
        self.final_conf = Configuration.read_config(self.height)


class Configuration:
    @staticmethod
    def read_config(height):
        conf = [[]] * height
        for i in range(height):
            boxes = input().split()
            boxes = list(map(lambda x: int(x), boxes))
            conf[i] = boxes

        return conf

    @staticmethod
    def generate_configs(initial_config, weights):
        configs = []
        for box_x in range(len(initial_config)):
            for box_y in range(len(initial_config[box_x])):
                # Try to move the box vertically
                if box_x - 1 >= 0:
                    configs.append(
                        Configuration.move_up(
                            deepcopy(initial_config), weights, box_x, box_y
                        )
                    )

                # Try to move the box horizontally
                if box_y - 1 >= 0:
                    configs.append(
                        Configuration.move_left(
                            deepcopy(initial_config), weights, box_x, box_y
                        )
                    )
        return configs

    @staticmethod
    def move_up(config, weights, box_x, box_y):
        config[box_x][box_y], config[box_x - 1][box_y] = (
            config[box_x - 1][box_y],
            config[box_x][box_y],
        )
        cost = weights[config[box_x][box_y] - 1] + weights[config[box_x - 1][box_y] - 1]
        return config, cost

    @staticmethod
    def move_left(config, weights, box_x, box_y):
        config[box_x][box_y], config[box_x][box_y-1] = (
            config[box_x][box_y-1],
            config[box_x][box_y],
        )
        cost = weights[config[box_x][box_y] - 1] + weights[config[box_x][box_y-1] - 1]
        return config, cost
