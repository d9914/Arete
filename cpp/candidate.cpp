/*
N Nearest Stores Problem
Implement the functions below.

For n_nearest_without_obstacles, your function should return the N nearest stores to 
the provided input position.

For n_nearest_with_obstacles, your function should return the N nearest stores to the 
provided input position that avoid the obstacles defined in the map file.
*/

#include <iostream>
#include <string>
#include <vector>
// TODO: add any additional include statements here


/*
    PROBLEM 1
    Returns a vector of n_stores stores closest to the provided input position (pos)
    using the input file (input_file).
*/
std::vector<std::string> n_nearest_without_obstacles(std::string input_file, int n_stores, std::pair<int, int> pos)
{
    printf("Please implement your solution to problem 1 here.");

    return std::vector<std::string> {};
}


/*
    PROBLEM 2
    Returns a vector of n_stores stores closest to the provided input position (pos)
    from the input file (input_file), avoiding obstacles in the map (map_file).
*/
std::vector<std::string> n_nearest_with_obstacles(std::string input_file, std::string map_file, int n_stores, std::pair<int, int> pos)
{
    printf("Please implement your solution to problem 2 here.");

    return std::vector<std::string> {};
}

int main()
{
    std::string input_file {"../inp_files/stores.csv"};
    std::string map_file {"../inp_files/stores_map.txt"};
    int n_stores {5};
    std::pair<int, int> pos (0,0);

    std::vector<std::string> prob1;
    std::vector<std::string> prob2;

    prob1 = n_nearest_without_obstacles(input_file, n_stores, pos);
    prob2 = n_nearest_with_obstacles(input_file, map_file, n_stores, pos);

    
}