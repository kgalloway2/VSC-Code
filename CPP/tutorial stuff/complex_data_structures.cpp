#include <iostream>
#include <cmath>

void print_normed(int arg[], int length);
void print_diagonal(int array[][2], int size);

int main() {
    int test_vec [4] = {0, 1, 2, 3};
    int length = *(&test_vec + 1) - test_vec;
    for (int i = 0; i < length; i++) {
        std::cout << test_vec[i] << '\n';
    }

    int height = 2;
    int width = 2;
    int test_array[height][2];
    // can also make even more dimensions
    // int 6d_array[2][3][4][5][6][7];

    // it's kinda like in julia, where they are stored as 1d arrays
    // but the computer remembers that it is a matrix
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            test_array[i][j] = i + j;
            std::cout << "Entry at " << i << ", " << j << " is " << test_array[i][j] << ".\n";
        }
    }

    print_normed(test_vec, length);
    print_diagonal(test_array, height);

}

void print_normed(int arg[], int length) {
    double new_vec[length];
    double sum_squares = 0;
    for (int i = 0; i < length; i++) {
        sum_squares += arg[i] * arg[i];
    }
    double magnitude = sqrt(sum_squares);
    for (int i=0; i < length; i++) {
        new_vec[i] = arg[i] / magnitude;
        std::cout << new_vec[i] << '\n';
    }

}

void print_diagonal(int array[][2], int size) {
    for (int i = 0; i < size; i++) {
        std::cout << array[i][i] << ", ";
    }
    std::cout << std::endl;
}