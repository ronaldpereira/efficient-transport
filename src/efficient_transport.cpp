#include <iostream>
#include "libs/graph.hpp"
#include "libs/dijkstra.hpp"

int main()
{
    // Fast reading from input
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(0);

    Graph graph;
    Dijkstra dijkstra(&graph);

    dijkstra.Execute();

    std::cout << graph.nodes[graph.index_final].distance << std::endl;

    return 0;
}
