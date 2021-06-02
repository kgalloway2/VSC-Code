#include <iostream>
#include <vector>

std::vector<int> fibs(int num) {
    std::vector<int> fib_vector;
    for (int i = 0; i < num; i++) {
        if (i == 0) {
            fib_vector.push_back(1);
        }
        else if (i == 1) {
            fib_vector.push_back(1);
        }
        else {
            fib_vector.push_back(fib_vector[i-1] + fib_vector[i-2]);
        }
    }
    return fib_vector;

}

int fib_recur(int index) {
    if (index == 0 || index == 1) {
        return 1;
    }
    else {
        return fib_recur(index - 1) + fib_recur(index - 2);
    }
}

int sum_recur(int number) {
    if (number == 1) {
        return 1;
    }
    else {
        return sum_recur(number - 1) + number;
    }
}