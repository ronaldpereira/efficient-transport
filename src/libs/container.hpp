#ifndef CONTAINER
#define CONTAINER

#include <iostream>
#include <vector>
#include <sstream>
#include <vector>
#include <string>

class Container
{
private:
    void BuildInitialAndFinalConfig();

public:
    int height, width;
    std::vector<int> weights;
    std::vector<std::vector<int>> initial_config, final_config;
    Container();
    void PrintVars();
};

#endif
