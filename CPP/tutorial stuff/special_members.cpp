#include <iostream>

class without_explicit_constructor {
    public:
        int total;
        void accumulate(int x) { total += x; }
};

class with_explicit_constructor {
    public:
        int total;

        with_explicit_constructor(int initial_value) : total(initial_value) { };

        void accumulate (int x) { total += x; } 
};

class with_default_and_argument {
    std::string data;
    public:
        with_default_and_argument(const std::string& str) : data(str) {};
        with_default_and_argument() {};
        const std::string& content() const {return data;};
};

class destructor {
    std::string * ptr;

    public:
        // constructors:
        destructor() : ptr(new std::string) {};
        destructor(const std::string& str) : ptr(new std::string(str)) {};

        // destructor:
        ~destructor() {delete ptr;};

        // access content:
        const std::string& content() const {return *ptr;};
};

class copy_stuff_not_explicit {
    public:
        int a, b; std::string c;
};

class copy_defined {
    std::string * ptr;

    public:
        copy_defined(const std::string& str) : ptr(new std::string(str)) {};
        ~copy_defined() {delete ptr;};
        // copy constructor
        copy_defined(const copy_defined& x) : ptr(new std::string(x.content())) {};
        // access content
        const std::string& content() const {return *ptr;};
};

int main() {

    // without an explicit constructor, the compliler assumes a default one
    // these objects are constructed automatically
    without_explicit_constructor example1;

    // when an explicit constructor is declared, it must be used
    with_explicit_constructor example2(200);

    // when both are declared, both can be used
    with_default_and_argument example3; // contains no data
    with_default_and_argument example4("example"); // contains the argument passed as data

    // using a destructor
    destructor example5;
    destructor example6("example");
    // at the end of main, the destructor is called for each of these

    // copying when no copy method is defined
    destructor example7 = example6;
    // this only copied pointers so both 6 and 7 point at the same place in memory
    // but if we define a custom copy method, it copies data to a new spot in memory
    copy_defined example8("example");
    copy_defined example9 = example8;
}