function generate_blank_board()
    board = []
    for i in 1:9
        push!(board, 0)
    end
    return board
end

function display_board(board)
    for i in 1:9
        if (board[i] == -1)
            print("|O")
        elseif (board[i] == 1)
            print("|X")
        elseif (board[i] == 0)
            print("|_")
        end
        if (i % 3 == 0)
            print("\n")
        end
    end
end

function num_Os(board)
    count = 0
    for i in board
        if (i == -1)
            count += 1
        end
    end
    return count
end

function num_Xs(board)
    count = 0
    for i in board
        if (i == 1)
            count += 1
        end
    end
    return count
end

function is_X_win(board)
    if (board[3] == board[5] == board[7] == 1)
        return true
    elseif (board[1] == board[2] == board[3] == 1)
        return true
    elseif (board[4] == board[5] == board[6] == 1)
        return true
    elseif (board[7] == board[8] == board[9] == 1)
        return true
    elseif (board[1] == board[4] == board[7] == 1)
        return true
    elseif (board[2] == board[5] == board[8] == 1)
        return true
    elseif (board[3] == board[6] == board[9] == 1)
        return true
    elseif (board[1] == board[5] == board[9] == 1)
        return true
    end
    return false
end

function is_O_win(board)
    if (board[3] == board[5] == board[7] == -1)
        return true
    elseif (board[1] == board[2] == board[3] == -1)
        return true
    elseif (board[4] == board[5] == board[6] == -1)
        return true
    elseif (board[7] == board[8] == board[9] == -1)
        return true
    elseif (board[1] == board[4] == board[7] == -1)
        return true
    elseif (board[2] == board[5] == board[8] == -1)
        return true
    elseif (board[3] == board[6] == board[9] == -1)
        return true
    elseif (board[1] == board[5] == board[9] == -1)
        return true
    end
    return false
end

function is_empty(board)
    for i in board
        if (i != 0)
            return false
        end
    end
    return true
end

boards = []

for i in 1:3^9
    temp_board = digits(i, base = 3, pad = 9)
    for j in 1:9
        if (temp_board[j] == 2)
            temp_board[j] = -1
        end
    end
    push!(boards, temp_board)
end

# trim boards with impossible numbers of Xs or Os
valid_boards = []
for board in boards
    if (abs(num_Os(board) - num_Xs(board)) <= 1)
        push!(valid_boards, board)
    end
end

# trim boards where both X and O won and the empty board
valid_boards2 = []
for board in valid_boards
    if ((is_X_win(board) && is_O_win(board)) || (is_empty(board)))

    else
        push!(valid_boards2, board)

    end
end

# trim boards where it is O's move
valid_boards3 = []
for board in valid_boards2
    if (num_Xs(board) <= num_Os(board))
        push!(valid_boards3, board)
    end
end

println(length(valid_boards3))

for i in 1:10
    display_board(valid_boards3[i])
    println(" ")
end


# https://en.wikipedia.org/wiki/Tic-tac-toe#Strategy