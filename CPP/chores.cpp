#include "chore_functions.hpp"
#include <iostream>

int main() {

    std::cout << "=================\n";
    std::cout << "  CHORE MANAGER\n";
    std::cout << "=================\n";
    bool exit_con = false;
    while (!exit_con) {
        int choice;
        std::cout << "OPTIONS:\n";
        std::cout << "1. VIEW CURRENT SCHEDULE\n";
        std::cout << "2. MANAGE SCHEDULES\n";
        std::cout << "3. MANAGE PEOPLE\n";
        std::cout << "4. MANAGE CHORES\n";
        std::cout << "5. EXIT \n\n";

        std::cout << "ENTER SELECTION:\n";
        std::cin >> choice;
        
        switch (choice) {
            case 1 :
                show_current_schedule(schedules[-1]);
                break;
            case 2 :
                generate_schedule_menu();
                break;
            case 3 :
                manage_people_menu();
                break;
            case 4 :
                manage_chores_menu();
                break;
            case 5 :
                exit_con = true;
                break;
            default:
                std::cout << "INVALID CHOICE. PLEASE TRY AGAIN.\n";
        }

    }
}