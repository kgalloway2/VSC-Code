#include <iostream>
#include <map>
#include <iterator>
#include <vector>
#include <string>

using namespace std;

int main() {
    map<char, int> letter_map;
    map<int, char> cipher_map;
    std::vector<char> letters = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    for (int i = 0; i <= 25; i++) {
        letter_map.insert(pair<char, int>(letters[i], i));
    }
    for (int i = 0; i <= 25; i++) {
        cipher_map.insert(pair<int, char>(i, letters[i]));
    }
    std::string pre_message;
    int shift;
    std::string post_message;

    std::cout << "What is the message to encrypt? (ALL CAPS)\n";
    std::getline(std::cin, pre_message);

    std::cout << "What is the amount of shift? (positive int)\n";
    std::cin >> shift;

    for (int j = 0; j < pre_message.size(); j++) {
        if (pre_message[j] == ' ') {
            post_message += " ";
        }
        else {
            int letter_index = letter_map[pre_message[j]];
            letter_index = (letter_index + shift) % 26;
            post_message += cipher_map[letter_index];
        }
    }

    std::cout << "The encrypted message is: \n"
              << post_message;

}