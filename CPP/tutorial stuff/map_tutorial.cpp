#include <iostream>
#include <string.h>
#include <map>
#include <utility>
using namespace std;

int main()
{
    // Initializing a map with integer keys
    // and corresponding string values
    map<int, string> Employees;

    // Inserting values in map using insert function
    Employees.insert(std::pair<int, string>(101, "Aaron"));
    Employees.insert(std::pair<int, string>(102, "Amanda"));
    Employees.insert(std::pair<int, string>(105, "Ryan"));

    // Finding the value corresponding to the key '102'
    std::map<int, string> ::iterator it = Employees.find(102);
    if (it != Employees.end()) {
        std::cout << endl << "Value of key = 102 => " << Employees.find(102)->second << '\n';
    }
}