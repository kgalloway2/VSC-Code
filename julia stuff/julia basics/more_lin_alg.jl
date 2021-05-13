using LinearAlgebra

# rational systems
A = rand(1:10,3,3)
B = rand(1:10,3,3)

display(A * B)
println("")

# make it a matrix of rationals and all subsequent operations will also give rational numbers
Ar = LinearAlgebra.convert(Matrix{Rational{BigInt}}, A)/10

display(Ar)
println("")

x = ones(Int, 3)
b = Ar * x

display(b)
println("")
display(Ar\b)
println("")

# rational LU

display(LinearAlgebra.lu(Ar))
println("")

# we can also do eigenstuff with rational matrices

l1, l2, l3 = 1//1, 1//2, 1//4 # use double slash to denote that these are rationals
v1, v2, v3 = [1, 0, 0], [1, 1, 0], [1, 1, 1]
V, G = [v1 v2 v3], Diagonal([l1, l2, l3])
A = V * G / V # that's * V-1 on the right

display(V)
println("")
display(G)
println("")
display(A)
println("")
