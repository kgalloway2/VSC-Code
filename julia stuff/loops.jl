#=
i = 1
while i < 10
    println(i)
    global i +=1
end

myfriends = ["Ted", "Robyn", "Barney", "Lily", "Marshall"]

i = 1
while i <= length(myfriends)
    friend = myfriends[i]
    println("Hi $friend, it's great to see you!")
    global i += 1
end

for i in 1:10
    println(i)
end

for i = 1:10
    println(i)
end

for friend in myfriends
    println("Hi $friend, it's great to see you!")
end
=#

m, n = 5, 5
A = zeros(m, n) #this makes a 5x5 matrix with all 0s

for i in 1:m
    for j in 1:n
        A[i, j] = i + j
    end
end

for i in 1:m
    for j in 1:n
        print(A[i, j], "  ")
    end
    println(" ")
end

B = zeros(m , n)

for i in 1:m, j in 1:n
    B[i, j] = i * j
end

for i in 1:m
    for j in 1:n
        print(B[i, j], "  ")
    end
    println(" ")
end

C = [i + j for i in 1:m, j in 1:n]
for i in 1:m
    for j in 1:n
        print(C[i, j], "  ")
    end
    println(" ")
end

for n in 1:10
    D = [i + j for i in 1:n, j in 1:n]
    display(D)
end