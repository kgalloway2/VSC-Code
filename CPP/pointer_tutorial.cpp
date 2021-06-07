#include <iostream>
using namespace std;

int main()
{
    int val1, val2;
    int * mypointer;

    mypointer = &val1;
    *mypointer = 10;
    mypointer = &val2;
    *mypointer = 20;
    cout <<"firstvalue is " << val1 << '\n';
    cout <<"secondvalue is " << val2 << '\n';
}