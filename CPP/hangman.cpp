#include <iostream>
#include <string>

using namespace std;

int main() {
    string word = "triple";
    string guessed_letters;
    string guess;
    string full_guess;

    for (int i = 0; i < word.size(); i++) {
        full_guess.append("_");
    }

    std::cout << "Welcome to Hangman!\n";
    int tries = 0;
    
    while (full_guess != word && tries < 10) {
        std::cout << "Please guess a letter: ";
        std::cin >> guess;
        int pos = word.find_first_of(guess);
        if (pos >= 0) {
            full_guess.replace(pos, 1, guess);
            std::cout << "Your current guess is " << full_guess << "\n";
        }
        else {
            std::cout << "That is not a letter in the word.\n";
            guessed_letters.append(guess);
            std::cout << "You have guessed the following letters: \n";
            for (int i = 0; i < guessed_letters.size(); i++) {
                std::cout << guessed_letters[i] << ", ";
            }
            std::cout << "\n";
            tries++;
        }
    }

    if (full_guess == word) {
        std::cout << "You win!\n";
    }
    else {
        std::cout << "You lose!\n";
    }
}