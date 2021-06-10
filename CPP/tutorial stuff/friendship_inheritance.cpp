#include <iostream>
using namespace std;

class Square;

class Rectangle {
    int width, height;
    public:
        Rectangle() {};
        Rectangle(int x, int y) : width(x), height(y) {};
        
        int area() { return width * height;};
        void convert (Square a);
        friend Rectangle duplicate (const Rectangle&);
};

Rectangle duplicate (const Rectangle& param) {
    Rectangle res;
    res.width = param.width * 2;
    res.height = param.height * 2;
    return res;
}

class Square {
    friend class Rectangle;
    private:
        int side;
    public:
        Square(int a) : side(a) {};
};

void Rectangle::convert(Square a) {
    width = a.side;
    height = a.side;
}

class Polygon {
    protected:
        int width, height;
    public:
        void set_values(int a, int b) {width = a, height = b;};
};

class Rectangle2: public Polygon {
    public:
        int area() { return width * height;};
};

class Triangle: public Polygon {
    public:
    int area() {return width * height / 2; };
};

class Mother {
    public:
        Mother() {cout << "Mother: no parameters\n";}
        Mother(int a) {cout << "Mother: int parameter\n";}
};

class Daughter: public Mother {
    public:
        Daughter(int a) {cout << "Daughter: int parameter\n\n";}
};

class Son : public Mother {
    public:
        Son(int a) : Mother(a) {cout << "Son: int parameter \n\n";}
};

class Polygon2 {
    protected:
        int width, height;
    public:
        Polygon2(int a, int b) : width(a), height(b) {}

};

class Output {
    public:
        static void print(int i);
};

void Output::print(int i) {
    cout << i << '\n';
}

class Rectangle3 : public Polygon2, public Output {
    public:
        Rectangle3(int a, int b) : Polygon2(a, b) {}
        int area() { return width * height;}
};

class Triangle2 : public Polygon2, public Output {
    public:
        Triangle2(int a, int b) : Polygon2(a, b) {}
        int area() { return width * height / 2;}
};

int main() {
    Rectangle rec1;
    Rectangle rec2(2, 3);
    rec1 = duplicate(rec2);
    cout << rec1.area() << "\n";
    
    Rectangle rect;
    Square sqr(4);
    rect.convert(sqr);
    cout << rect.area() << "\n";
    
    Rectangle2 rect2;
    Triangle trgl;
    rect2.set_values(4, 5);
    trgl.set_values(4, 5);
    cout << rect2.area() << '\n';
    cout << trgl.area() << '\n';

    Daughter kelly(0);
    Son bud(0);

    Rectangle3 rect3(4, 5);
    Triangle2 trgl2(4, 5);
    rect3.print(rect3.area());
    Triangle2::print(trgl2.area());

    return 0;
}