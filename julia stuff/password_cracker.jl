#=
This is a simple password cracker that guesses a random password of the same length and changes it until it matches.
It works similar to how you would guess full passwords from a list of passwords. If the guess is wrong, remove it from the list and try another.
Only it does that for each character of the guess and password.
=#


characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 
'A', 'B', 'C', 'D', 'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
'0','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','-','=','`','~', '[',']','{','}','|',';',':']

function generator(length)
    password = ""
    for i in 1:length
        password *= string(Base.rand(characters))
    end
    password
end

function cracker(password)
    n = length(password)
    guess = generator(n)
    count = 0
    available_guesses = Any[]
    for i in 1:n
        push!(available_guesses, [])
        for j in 1:length(characters)
            push!(available_guesses[i], characters[j])
        end
    end
    while guess != password
        newguess = ""
        samecount = 0
        print("attempt #", count, ": ", guess)
        for i in 1:n
            current_char = guess[i]
            if current_char != password[i]
                deleteat!(available_guesses[i], findall(x -> x == current_char, available_guesses[i]))
                newguess *= string(Base.rand(available_guesses[i]))
            else
                newguess *= current_char
                samecount += 1
            end
        end
        guess = newguess
        count += 1
        percent_same = samecount / n
        println(" They are ", 100 * percent_same, "% similar")
    end
    guess
end

password = generator(80)
println("the password is $password")
guess = cracker(password)
println("final guess is $guess", "\n", guess == password)