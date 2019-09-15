#ifndef GRAPH_HPP
#define GRAPH_HPP

#include <vector>

class AdjListGraph
{
public:
    // Data
    std::vector<std::vector<int, int>> graph;

    // Methods
    void insertNode(int, int);
};

#endif
