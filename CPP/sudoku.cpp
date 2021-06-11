// board generator not generating solvable board every time

#include <iostream>
#include <random>
#include <vector>
#include <algorithm>

void display_board(int current_board[][9]);

bool check_valid_move(int current_board[][9], int position[], int entry);

void generate_sudoku_board(int current_board[][9]);

// this is for filling the diagonal blocks randomly. it doesn't check for valid moves because it doesn't have to
void fill_block_one(int current_board[][9], int start[], int end[]);

// this is for filling the off diagonal blocks with valid moves
void fill_block_two(int current_board[][9], int start[], int end[]);

// this is to remove entries form a puzzle to make it ready to solve
void remove_entries(int current_board[][9], int number_to_remove);

std::vector<int> distinct_random_numbers(int number_of_numbers);

bool check_win (int current_board[][9]);

int main() {

    int my_board[9][9];
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            my_board[i][j] = 0;
        }
    }
    generate_sudoku_board(my_board);

    bool game_over = false;
    int num_to_place;
    int position[2];
    int strikes = 0;
    while (!game_over) {
        std::cout << "Here is your board:\n";
        display_board(my_board);
        std::cout << "Number to place: ";
        std::cin >> num_to_place;
        std::cout << "Row to place in: ";
        std::cin >> position[0];
        std::cout << "Column to place in: ";
        std::cin >> position[1];
        if (check_valid_move(my_board, position, num_to_place)) {
            my_board[position[0]][position[1]] = num_to_place;
        }
        else {
            strikes++;
            std::cout << "That is an invalid move. You have " << strikes << " strikes.\n";
        }
        if (strikes >= 3) {
            std::cout << "You have lost. Please try again.";
            game_over = true;
        }
        if (check_win(my_board)) {
            std::cout << "You have won! Congratulations!";
            game_over = true; 
        }
    }
}

void display_board(int current_board[][9]) {
    std::cout << "   0  1  2 | 3  4  5 | 6  7  8 \n";
    std::cout << "0| " << current_board[0][0] << "  " << current_board[0][1] << "  " << current_board[0][2] << " | " << current_board[0][3] << "  " << current_board[0][4] << "  " << current_board[0][5] << " | " << current_board[0][6] << "  " << current_board[0][7] << "  " << current_board[0][8] << " \n";
    std::cout << "1| " << current_board[1][0] << "  " << current_board[1][1] << "  " << current_board[1][2] << " | " << current_board[1][3] << "  " << current_board[1][4] << "  " << current_board[1][5] << " | " << current_board[1][6] << "  " << current_board[1][7] << "  " << current_board[1][8] << " \n";
    std::cout << "2| " << current_board[2][0] << "  " << current_board[2][1] << "  " << current_board[2][2] << " | " << current_board[2][3] << "  " << current_board[2][4] << "  " << current_board[2][5] << " | " << current_board[2][6] << "  " << current_board[2][7] << "  " << current_board[2][8] << " \n";
    std::cout << " |---------|---------|---------\n";
    std::cout << "3| " << current_board[3][0] << "  " << current_board[3][1] << "  " << current_board[3][2] << " | " << current_board[3][3] << "  " << current_board[3][4] << "  " << current_board[3][5] << " | " << current_board[3][6] << "  " << current_board[3][7] << "  " << current_board[3][8] << " \n";
    std::cout << "4| " << current_board[4][0] << "  " << current_board[4][1] << "  " << current_board[4][2] << " | " << current_board[4][3] << "  " << current_board[4][4] << "  " << current_board[4][5] << " | " << current_board[4][6] << "  " << current_board[4][7] << "  " << current_board[4][8] << " \n";
    std::cout << "5| " << current_board[5][0] << "  " << current_board[5][1] << "  " << current_board[5][2] << " | " << current_board[5][3] << "  " << current_board[5][4] << "  " << current_board[5][5] << " | " << current_board[5][6] << "  " << current_board[5][7] << "  " << current_board[5][8] << " \n";
    std::cout << " |---------|---------|---------\n";
    std::cout << "6| " << current_board[6][0] << "  " << current_board[6][1] << "  " << current_board[6][2] << " | " << current_board[6][3] << "  " << current_board[6][4] << "  " << current_board[6][5] << " | " << current_board[6][6] << "  " << current_board[6][7] << "  " << current_board[6][8] << " \n";
    std::cout << "7| " << current_board[7][0] << "  " << current_board[7][1] << "  " << current_board[7][2] << " | " << current_board[7][3] << "  " << current_board[7][4] << "  " << current_board[7][5] << " | " << current_board[7][6] << "  " << current_board[7][7] << "  " << current_board[7][8] << " \n";
    std::cout << "8| " << current_board[8][0] << "  " << current_board[8][1] << "  " << current_board[8][2] << " | " << current_board[8][3] << "  " << current_board[8][4] << "  " << current_board[8][5] << " | " << current_board[8][6] << "  " << current_board[8][7] << "  " << current_board[8][8] << " \n";
}

bool check_valid_move(int current_board[][9], int position[], int entry) {
    for (int i = 0; i < 9; i ++) {
        if ((current_board[position[0]][i] == entry) || (current_board[i][position[1]] == entry)) {
            return false;
        }
    }
    if (position[0] <=2) {
        if (position[1] <=2) {
            for (int i = 0; i <= 2; i++) {
                for (int j = 0; j <= 2; j++) {
                    if (current_board[i][j] == entry) {
                        return false;
                    }
                }
            }
        }
        else if (position[1] <= 5) {
            for (int i = 0; i <= 2; i++) {
                for (int j = 3; j <= 5; j++) {
                    if (current_board[i][j] == entry) {
                        return false;
                    }
                }
            }
        }
        else {
            for (int i = 0; i <= 2; i++) {
                for (int j = 6; j <= 8; j++) {
                    if (current_board[i][j] == entry) {
                        return false;
                    }
                }
            }
        }
    }
    else if (position[0] <= 5) {
        if (position[1] <=2) {
            for (int i = 3; i <= 5; i++) {
                for (int j = 0; j <= 2; j++) {
                    if (current_board[i][j] == entry) {
                        return false;
                    }
                }
            }
        }
        else if (position[1] <= 5) {
            for (int i = 3; i <= 5; i++) {
                for (int j = 3; j <= 5; j++) {
                    if (current_board[i][j] == entry) {
                        return false;
                    }
                }
            }
        }
        else {
            for (int i = 3; i <= 5; i++) {
                for (int j = 6; j <= 8; j++) {
                    if (current_board[i][j] == entry) {
                        return false;
                    }
                }
            }        
        }
    }
    else {
        if (position[1] <=2) {
            for (int i = 6; i <= 8; i++) {
                for (int j = 0; j <= 2; j++) {
                    if (current_board[i][j] == entry) {
                        return false;
                    }
                }
            }
        }
        else if (position[1] <= 5) {
            for (int i = 6; i <= 8; i++) {
                for (int j = 3; j <= 5; j++) {
                    if (current_board[i][j] == entry) {
                        return false;
                    }
                }
            }
        }
        else {
            for (int i = 6; i <= 8; i++) {
                for (int j = 6; j <= 8; j++) {
                    if (current_board[i][j] == entry) {
                        return false;
                    }
                }
            }        
        }
    }

    return true;
}

void generate_sudoku_board(int current_board[][9]) {
    int start[] {0,0};
    int end[] {2,2};
    fill_block_one(current_board, start, end);
    start[0] = 3;
    start[1] = 3;
    end[0] = 5;
    end[1] = 5;
    fill_block_one(current_board, start, end);
    start[0] = 6;
    start[1] = 6;
    end[0] = 8;
    end[1] = 8;
    fill_block_one(current_board, start, end);

    start[0] = 0;
    start[1] = 3;
    end[0] = 2;
    end[1] = 5;
    fill_block_two(current_board, start, end);
    start[0] = 0;
    start[1] = 6;
    end[0] = 2;
    end[1] = 8;
    fill_block_two(current_board, start, end);
    start[0] = 3;
    start[1] = 6;
    end[0] = 5;
    end[1] = 8;
    fill_block_two(current_board, start, end);

    start[0] = 6;
    start[1] = 0;
    end[0] = 6;
    end[1] = 2;
    fill_block_two(current_board, start, end);
    start[0] = 6;
    start[1] = 3;
    end[0] = 8;
    end[1] = 5;
    fill_block_two(current_board, start, end);
    start[0] = 3;
    start[1] = 0;
    end[0] = 5;
    end[1] = 2;
    fill_block_two(current_board, start, end);

    remove_entries(current_board, 30);
}

void fill_block_one(int current_board[][9], int start[], int end[]) {
    std::vector<int> entries =  {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int temp_entry_index;
    int temp_entry;
    int cur_pos[] {start[0], start[1]};
    int count = 9;
    while (count > 0) {
        temp_entry_index = rand() % count;
        temp_entry = entries[temp_entry_index];
        current_board[cur_pos[0]][cur_pos[1]] = temp_entry;
        entries.erase(entries.begin() + temp_entry_index);
        if (cur_pos[1] == end[1]) {
            cur_pos[0] = cur_pos[0] + 1;
            cur_pos[1] = start[1];
        }
        else {
            cur_pos[1] = cur_pos[1] + 1;
        }
        count--;
    }
}

void fill_block_two(int current_board[][9], int start[], int end[]) {
    std::vector<int> entries =  {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int cur_pos[] {start[0], start[1]};
    int count = 9;
    while (count > 0) {
        for (int const& number : entries) {
            if (check_valid_move(current_board, cur_pos, number)) {
                current_board[cur_pos[0]][cur_pos[1]] = number;
                break;
            } 
        }
        if (cur_pos[1] == end[1]) {
            cur_pos[0] = cur_pos[0] + 1;
            cur_pos[1] = start[1];
        }
        else {
            cur_pos[1] = cur_pos[1] + 1;
        }
        count--;
    }
}

void remove_entries(int current_board[][9], int number_to_remove) {
    std::vector<int> indices = distinct_random_numbers(number_to_remove);
    for (int i = 0; i < number_to_remove; i++) {
        int r_index = indices[i] % 9;
        int q_index = (indices[i] - r_index) / 9;
        std::cout << indices[i] << ", q: " << q_index << ", r: " << r_index << "\n";
        current_board[q_index][r_index] = 0;
    }
}

std::vector<int> distinct_random_numbers(int number_of_numbers) {
    std::vector<int> nums;
    int count = 0;
    while (count < number_of_numbers) {
        int potential_number = rand() % 81;
        bool duplicate = false;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == potential_number) {
                duplicate = true;
            }
        }
        if (!duplicate) {
            nums.push_back(potential_number);
            count++;
        }
    }
    return nums;
}

bool check_win (int current_board[][9]) {
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            int position[] {i, j};
            if (current_board[i][j] == 0) {
                return false;
            }
            else if (!check_valid_move(current_board, position, current_board[i][j])) {
                return false;
            }
        }
    }
    return true;

}

