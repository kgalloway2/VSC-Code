using DelimitedFiles

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

function not_in_classes(board, classes)
    for class in classes
        for r in class
            if (r == board)
                return false
            end
        end
    end
    return true
end

function rotate90(board)
    newboard = zeros(9)
    for i in 1:length(board)
        if (i == 1)
            newboard[7] = board[i]
        elseif (i == 2)
            newboard[4] = board[i]
        elseif (i == 3)
            newboard[1] = board[i]
        elseif (i == 4)
            newboard[8] = board[i]
        elseif (i == 5)
            newboard[5] = board[i]
        elseif (i == 6)
            newboard[2] = board[i]
        elseif (i == 7)
            newboard[9] = board[i]
        elseif (i == 8)
            newboard[6] = board[i]
        elseif (i == 9)
            newboard[3] = board[i]
        end
    end
    return newboard
end

function rotate180(board)
    temp = rotate90(board)
    return rotate90(temp)
end

function rotate270(board)
    temp = rotate180(board)
    return rotate90(temp)
end

function rotationally_similar(board1, board2)
    if (board1 == rotate90(board2))
        return true
    elseif (board1 == rotate180(board2))
        return true
    elseif (board1 == rotate270(board2))
        return true
    else
        return false
    end
end

function class_index(board, classes)
    for i in 1:length(classes)
        for k in classes[i]
            if (board == k)
                return i
            end
        end 
    end
    return false
end

function num_Xs_row(row)
    count = 0
    for i in row
        if (i == 1)
            count += 1
        end
    end
    return count
end

function num_Os_row(row)
    count = 0
    for i in row
        if (i == -1)
            count += 1
        end
    end
    return count
end

function num_Es_row(row)
    count = 0
    for i in row
        if (i == 0)
            count += 1
        end
    end
    return count
end

function X_can_win(board)
    rows = [[board[1] board[2] board[3]],
    [board[4] board[5] board[6]],
    [board[7] board[8] board[9]],
    [board[1] board[4] board[7]],
    [board[2] board[5] board[8]],
    [board[3] board[6] board[9]],
    [board[1] board[5] board[9]],
    [board[3] board[5] board[7]]]

    for row in rows
        if (num_Xs_row(row) == 2 && num_Es_row(row) == 1)
            return true
        end
    end
    return false
end

function O_can_win(board)
    rows = [[board[1] board[2] board[3]],
    [board[4] board[5] board[6]],
    [board[7] board[8] board[9]],
    [board[1] board[4] board[7]],
    [board[2] board[5] board[8]],
    [board[3] board[6] board[9]],
    [board[1] board[5] board[9]],
    [board[3] board[5] board[7]]]

    for row in rows
        if (num_Os_row(row) == 2 && num_Es_row(row) == 1)
            return true
        end
    end
    return false
end

function solve_one_move(board)
    solution = zeros(9)
    
    for i in 1:length(board)
        temp_board = copy(board)
        if (temp_board[i] == 0)
            temp_board[i] = 1
        end
        if (is_X_win(temp_board))
            solution[i] = 1
            return solution
        end
    end
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
println(length(boards))

# trim boards with impossible numbers of Xs or Os
valid_boards = []
for board in boards
    if (abs(num_Os(board) - num_Xs(board)) <= 1)
        push!(valid_boards, board)
    end
end
println(length(valid_boards))

# trim boards where both X and O won and the empty board and finished games
valid_boards2 = []
for board in valid_boards
    if ((is_X_win(board) && is_O_win(board)) || (is_empty(board)) || is_X_win(board) || is_O_win(board))

    else
        push!(valid_boards2, board)

    end
end
println(length(valid_boards2))

# trim boards where it is O's move
valid_boards3 = []
for board in valid_boards2
    if (num_Xs(board) <= num_Os(board))
        push!(valid_boards3, board)
    end
end
println(length(valid_boards3))

# trim full boards with no moves left
valid_boards4 = []
for board in valid_boards3
    if (num_Xs(board) + num_Os(board) < 9)
        push!(valid_boards4, board)
    end
end
println(length(valid_boards4))

# now we split these boards up by rotational symmetry
symmetry_classes = []
for board in valid_boards4
    in_class = false
    if (not_in_classes(board, symmetry_classes))
        for class in symmetry_classes
            if (rotationally_similar(board, class[1]))
                push!(class, board)
                in_class = true
                break
            end
        end
        if (!in_class)
            push!(symmetry_classes, [board])
        end
    end
end

println(length(symmetry_classes))

solved_boards = []
solutions = []
for class in symmetry_classes
    if (X_can_win(class[1]))
        for board in class
            push!(solved_boards, board)
            push!(solutions, solve_one_move(board))
        end
    end
end

# for i in 1:5
#     println("board")
#     display_board(solved_boards[i])
#     println("solution")
#     display_board(solutions[i])
#     println("-------------")
# end

# writedlm("data.txt", "[")
writedlm("data.txt", [solved_boards, solutions], ",")
# writedlm("data.txt", "]")
# writedlm("data.txt", "[")
# writedlm("data.txt", solutions, ",")
# writedlm("data.txt", "]")


# https://en.wikipedia.org/wiki/Tic-tac-toe#Strategy