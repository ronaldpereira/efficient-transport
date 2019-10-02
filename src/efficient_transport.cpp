#include <iostream>
#include "libs/graph.hpp"

int main()
{
    // Fast reading from input
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(0);

    Graph graph;

    graph.GenerateConfigs(graph.initial_config);

    std::cout << graph.FlatConfig(graph.initial_config) << std::endl;

    return 0;
}
