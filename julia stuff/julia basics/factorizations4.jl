using LinearAlgebra

A = randn(3,3)

Asvd = LinearAlgebra.svd(A)

display(Asvd)
println("")
display(Asvd.U)
println("")
display(Asvd.Vt)
println("")

# can use this to solve matrix equations too
x = ones(3)
b = A*x

display(Asvd\b)
println("")