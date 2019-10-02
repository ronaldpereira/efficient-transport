#include "heap.hpp"

int Heap::Size()
{
    return heap.size();
}

void Heap::Push(int distance, int node_index)
{
    heap.push(std::make_pair(distance, node_index));
}

int Heap::Pop()
{
    std::pair<int, int> minNode = heap.top();
    heap.pop();

    return minNode.second;
}
