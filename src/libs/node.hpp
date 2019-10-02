#ifndef NODE
#define NODE

#include <vector>
#include <limits.h>

class Node
{
public:
    std::vector<std::vector<int>> config;
    int cost;
    int distance;

    Node(std::vector<std::vector<int>>);
};

#endif
