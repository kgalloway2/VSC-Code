#include <iostream>

int main() {
    double angle1;
    double angle2;
    double angle3;

    std::cout << "Enter the measure of angle 1: ";
    std::cin >> angle1;

    std::cout << "Enter the measure of angle 2: ";
    std::cin >> angle2;

    std::cout << "Enter the measure of angle 3: ";
    std::cin >> angle3;

    double angleSum = angle1 + angle2 + angle3;

    if (angleSum == 180) {
        std::cout << "These angles make a triangle!\n";
    }
    else {
        std::cout << "These angles do not make a triangle.\n";
    }
}