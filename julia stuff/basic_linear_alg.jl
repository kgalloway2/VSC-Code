
A = rand(1:4, 3, 3)
B = A
C = copy(A)
display([ B C])
println("")

# now update A and look again
A[1] = 17
display([ B C])
println("")

# so B is just referenceing A but C copied A and became a new thing


x = ones(3)

b = A*x
display(b)
println("")

# conjugate transpose
display(A')
println("")

Asym = A + A'
display(Asym)
println("")

# don't need * operator to multiply matrices
Apd = A'A
display(Apd)
println("")

# can also solve linear systems using division (when solvable)
display(A\b)
println("")

# when the system is overdetermined, it gives the least squares solution

Atall = A[ :, 1:2]
display(Atall)
println("")
display(Atall\b)
println("")

# when the system is rank deficient we can also find a lest suwraes with smallest norm

A = randn(3, 3)
display(A)
println("")

display([A[:,1] A[:,1]]\b)
println("")

# when the system is underdetermined, we get the minimum norm solution

Ashort = A[1:2, :]
display(Ashort)
println("")

display(Ashort\b[1:2])
println("")