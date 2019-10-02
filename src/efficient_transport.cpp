#include <iostream>
#include <vector>
#include <sstream>
#include <vector>
#include <string>

class Container
{
private:
    int height, width;
    std::vector<int> weights;
    std::vector<std::vector<int>> initial_config, final_config;

public:
    Container();
};

Container::Container()
{
    std::cin >> height >> width;

    std::string weights_string;
    std::cin >> weights_string;
    std::stringstream iss(weights_string);

    int w;
    while (iss >> w)
    {
        weights.push_back(w);
    }

    for (auto i : weights)
        std::cout << i << ' ';
}

int main()
{
    // Fast reading from input
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(0);

    return 0;
}
