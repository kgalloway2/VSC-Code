# tic-tac-toe master

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

test = generate_blank_board()
display_board([1.0, -1.0, -1.0, -1.0, 1.0, -1.0, 1.0, -1.0, 1.0])
display_board([1.0, -1.0, -1.0, -1.0, 1.0, -1.0, 1.0, 1.0, 1.0])

