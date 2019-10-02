#ifndef GRAPH
#define GRAPH

#include <iostream>
#include <string>
#include <vector>
#include "node.hpp"

class Graph
{
private:
    void InsertConfigToLookup(std::vector<std::vector<int>>);
    bool CheckConfigIsInsertedInLookup(std::vector<std::vector<int>>);
    std::string FlatConfig(std::vector<std::vector<int>>);

public:
    int height, width;
    std::vector<int> weights;
    std::vector<std::vector<int>> initial_config, final_config;
    std::vector<Node> nodes;

    Graph();
    void ReadInitialAndFinalConfig();
    std::vector<std::pair<std::vector<std::vector<int>>, int>> GenerateConfigs(std::vector<std::vector<int>> base_config);
    std::pair<std::vector<std::vector<int>>, int> MoveUp(std::vector<std::vector<int>> base_config, int box_x, int box_y);
    std::pair<std::vector<std::vector<int>>, int> MoveLeft(std::vector<std::vector<int>> base_config, int box_x, int box_y);
};

#endif
