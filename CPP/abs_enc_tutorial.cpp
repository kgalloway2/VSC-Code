#include <iostream>
using namespace std;

class abstraction
{
    private:
        int a, b;

    public:

        // public setter function
        void set(int x, int y)
        {
            a = x;
            b = y;
        }

        // public getter function
        void display()
        {
            cout << "a = " << a << endl;
            cout << "b = " << b << endl;
        }
};

int main()
{
    abstraction obj;
    obj.set(1, 2);
    obj.display();
    return 0;
}