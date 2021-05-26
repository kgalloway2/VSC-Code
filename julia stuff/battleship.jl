function generate_blank_board(size)
    empty_sea = []
    for i in 1:size
        push!(empty_sea, [])
        for j in 1:size
            push!(empty_sea[i], "|_")
        end
    end
    return empty_sea
end

function display_sea(sea)
    print("y:")
    for i in 1:length(sea)
        print("  ", i)
    end
    print("|x", "\n")
    for i in 1:length(sea)
        print("  ")
        for j in 1:length(sea)
            print(" ", sea[i][j])
        end
        print(" ", i, "\n")
    end
end

function available_positions(bow, length, size)
    positions = []
    length -= 1
    if (bow[1] + length <= size)
        push!(positions, [bow[1] + length, bow[2]])
    end
    if (bow[1] - length > 0)
        push!(positions, [bow[1] - length, bow[2]])
    end
    if (bow[2] + length <= size)
        push!(positions, [bow[1], bow[2] + length])
    end
    if (bow[2] - length > 0)
        push!(positions, [bow[1], bow[2] - length])
    end
    return positions
end

function place_ships(size, board)
    if (size == 5)
        ship1 = []
        println("You have one 3x1 ship. Where would you like to place the bow (front)?") 
        println("Enter x-coordinate:")
        bow1x = readline()
        bow1x = parse(Int64, bow1x)
        println("Enter y-coordinate:")
        bow1y = readline()
        bow1y = parse(Int64, bow1y)
        stern_positions = available_positions([bow1x, bow1y], 3, size)
        for k in 1:length(stern_positions)
            println(k, ". ", stern_positions[k])
        end
        println("Where would you like to place the stern?")
        println("Enter a number:")
        stern = readline()
        stern = parse(Int64, stern)
        stern1x = stern_positions[stern][1]
        stern1y = stern_positions[stern][2]
        if (bow1y == stern1y)
            if (bow1x < stern1x)
                for i in bow1x:stern1x
                    push!(ship1, [i, stern1y])
                end
            else
                for i in stern1x:bow1x
                    push!(ship1, [i, stern1y])
                end
            end
        else
            if (bow1y < stern1y)
                for i in bow1y:stern1y
                    push!(ship1, [bow1x, i])
                end
            else
                for i in stern1y:bow1y
                    push!(ship1, [bow1x, i])
                end
            end
        end
        for j in ship1
            board[j[1]][j[2]] = "|S"
        end
    elseif (size == 7)
        ship1 = []
        println("You have one 3x1 ship and one 4x1 ship. Where would you like to place the bow (front) of the 3x1 ship?") 
        println("Enter x-coordinate:")
        bow1x = readline()
        bow1x = parse(Int64, bow1x)
        println("Enter y-coordinate:")
        bow1y = readline()
        bow1y = parse(Int64, bow1y)
        stern_positions = available_positions([bow1x, bow1y], 3, size)
        for k in 1:length(stern_positions)
            println(k, ". ", stern_positions[k])
        end
        println("Where would you like to place the stern?")
        println("Enter a number:")
        stern = readline()
        stern = parse(Int64, stern)
        stern1x = stern_positions[stern][1]
        stern1y = stern_positions[stern][2]
        if (bow1y == stern1y)
            if (bow1x < stern1x)
                for i in bow1x:stern1x
                    push!(ship1, [i, stern1y])
                end
            else
                for i in stern1x:bow1x
                    push!(ship1, [i, stern1y])
                end
            end
        else
            if (bow1y < stern1y)
                for i in bow1y:stern1y
                    push!(ship1, [bow1x, i])
                end
            else
                for i in stern1y:bow1y
                    push!(ship1, [bow1x, i])
                end
            end
        end
        for j in ship1
            board[j[1]][j[2]] = "|S"
        end
        ship2 = []
        println("You have a 4x1 ship. Where would you like to place the bow (front)?") 
        println("Enter x-coordinate:")
        bow1x = readline()
        bow1x = parse(Int64, bow1x)
        println("Enter y-coordinate:")
        bow1y = readline()
        bow1y = parse(Int64, bow1y)
        stern_positions = available_positions([bow1x, bow1y], 4, size)
        for k in 1:length(stern_positions)
            println(k, ". ", stern_positions[k])
        end
        println("Where would you like to place the stern?")
        println("Enter a number:")
        stern = readline()
        stern = parse(Int64, stern)
        stern1x = stern_positions[stern][1]
        stern1y = stern_positions[stern][2]
        if (bow1y == stern1y)
            if (bow1x < stern1x)
                for i in bow1x:stern1x
                    push!(ship2, [i, stern1y])
                end
            else
                for i in stern1x:bow1x
                    push!(ship2, [i, stern1y])
                end
            end
        else
            if (bow1y < stern1y)
                for i in bow1y:stern1y
                    push!(ship2, [bow1x, i])
                end
            else
                for i in stern1y:bow1y
                    push!(ship2, [bow1x, i])
                end
            end
        end
        for j in ship2
            board[j[1]][j[2]] = "|S"
        end
    elseif (size == 10)
        ship1 = []
        println("You have one 3x1 ship, one 4x1 ship, and one 5x1 ship. Where would you like to place the bow (front) of the 3x1 ship?") 
        println("Enter x-coordinate:")
        bow1x = readline()
        bow1x = parse(Int64, bow1x)
        println("Enter y-coordinate:")
        bow1y = readline()
        bow1y = parse(Int64, bow1y)
        stern_positions = available_positions([bow1x, bow1y], 3, size)
        for k in 1:length(stern_positions)
            println(k, ". ", stern_positions[k])
        end
        println("Where would you like to place the stern?")
        println("Enter a number:")
        stern = readline()
        stern = parse(Int64, stern)
        stern1x = stern_positions[stern][1]
        stern1y = stern_positions[stern][2]
        if (bow1y == stern1y)
            if (bow1x < stern1x)
                for i in bow1x:stern1x
                    push!(ship1, [i, stern1y])
                end
            else
                for i in stern1x:bow1x
                    push!(ship1, [i, stern1y])
                end
            end
        else
            if (bow1y < stern1y)
                for i in bow1y:stern1y
                    push!(ship1, [bow1x, i])
                end
            else
                for i in stern1y:bow1y
                    push!(ship1, [bow1x, i])
                end
            end
        end
        for j in ship1
            board[j[1]][j[2]] = "|S"
        end
        ship2 = []
        println("You have a 4x1 ship. Where would you like to place the bow (front)?") 
        println("Enter x-coordinate:")
        bow1x = readline()
        bow1x = parse(Int64, bow1x)
        println("Enter y-coordinate:")
        bow1y = readline()
        bow1y = parse(Int64, bow1y)
        stern_positions = available_positions([bow1x, bow1y], 4, size)
        for k in 1:length(stern_positions)
            println(k, ". ", stern_positions[k])
        end
        println("Where would you like to place the stern?")
        println("Enter a number:")
        stern = readline()
        stern = parse(Int64, stern)
        stern1x = stern_positions[stern][1]
        stern1y = stern_positions[stern][2]
        if (bow1y == stern1y)
            if (bow1x < stern1x)
                for i in bow1x:stern1x
                    push!(ship2, [i, stern1y])
                end
            else
                for i in stern1x:bow1x
                    push!(ship2, [i, stern1y])
                end
            end
        else
            if (bow1y < stern1y)
                for i in bow1y:stern1y
                    push!(ship2, [bow1x, i])
                end
            else
                for i in stern1y:bow1y
                    push!(ship2, [bow1x, i])
                end
            end
        end
        for j in ship2
            board[j[1]][j[2]] = "|S"
        end
        ship3 = []
        println("You have a 5x1 ship. Where would you like to place the bow (front)?") 
        println("Enter x-coordinate:")
        bow1x = readline()
        bow1x = parse(Int64, bow1x)
        println("Enter y-coordinate:")
        bow1y = readline()
        bow1y = parse(Int64, bow1y)
        stern_positions = available_positions([bow1x, bow1y], 5, size)
        for k in 1:length(stern_positions)
            println(k, ". ", stern_positions[k])
        end
        println("Where would you like to place the stern?")
        println("Enter a number:")
        stern = readline()
        stern = parse(Int64, stern)
        stern1x = stern_positions[stern][1]
        stern1y = stern_positions[stern][2]
        if (bow1y == stern1y)
            if (bow1x < stern1x)
                for i in bow1x:stern1x
                    push!(ship3, [i, stern1y])
                end
            else
                for i in stern1x:bow1x
                    push!(ship3, [i, stern1y])
                end
            end
        else
            if (bow1y < stern1y)
                for i in bow1y:stern1y
                    push!(ship3, [bow1x, i])
                end
            else
                for i in stern1y:bow1y
                    push!(ship3, [bow1x, i])
                end
            end
        end
        for j in ship3
            board[j[1]][j[2]] = "|S"
        end
    end
end
        
function place_opponent_ships(size, board)
    if (size == 5)
        bowx = rand(1:size)
        bowy = rand(1:size)
        stern_positions = available_positions([bowx, bowy], 3, size)
        stern = rand(1:length(stern_positions))
        sternx = stern_positions[stern][1]
        sterny = stern_positions[stern][2]
        ship1 = []
        if (bowy == sterny)
            if (bowx < sternx)
                for i in bowx:sternx
                    push!(ship1, [i, sterny])
                end
            else
                for i in sternx:bowx
                    push!(ship1, [i, sterny])
                end
            end
        else
            if (bowy < sterny)
                for i in bowy:sterny
                    push!(ship1, [bowx, i])
                end
            else
                for i in sterny:bowy
                    push!(ship1, [bowx, i])
                end
            end
        end
        for j in ship1
            board[j[1]][j[2]] = "|S"
        end
    elseif (size == 7)
        for n in 3:4
            bowx = rand(1:size)
            bowy = rand(1:size)
            stern_positions = available_positions([bowx, bowy], n, size)
            stern = rand(1:length(stern_positions))
            sternx = stern_positions[stern][1]
            sterny = stern_positions[stern][2]
            ship1 = []
            if (bowy == sterny)
                if (bowx < sternx)
                    for i in bowx:sternx
                        push!(ship1, [i, sterny])
                    end
                else
                    for i in sternx:bowx
                        push!(ship1, [i, sterny])
                    end
                end
            else
                if (bowy < sterny)
                    for i in bowy:sterny
                        push!(ship1, [bowx, i])
                    end
                else
                    for i in sterny:bowy
                        push!(ship1, [bowx, i])
                    end
                end
            end
            for j in ship1
                board[j[1]][j[2]] = "|S"
            end
        end
    elseif (size == 10)
        for n in 3:5
            bowx = rand(1:size)
            bowy = rand(1:size)
            stern_positions = available_positions([bowx, bowy], n, size)
            stern = rand(1:length(stern_positions))
            sternx = stern_positions[stern][1]
            sterny = stern_positions[stern][2]
            ship1 = []
            if (bowy == sterny)
                if (bowx < sternx)
                    for i in bowx:sternx
                        push!(ship1, [i, sterny])
                    end
                else
                    for i in sternx:bowx
                        push!(ship1, [i, sterny])
                    end
                end
            else
                if (bowy < sterny)
                    for i in bowy:sterny
                        push!(ship1, [bowx, i])
                    end
                else
                    for i in sterny:bowy
                        push!(ship1, [bowx, i])
                    end
                end
            end
            for j in ship1
                board[j[1]][j[2]] = "|S"
            end
        end
    end
end

function player_turn(actual_sea, view_sea)
    println("It is your turn. Here is the current board:")
    display_sea(view_sea)
    println("Choose your next shot.")
    println("Enter x-coordinate: ")
    shotx = parse(Int64, readline())
    println("Enter y-coordinate: ")
    shoty = parse(Int64, readline())
    if (actual_sea[shotx][shoty] == "|S")
        println("HIT!")
        actual_sea[shotx][shoty] = "|H"
        view_sea[shotx][shoty] = "|H"
    elseif (actual_sea[shotx][shoty] == "|_")
        println("MISS!")
        actual_sea[shotx][shoty] = "|X"
        view_sea[shotx][shoty] = "|X"
    end
    println("Here is the current board:")
    display_sea(view_sea)
end

function opponent_turn(sea, guesses)
    println("It is the opponent's turn.")
    shot = rand(guesses)
    shotx = shot[1]
    shoty = shot[2]
    if (sea[shotx][shoty] == "|S")
        println("HIT!")
        sea[shotx][shoty] = "|H"
        deleteat!(guesses, findall(x -> x == shot, guesses))
    elseif (sea[shotx][shoty] == "|_")
        println("MISS!")
        sea[shotx][shoty] = "|X"
        deleteat!(guesses, findall(x -> x == shot, guesses))
    end
    println("Here is the current board:")
    display_sea(sea)
end

while (true)
    println("Welcome to Battleship!")
    println("How large of a board do you want to play on? (5, 7, 10)")
    size = readline()
    size = parse(Int64, size)
    player_sea = generate_blank_board(size)
    opponent_sea = generate_blank_board(size)
    opp_sea_player_view = generate_blank_board(size)
    place_ships(size, player_sea)
    display_sea(player_sea)
    place_opponent_ships(size, opponent_sea)
    gameover = false
    guesses = []
    for i in 1:size, j in 1:size
        push!(guesses, [i,j])
    end
    while (!gameover)
        gameover = true
        player_turn(opponent_sea, opp_sea_player_view)
        for a in opponent_sea
            for b in a
                if (b == "|S")
                    gameover = false
                end
            end
        end
        if (gameover == true)
            println("You win!")
            break
        end
        println("Press \'Enter\' to continue to opponent's turn.")
        readline()
        opponent_turn(player_sea, guesses)
        for a in opponent_sea
            for b in a
                if (b == "|S")
                    gameover = false
                end
            end
        end
        if (gameover == true)
            println("You lose!")
            break
        end
        println("Press \'Enter\' to continue to your turn.")
        readline()
    end
end