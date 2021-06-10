#include <iostream>
#include <random>

int main() {
    int nums[81];
    for (int i = 0; i < 81; i++) {
        nums[i] = rand() % 81;
        std::cout << nums[i] << ", ";
    }

}