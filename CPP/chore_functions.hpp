#include <iostream>
#include <vector>

int num_people = 0;
std::vector<person> people = {};
std::vector<chore> chores = {};
std::vector<schedule> schedules = {};

class person {
    public:
    int id_num;
    int chore_level;
    std::string name;
    std::vector<int> preferred_chores;
    int weight;
    int max_weight;

    person(int new_id, int new_level, std::string new_name, std::vector<int> new_pref, int new_weight, int new_max_weight);
    ~person();
    void update_id(int new_id);
    void update_level(int new_level);
    void update_name(std::string new_name);
    void update_pref(std::vector<int> new_pref);
    void update_weight(int new_weight);
    void update_max_weight(int new_max_weight);
};

class chore {
    public:
    int id_num;
    int chore_level;
    std::string name;
    std::string frequency;
    int weight;

    chore(int new_id, int new_level, std::string new_name, std::string new_freq, int new_weight);
    ~chore();
    void update_id(int new_id);
    void update_level(int new_level);
    void update_name(std::string new_name);
    void update_frequency(std::string new_freq);
    void update_weight(int new_weight);
};

class schedule {
    public:
    std::vector<std::vector<int>> week_schedule;
    int num_people;
    std::vector<person> people;
    std::vector<chore> chores;

    schedule(int new_num_people, std::vector<person> new_people, std::vector<chore> new_chores);
    ~schedule();
    void show_schedule();
};

void main_menu();
void show_current_schedule(schedule input_schedule);
void generate_schedule_menu();
void manage_people_menu();
void manage_chores_menu();