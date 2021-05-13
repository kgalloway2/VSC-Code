using LinearAlgebra

n = 1000
A = randn(n, n)
Asym1 = A + A'
Asym2 = copy(Asym1)
Asym2[1,2] += 5eps()

println("Is Asym1 symmetric? ", issymmetric(Asym1))
println("Is Asym2 symmetric? ", issymmetric(Asym2))

@time eigvals(Asym1)
@time eigvals(Asym2)
@time eigvals(Symmetric(Asym2))
