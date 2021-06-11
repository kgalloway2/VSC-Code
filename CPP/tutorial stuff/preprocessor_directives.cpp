#include <iostream>
#define MAX_NUMBER 100
#define getmax(a, b) (a>b? a : b)

using namespace std;


int main() {
    cout << MAX_NUMBER << '\n';
    int x = 5, y;
    y = getmax(x,2);
    cout << y << endl;
    cout << getmax(7,x) << endl;
    return 0;
}