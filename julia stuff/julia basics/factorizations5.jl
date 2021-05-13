using LinearAlgebra

A = randn(3, 3)
display(A)
println("")

# three ways to return the diagonal of A as a Diagonal type object
display(Diagonal(LinearAlgebra.Diagonal(A)))
println("")

display(LinearAlgebra.Diagonal(A))
println("")

display(Diagonal(A))
println("")

# similarly, we can do lower triangular and upper triangular

display(LinearAlgebra.LowerTriangular(A))
println("")

display(LinearAlgebra.UpperTriangular(A))
println("")

# if we pass a symmetric to Symmetric, then we can declare it as symmetric to make some operatons better
Asym = A + A'

display(LinearAlgebra.Symmetric(Asym))
println("")

# and whatever tridiagonal is
# display(LinearAlgebra.SymTridiagonal(LinearAlgebra.Diagonal(Asym), LinearAlgebra.Diagonal(Asym, 1)))
# println("")
# didn't work