#include <iostream>
#include <vector>
#include <algorithm>

class address {
    std::string name;
    std::string street_address;
    std::string city;
    std::string state;
    int zip_code;

    public:
        address(std::string new_name, std::string new_street, std::string new_city, std::string new_state, int new_zip);

        void update_name(std::string new_name);
        void update_street(std::string new_street);
        void update_city(std::string new_city);
        void update_state(std::string new_state);
        void update_zip(int new_zip);

        void print_address();
};

class address_book {
    std::vector<address> addresses;

    public:
        address_book(std::vector<address> new_addresses);

        void add_address(address new_address);
        void delete_address(int address_index);
        void update_address(int old_address_index, address updated_address);
        void show_book();

};