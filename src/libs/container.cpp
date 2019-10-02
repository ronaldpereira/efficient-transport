#include "container.hpp"

void Container::PrintVars()
{
    std::cout << height << ", " << width << std::endl;

    for (auto w : weights)
        std::cout << w << " ";
    std::cout << std::endl;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            std::cout << initial_config[i][j] << " ";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            std::cout << final_config[i][j] << " ";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

Container::Container()
{
    std::cin >> height >> width;

    int w;
    for (int i = 0; i < height * width; i++)
    {
        std::cin >> w;
        weights.push_back(w);
    }

    BuildInitialAndFinalConfig();
}

void Container::BuildInitialAndFinalConfig()
{
    int box;

    for (int i = 0; i < height; i++)
    {
        initial_config.push_back(std::vector<int>(width));
        for (int j = 0; j < width; j++)
        {
            std::cin >> box;
            initial_config[i][j] = box;
        }
    }

    for (int i = 0; i < height; i++)
    {
        final_config.push_back(std::vector<int>(width));
        for (int j = 0; j < width; j++)
        {
            std::cin >> box;
            final_config[i][j] = box;
        }
    }
}
