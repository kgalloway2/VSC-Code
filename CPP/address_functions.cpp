#include <iostream>
#include <vector>
#include <algorithm>
#include "address_functions.hpp"

address::address(std::string new_name, std::string new_street, std::string new_city, std::string new_state, int new_zip) {
    name = new_name;
    street_address = new_street;
    city = new_city;
    state = new_state;
    zip_code = new_zip;
    }


void address::update_name(std::string new_name) {
    name = new_name;
}
void address::update_street(std::string new_street) {
    street_address = new_street;
}
void address::update_city(std::string new_city) {
    city = new_city;
}
void address::update_state(std::string new_state) {
    state = new_state;
}
void address::update_zip(int new_zip) {
    zip_code = new_zip;
}

void address::print_address() {
    std::cout << "Name: " << name << "\n";
    std::cout << "Street Address: " << street_address << "\n";
    std::cout << "City: " << city << "\n";
    std::cout << "State: " << state << "\n";
    std::cout << "Zip Code: " << zip_code << "\n";
}

address_book::address_book(std::vector<address> new_addresses) {
    addresses = new_addresses;
}

void address_book::add_address(address new_address) {
    addresses.push_back(new_address);
}
void address_book::delete_address(int address_index) {
    auto index = addresses.begin() + address_index;
    addresses.erase(index);
}
void address_book::update_address(int old_address_index, address updated_address) {
    auto index = addresses.begin() + old_address_index;
    addresses.erase(index);
    addresses.push_back(updated_address);
}

void address_book::show_book() {
    for (int i = 0; i < addresses.size(); i++) {
        addresses[i].print_address();
    }
}
