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
}

person::~person() {
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
    my_chores = new_chores;
    for (int i = 0; i < num_people + 1; i++) {
        week_schedule.push_back({});
    }
    std::vector<int> unassigned_chores = {};
    for (int c = 0; c < chores.size(); c++) {
        bool assigned = false;
        chore current_chore = my_chores[c];
        
        for (int p = 0; p < people.size(); p++) {
            if (!assigned) {
                person current_person = people[p];
                if (current_chore.chore_level <= current_person.chore_level) {
                    if (current_chore.weight + current_person.weight <= current_person.max_weight) {
                        auto chore_pos = std::find(current_person.preferred_chores.begin(), current_person.preferred_chores.end(), current_chore.id_num);
                        if (chore_pos != current_person.preferred_chores.end()) {
                            week_schedule[p].push_back(current_chore.id_num);
                            current_person.update_weight(current_chore.weight);
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
    for (int u = 0; u < unassigned_chores.size(); u++) {
        chore current_chore = my_chores[unassigned_chores[u]];
        bool assigned = false;
        if (!assigned) {
            for (int p = 0; p < people.size(); p++) {
                person current_person = people[p];
                if (current_chore.chore_level <= current_person.chore_level) {
                    if (current_person.weight <= current_person.max_weight) {
                        week_schedule[p].push_back(current_chore.id_num);
                        current_person.update_weight(current_chore.weight);
                        assigned = true;
                    }
                }
            }
        }
        if (!assigned) {
            int n = week_schedule.size();
            week_schedule[n - 1].push_back(current_chore.id_num);
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
            std::cout << "\t" << my_chores[current_assignments[a]].name << "\n";
        }
    }
    int n = week_schedule.size();
    std::vector<int> current_assignments = week_schedule[n - 1];
    std::cout << "The unassigned chores for this week are: \n";
    for (int a = 0; a < current_assignments.size(); a++) {
        std::cout << "\t" << my_chores[current_assignments[a]].name << "\n";
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
        std::cout << "\nMAKE THIS THE CURRENT SCHEDULE? \n";
        std::cout << "1. YES\n";
        std::cout << "2. NO\n";
        std::cout << "3. EXIT\n";
        std::cin >> choice;
        
        switch (choice) {
            case 1 :
                schedules.push_back(new_schedule);
                exit_con = true;
                break;
            case 2 :
                std::cout << "SCHEDULE NOT SELECTED.\n";
                exit_con = true;
                break;
            case 3 :
                exit_con = true;
                break;
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
        std::cout << "\nOPTIONS: \n";
        std::cout << "1. MAKE NEW PERSON\n";
        std::cout << "2. DELETE PERSON\n";
        std::cout << "3. UPDATE PERSON\n";
        std::cout << "4. EXIT\n";
        std::cin >> choice;
        
        switch (choice) {
            case 1 :
                {int cur_num_people = people.size();
                int id_num;
                if (cur_num_people > 0) {
                    id_num = cur_num_people + 1;
                }
                else {
                    id_num  = 0;
                }
                
                std::string name;
                std::cout << "What is this person's name?\n";
                std::cin.ignore();
                std::getline(std::cin, name);

                int chore_level;
                std::cout << "What is their chore level?\n";
                std::cin >> chore_level;
                
                std::vector<int> preferred_chores = {};
                
                int weight = 0;
                
                int max_weight;
                std::cout << "How many chores can they do?\n";
                std::cin >> max_weight;

                person new_person = person(id_num, chore_level, name, preferred_chores, weight, max_weight);
                people.push_back(new_person);
                num_people++;
                std::cout << "New person added!" << std::endl;
                break;}
            case 2 :
                {for (int i = 0; i < people.size(); i++) {
                    std::cout << i << ": " << people[i].name << '\n';
                }
                int delete_number;
                std::cout << "Delete which person? (input number)\n";
                std::cin >> delete_number; 
                people.erase(people.begin() + delete_number);
                num_people--;
                std::cout << "Person deleted!\n";
                break;}
            case 3 :
                {for (int i = 0; i < people.size(); i++) {
                    std::cout << i << ": " << people[i].name << '\n';
                }
                int update_number;
                std::cout << "Update which person? (input number)\n";
                std::cin >> update_number; 
                person temp_person = people[update_number];
                
                std::string name;
                std::cout << "New name? (enter 'NA' if no update)\n";
                std::cin.ignore();
                std::getline(std::cin, name);
                if (name != "NA") {
                    temp_person.update_name(name);
                }

                int chore_level;
                std::cout << "New chore level? (enter '-1' if no update)\n";
                std::cin >> chore_level;
                if (chore_level != -1) {
                    temp_person.update_level(chore_level);
                }
                
                std::vector<int> preferred_chores;
                int add_chore;
                std::cout << "Add preferred chore? (enter '-1' if no update)\n";
                std::cin >> add_chore;
                preferred_chores.push_back(add_chore);
                if (add_chore != -1) {
                    temp_person.update_pref(preferred_chores);
                }
                
                int max_weight;
                std::cout << "New max weight? (enter '-1' if no update)\n";
                std::cin >> max_weight;
                if (max_weight != -1) {
                    temp_person.update_max_weight(max_weight);
                }
                break;}
            case 4 :
                exit_con = true;
                break;
            default:
                std::cout << "INVALID CHOICE. PLEASE TRY AGAIN.\n";
        }

    }
}

void manage_chores_menu() {
    std::cout << "=================\n";
    std::cout << "  CHORE MANAGER\n";
    std::cout << "=================\n";
    bool exit_con = false;
    while (!exit_con) {
        int choice;
        std::cout << "\nOPTIONS: \n";
        std::cout << "1. MAKE NEW CHORE\n";
        std::cout << "2. DELETE CHORE\n";
        std::cout << "3. UPDATE CHORE\n";
        std::cout << "4. EXIT\n";
        std::cin >> choice;
        
        switch (choice) {
            case 1 :
                {int cur_num_chores = chores.size();
                int id_num;
                if (cur_num_chores > 0) {
                    id_num = cur_num_chores + 1;
                }
                else {
                    id_num  = 0;
                }
                
                std::string name;
                std::cout << "What is this chores's name?\n";
                std::cin.ignore();
                std::getline(std::cin, name);

                int chore_level;
                std::cout << "What is the chore level?\n";
                std::cin >> chore_level;
                                
                std::string freq;
                std::cout << "What is this chores's frequency?\n";
                std::cin.ignore();
                std::getline(std::cin, freq);

                int weight;
                std::cout << "What is the chore weight?\n";
                std::cin >> weight;

                chore new_chore = chore(id_num, chore_level, name, freq, weight);
                chores.push_back(new_chore);
                std::cout << "New chore added!" << std::endl;
                break;}
            case 2 :
                {for (int i = 0; i < chores.size(); i++) {
                    std::cout << i << ": " << chores[i].name << '\n';
                }
                int delete_number;
                std::cout << "Delete which chore? (input number)\n";
                std::cin >> delete_number; 
                chores.erase(chores.begin() + delete_number);
                std::cout << "Chore deleted!\n";
                break;}
            case 3 :
                {for (int i = 0; i < chores.size(); i++) {
                    std::cout << i << ": " << chores[i].name << '\n';
                }
                int update_number;
                std::cout << "Update which chore? (input number)\n";
                std::cin >> update_number; 
                chore temp_chore = chores[update_number];
                
                std::string name;
                std::cout << "New name? (enter 'NA' if no update)\n";
                std::cin.ignore();
                std::getline(std::cin, name);
                if (name != "NA") {
                    temp_chore.update_name(name);
                }

                int chore_level;
                std::cout << "New chore level? (enter '-1' if no update)\n";
                std::cin >> chore_level;
                if (chore_level != -1) {
                    temp_chore.update_level(chore_level);
                }
                                
                std::string freq;
                std::cout << "New frequency? (enter 'NA' if no update)\n";
                std::cin.ignore();
                std::getline(std::cin, freq);
                if (name != "NA") {
                    temp_chore.update_frequency(freq);
                }
                
                int weight;
                std::cout << "New weight? (enter '-1' if no update)\n";
                std::cin >> weight;
                if (weight != -1) {
                    temp_chore.update_weight(weight);
                }
                break;}
            case 4 :
                exit_con = true;
                break;
            default:
                std::cout << "INVALID CHOICE. PLEASE TRY AGAIN.\n";
        }

    }
}


int num_people = 0;
std::vector<person> people;
std::vector<chore> chores;
std::vector<schedule> schedules = {};