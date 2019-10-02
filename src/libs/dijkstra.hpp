#ifndef DIJKSTRA
#define DIJKSTRA

#include <algorithm>
#include "graph.hpp"
#include "heap.hpp"

class Dijkstra
{
public:
    Graph *graph;
    Heap heap;

    Dijkstra(Graph *);
    void Execute();
};

#endif
