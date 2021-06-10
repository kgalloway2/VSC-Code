#include <iostream>
using namespace std;

class Polygon {
    protected:
        int width, height;
    public:
        void set_values(int a, int b) {width = a; height = b;}
        virtual int area() {return 0;}
};

class Rectangle: public Polygon {
    public:
        int area() {return width * height;}
};

class Triangle: public Polygon {
    public:
        int area() {return width * height / 2;}
};


// the following is an abstract base class since it has
// at least one pure virtual funtion
class Polygon2 {
    protected:
        int width, height;
    public:
        void set_values (int a, int b) {width = a; height = b;}
        virtual int area() =0;
};
// it cannot be used to instantiate objects, but can be inherited from
// it can also be used to create pointers to itself

class Rectangle2 : public Polygon2 {
    public:
        int area(void) {return (width * height);}
};

class Triangle2 : public Polygon2 {
    public:
        int area(void) {return (width * height / 2);}
};


int main() {
    Rectangle rect;
    Triangle trgl;
    Polygon poly;
    Polygon * ppoly1 = &rect;
    Polygon * ppoly2 = &trgl;
    Polygon * ppoly3 = &poly;
    ppoly1->set_values(4, 5);
    ppoly2->set_values(4, 5);
    ppoly3->set_values(4, 5);
    cout << ppoly1->area() << "\n";
    cout << ppoly2->area() << "\n";
    cout << ppoly3->area() << '\n';

    Rectangle2 rect2;
    Triangle2 trgl2;
    Polygon2 * ppoly_rect2 = &rect2;
    Polygon2 * ppoly_trgl2 = & trgl2;
    ppoly_rect2->set_values(4, 5);
    ppoly_trgl2->set_values(4, 5);
    cout << ppoly_rect2->area() << '\n';
    cout << ppoly_trgl2->area() << '\n';

    return 0;
}