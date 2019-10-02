#include "dijkstra.hpp"

Dijkstra::Dijkstra(Graph *_graph)
{
    graph = _graph;
    heap.Push(graph->nodes[graph->index_initial].distance, graph->index_initial);
}

void Dijkstra::Execute()
{
    std::vector<int> visited_nodes;
    while (heap.Size() > 0)
    {
        int u_index = heap.Pop();

        Node u = graph->nodes[u_index];

        // If the search reaches the final node, stop the search
        if (u_index == graph->index_final)
        {
            break;
        }

        visited_nodes.push_back(u_index);

        auto neighbors = graph->GenerateNextMoves(u);

        for (auto neighbor : neighbors)
        {
            int v_index = neighbor.first;
            int uv_cost = neighbor.second;

            Node &v = graph->nodes[v_index];

            if (v.distance > u.distance + uv_cost)
            {
                v.distance = u.distance + uv_cost;

                // Check if node[v_index] was already visited by seeing if the config is already inserted in the vector
                auto it = std::find(visited_nodes.begin(), visited_nodes.end(), v_index);
                if (it == visited_nodes.end())
                {
                    heap.Push(v.distance, v_index);
                }
            }
        }
    }
}
