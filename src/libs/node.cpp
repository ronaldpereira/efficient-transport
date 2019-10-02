#include "node.hpp"

Node::Node(std::vector<std::vector<int>> _config)
{
    config = _config;
    cost = 0;
    distance = INT_MAX;
}
