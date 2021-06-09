#include <iostream>

using namespace std;

union unioned_data {
        int integer;
        double real;
        // these two variables share a space in memory which can only be set
        // to one value at a time, but of either type
    };

// makes a new type that can take values from a set list
enum notes {A, B, C, D, E, F, G};

// the values can be given integer values as well
//if the first is declared, the others will be assumed from it
enum months_t { january=1, february, march, april,
                may, june, july, august,
                september, october, november, december};

int main() {
    // types can be aliased so you can refer to them with different names
    typedef char character;
    typedef int number;

    character initial;
    number count;

    // you can also use this syntax
    using sentence = std::string;
    using ten_num_vec = int [10];

    notes note1 = A;

    months_t month_3 = march;

    if (month_3 == 3) {
        cout << "It worked.\n";
    }


}