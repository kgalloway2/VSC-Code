#include <iostream>
#include "functions.hpp"

int main() {
    std::vector<int> fib_vec = fibs(10);
    int size = fib_vec.size();
    for (int i = 0; i < size; i++) {
        std::cout << fib_vec[i] << "\n";
    }
    
    std::cout << fib_recur(10) << "\n";

    std::cout << sum_recur(100);
}