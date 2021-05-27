using JLD
using Flux, Flux.Data.MNIST
using Flux: onehotbatch, argmax, crossentropy, throttle
using Base.Iterators: repeated
using LinearAlgebra
using DelimitedFiles
using CSV
using DataFrames

neural_net = load("C:/Users/kgtrm/Documents/VSC Code/julia stuff/tictactoe/tictactoeneuralnet.jld")["data"]

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

function X_move(board)
    position = argmax(neural_net(board))
    board[position] = 1
end

function O_move(board)
    available_moves = []
    for place in 1:length(board)
        if board[place] == 0
            push!(available_moves, place)
        end
    end
    position = rand(available_moves)
    board[position] = -1
end

function play_game()
    board = generate_blank_board()
    xturn = true
    while !is_O_win(board) and !is_X_win(board)
        display_board(board)
        if xturn
            X_move!(board)
            xturn = false
        else
            O_move!(board)
            xturn = true
        end
    end
    if is_O_win(board)
        return 0
    elseif is_X_win(board)
        return 1
    else
        return 0
    end
end

num_games = 1
num_wins = 0
count = 1

while count <= num_games
    num_wins += play_game()
    count += 1

println(num_wins / num_games * 100)