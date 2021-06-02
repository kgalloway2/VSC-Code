#include <iostream>
#include <vector>
#include <cmath>

int main() {
    std::vector<double> numbers;
    double temp_number;

    while (true) {
        std::cout << "Add another data point? (Input '-1' to stop.)";
        std::cin >> temp_number;
        if (temp_number == -1) {
            break;
        }
        else {
            numbers.push_back(temp_number);
        }
    }

    double sum = 0;
    double mean;
    double std;

    for (int i = 0; i < numbers.size(); i++) {
        sum += numbers[i];
    }
    std::cout << "The sum of these numbers is " << sum << ".\n";

    mean = sum / numbers.size();
    std::cout << "The mean of these numbers is " << mean << ".\n";

    double squared_deviation_sum = 0;
    for (int i = 0; i < numbers.size(); i++) {
        squared_deviation_sum += pow(numbers[i] - mean, 2);
    }

    std = pow(squared_deviation_sum / (numbers.size() - 1), 0.5);
    std::cout << "The standard deviation of these numbers is " << std << ".\n";
}