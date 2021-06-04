#include <iostream>
#include <vector>
#include <algorithm>
#include "chore_functions.hpp"

person::person(int new_id, int new_level, std::string new_name, std::vector<int> new_pref, int new_weight, int new_max_weight) {
    id_num = new_id;
    chore_level = new_level;
    name = new_name;
    preferred_chores = new_pref;
    weight = new_weight;
    max_weight = new_max_weight;
    num_people++;
}

person::~person() {
    num_people--;
}
void person::update_id(int new_id) {
    id_num = new_id;
}
void person::update_level(int new_level) {
    chore_level = new_level;
}
void person::update_name(std::string new_name) {
    name = new_name;
}
void person::update_pref(std::vector<int> new_pref) {
    preferred_chores = new_pref;
}
void person::update_weight(int new_weight) {
    weight = new_weight;
}
void person::update_max_weight(int new_max_weight) {
    max_weight = new_max_weight;
}

chore::chore(int new_id, int new_level, std::string new_name, std::string new_freq, int new_weight) {
    id_num = new_id;
    chore_level = new_level;
    name = new_name;
    frequency = new_freq;
    weight = new_weight;
}

chore::~chore() {
    
}
void chore::update_id(int new_id) {
    id_num = new_id;
}
void chore::update_level(int new_level) {
    chore_level = new_level;
}
void chore::update_name(std::string new_name) {
    name = new_name;
}
void chore::update_frequency(std::string new_freq) {
    frequency = new_freq;
}
void chore::update_weight(int new_weight) {
    weight = new_weight;
}

schedule::schedule(int new_num_people, std::vector<person> new_people, std::vector<chore> new_chores) {
    week_schedule = {};
    num_people = new_num_people;
    people = new_people;
    chores = new_chores;

    for (int i = 0; i < num_people + 1; i++) {
        week_schedule.push_back({});
    }
    std::vector<int> unassigned_chores = {};
    for (int c = 0; c < chores.size(); c++) {
        bool assigned = false;
        chore current_chore = chores[c];
        
        for (int p = 0; p < people.size(); p++) {
            if (!assigned) {
                person current_person = people[p];
                if (current_chore.chore_level <= current_person.chore_level) {
                    if (current_chore.weight + current_person.weight <= current_person.max_weight) {
                        auto chore_pos = std::find(current_person.preferred_chores.begin(), current_person.preferred_chores.end(), current_chore.id_num);
                        if (chore_pos != current_person.preferred_chores.end()) {
                            week_schedule[p].push_back(current_chore.id_num);
                            assigned = true;
                        }
                    }
                }
            }
        }
        if (!assigned) {
            unassigned_chores.push_back(c);
        }
    }
    for (int u = 0; u <= unassigned_chores.size(); u++) {
        chore current_chore = chores[unassigned_chores[u]];
        bool assigned = false;
        if (!assigned) {
            for (int p = 0; p < people.size(); p++) {
                person current_person = people[p];
                if (current_chore.chore_level <= current_person.chore_level) {
                    if (current_person.weight <= current_person.max_weight) {
                        week_schedule[p].push_back(current_chore.id_num);
                        assigned = true;
                    }
                }
            }
        }
        if (!assigned) {
            week_schedule[-1].push_back(current_chore.id_num);
        }
    }
    
}
schedule::~schedule() {

}

void schedule::show_schedule() {
    for (int i = 0; i < people.size(); i++) {
        std::vector<int> current_assignments = week_schedule[i];
        person current_person = people[i];
        std::cout << "The chores for " << current_person.name << " are: \n";
        for (int a = 0; a < current_assignments.size(); a++) {
            chore current_chore = chores[current_assignments[a]];
            std::cout << "\t" << current_chore.name << "\n";
        }
    }
    std::vector<int> current_assignments = week_schedule[-1];
    std::cout << "The unassigned chores for this week are: \n";
    for (int a = 0; a < current_assignments.size(); a++) {
        chore current_chore = chores[current_assignments[a]];
        std::cout << "\t" << current_chore.name << "\n";
    }
}


void show_current_schedule(schedule input_schedule) {
    input_schedule.show_schedule();
}

void generate_schedule_menu() {
    std::cout << "=================\n";
    std::cout << " SCHEDULE MANAGER\n";
    std::cout << "=================\n";
    bool exit_con = false;
    while (!exit_con) {
        schedule new_schedule = schedule(num_people, people, chores);
        int choice;
        new_schedule.show_schedule();
        std::cout << "MAKE THIS THE CURRENT SCHEDULE? \n";
        std::cout << "1. YES\n";
        std::cout << "2. NO\n";
        std::cout << "3. EXIT\n";
        std::cin >> choice;
        
        switch (choice) {
            case 1 :
                schedules.push_back(new_schedule);
                break;
            case 2 :
                std::cout << "SCHEDULE NOT SELECTED.\n";
                break;
            case 3 :
                exit_con = true;
            default:
                std::cout << "INVALID CHOICE. PLEASE TRY AGAIN.\n";
        }

    }
}

void manage_people_menu() {
    std::cout << "=================\n";
    std::cout << "  PEOPLE MANAGER\n";
    std::cout << "=================\n";
    bool exit_con = false;
    while (!exit_con) {
        int choice;
        new_schedule.show_schedule();
        std::cout << "OPTIONS: \n";
        std::cout << "1. MAKE NEW PERSON\n";
        std::cout << "2. DELETE PERSON\n";
        std::cout << "3. UPDATE PERSON\n";
        std::cout << "4. EXIT\n";
        std::cin >> choice;
        
        switch (choice) {
            case 1 :
                schedules.push_back(new_schedule);
                break;
            case 2 :
                std::cout << "SCHEDULE NOT SELECTED.\n";
                break;
            case 3 :
                exit_con = true;
            default:
                std::cout << "INVALID CHOICE. PLEASE TRY AGAIN.\n";
        }

    }
}

void manage_chores_menu() {

}