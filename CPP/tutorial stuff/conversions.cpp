#include <iostream>
using namespace std;

class A {};

class B {
    public:
        // conversion from A (constructor):
        explicit B(const A& x) {}
        // conversion from A (assignment):
        B& operator= (const A& x) {return *this;}
        // conversion to A (type-cast operator):
        operator A() {return A();}
};

void fn (B x) {}

int main() {
    A foo;
    B bar (foo);
    bar = foo;
    foo = bar;      
    // fn(foo) not allowed for explicit constructor
    fn(bar);
    
    return 0;
}