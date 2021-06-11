#include <iostream>
#include <exception>
using namespace std;

class myexception : public exception {
    virtual const char* what() const throw() {
        return "My exception happened";
    }
} myex;

int main() {
    try {
        throw 20;
    }
    catch (int e) {
        cout << "An exception occured. Exception Nr. " << e << '\n';
    }

    try {
        throw myex;
    }
    catch (exception& e) {
        cout << e.what() << '\n';
    }

    try {
        int* myarray = new int[1000];
    }
    catch (exception& e) {
        cout << "Standard exception: " << e.what() << endl;
    }

    return 0;
}