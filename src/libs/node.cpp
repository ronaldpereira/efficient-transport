#include "node.hpp"

Node::Node(std::vector<std::vector<int>> config)
{
    config = config;
    cost = 0;
    distance = INT_MAX;
}
