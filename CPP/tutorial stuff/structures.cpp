#include <iostream>

struct card {
        int mana_value;
        std::string name;
    };

void print_card(card my_card);

struct deck {
    std::string name;
    card commander;
    int power_level;
};

int main() {
    card card1;
    std::cout << "Enter card name: ";
    std::getline(std::cin, card1.name);
    std::cout << "Enter mana value: ";
    std::cin >> card1.mana_value;

    print_card(card1);

    card * card_pointer = &card1;
    std::cout << "Using a pointer: " << card_pointer->mana_value << '\n';

}

void print_card(card my_card) {
    std::cout << "The card " << my_card.name << " has a mana value of " << my_card.mana_value << ".\n";
}