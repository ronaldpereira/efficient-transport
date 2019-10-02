#include "graph.hpp"

Graph::Graph()
{
    std::cin >> height >> width;

    int w;
    for (int i = 0; i < height * width; i++)
    {
        std::cin >> w;
        weights.push_back(w);
    }

    ReadInitialAndFinalConfig();
}

std::vector<std::pair<std::vector<std::vector<int>>, int>> Graph::GenerateConfigs(std::vector<std::vector<int>> base_config)
{
    std::vector<std::pair<std::vector<std::vector<int>>, int>> configs;

    for (int box_x = 0; box_x < height; box_x++)
    {
        for (int box_y = 0; box_y < width; box_y++)
        {
            // Check if it's possible to move the box up
            if (box_x - 1 >= 0)
            {
                configs.push_back(MoveUp(base_config, box_x, box_y));
            }

            // Check if it's possible to move the box left
            if (box_y - 1 >= 0)
            {
                configs.push_back(MoveLeft(base_config, box_x, box_y));
            }
        }
    }

    return configs;
}

std::pair<std::vector<std::vector<int>>, int> Graph::MoveUp(std::vector<std::vector<int>> base_config, int box_x, int box_y)
{
    int tmp = base_config[box_x][box_y];
    base_config[box_x][box_y] = base_config[box_x - 1][box_y];
    base_config[box_x - 1][box_y] = tmp;

    int cost = weights[base_config[box_x][box_y] - 1] + weights[base_config[box_x - 1][box_y] - 1];

    return std::make_pair(base_config, cost);
}

std::pair<std::vector<std::vector<int>>, int> Graph::MoveLeft(std::vector<std::vector<int>> base_config, int box_x, int box_y)
{
    int tmp = base_config[box_x][box_y];
    base_config[box_x][box_y] = base_config[box_x][box_y - 1];
    base_config[box_x][box_y - 1] = tmp;

    int cost = weights[base_config[box_x][box_y] - 1] + weights[base_config[box_x][box_y - 1] - 1];

    return std::make_pair(base_config, cost);
}

void Graph::ReadInitialAndFinalConfig()
{
    int box;
    for (int i = 0; i < height; i++)
    {
        initial_config.push_back(std::vector<int>(width));
        for (int j = 0; j < width; j++)
        {
            std::cin >> box;
            initial_config[i][j] = box;
        }
    }

    for (int i = 0; i < height; i++)
    {
        final_config.push_back(std::vector<int>(width));
        for (int j = 0; j < width; j++)
        {
            std::cin >> box;
            final_config[i][j] = box;
        }
    }
}

// TODO: generate_source_target_nodes function, node lib and dijstra lib
