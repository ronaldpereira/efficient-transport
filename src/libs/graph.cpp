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

void Graph::GenerateSourceTargetNodes()
{
    index_initial = 0;
    nodes.push_back(Node(initial_config));
    lookup[FlatConfig(initial_config)] = index_initial;
    nodes[index_initial].distance = 0;

    // If initial configuration is not the final configuration
    // insert it subsequent node
    if (initial_config != final_config)
    {
        index_final = 1;
        nodes.push_back(Node(final_config));
        lookup[FlatConfig(final_config)] = index_final;
    }
    else
    {
        index_final = index_initial;
        lookup[FlatConfig(final_config)] = index_initial;
    }
}

int Graph::FlatConfig(std::vector<std::vector<int>> config)
{
    std::string flat_config = "";

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            flat_config += std::to_string(config[i][j]);
        }
    }

    return std::stoi(flat_config);
}

std::vector<std::pair<int, int>> Graph::GenerateNextMoves(Node node)
{
    std::vector<std::pair<int, int>> next_moves;

    for (auto config : GenerateConfigs(node.config))
    {
        std::vector<std::vector<int>> next_config = config.first;
        int next_cost = config.second;

        auto lookup_index = lookup.find(FlatConfig(next_config));
        int next_index;
        if (lookup_index == lookup.end())
        {
            next_index = lookup.size();
            lookup[FlatConfig(next_config)] = next_index;
            nodes.push_back(Node(next_config));
        }
        else
        {
            next_index = lookup[FlatConfig(next_config)];
        }

        nodes[next_index].cost = next_cost;
        next_moves.push_back(std::make_pair(next_index, next_cost));
    }

    return next_moves;
}
