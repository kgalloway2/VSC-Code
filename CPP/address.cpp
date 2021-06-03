#include <iostream>
#include <vector>
#include <algorithm>
#include "address_functions.hpp"

int main() {
    address a1 = address("John Doe", "123 Street", "New York", "NY", 99999);
    address a2 = address("Jane Doe", "123 Street", "New York", "NY", 99999);
    address a3 = address("John Smith", "369 Avenue", "Birmingham", "AL", 35599);
    address a4 = address("Ricardo Montalbon", "485 Rock Road", "Anchorage", "AK", 93649);
    address a5 = address("Yippy Yippers", "99 Bollocks Drive", "Elevens", "CA", 12345);

    address_book my_address_book = address_book({a1, a2, a3, a4});

    my_address_book.show_book();
    std::cout << "-------------------------\n";

    my_address_book.add_address(a5);
    std::cout << "-------------------------\n";

    my_address_book.show_book();
    std::cout << "-------------------------\n";

    my_address_book.delete_address(3);
    std::cout << "-------------------------\n";

    my_address_book.show_book();
    std::cout << "-------------------------\n";

    my_address_book.update_address(4, a4);
    std::cout << "-------------------------\n";

    my_address_book.show_book();
    std::cout << "-------------------------\n";
}