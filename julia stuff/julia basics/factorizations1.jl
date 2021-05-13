using LinearAlgebra

A = randn(3, 3)

# this is with pivoting, so we need the p
l, u, p = LinearAlgebra.lu(A)

display(l)
println("")
display(u)
println("")
display(p)
println("")

display(A)
println("")
display(l * u)
println("")
display(A[p,:])
println("")

# this is without pivoting

l, u, p = LinearAlgebra.lu(A, Val(false))

display(l)
println("")
display(u)
println("")
display(p)
println("")

display(A)
println("")
display(l * u)
println("")
display(A[p,:])
println("")

# we can also use lufact
# B = randn(3, 3)

# Blu =LinearAlgebra.lufact(B)

# display(Blu)
# println("")

# lufact was not a function in LinearAlgebra

# we can use lu decomp to solve matrix equations

x = ones(Float64,3)
b = A*x

display(b)
println("")

display(u^-1 * l^-1 * b)
println("")

display(det(A))
println("")

display(det(l*u))
println("")