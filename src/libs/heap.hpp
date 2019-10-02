#ifndef HEAP
#define HEAP

#include <queue>

class HeapNodeCompare
{
public:
    int operator()(const std::pair<int, int> &n1, const std::pair<int, int> &n2)
    {
        if (n1.first != n2.first)
        {
            return n1.first > n2.first;
        }
        else
        {
            return n1.second > n2.second;
        }
    }
};

class Heap
{
private:
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, HeapNodeCompare> heap;

public:
    int Size();
    void Push(int, int);
    int Pop();
};

#endif
