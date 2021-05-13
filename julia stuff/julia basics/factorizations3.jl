using LinearAlgebra

A = randn(3, 3)

Asym = A + A'

AsymEig = LinearAlgebra.eigen(Asym)

display(AsymEig)
println("")

# julia knows that AsymEig has multiple pieces but it knows what to do
display(inv(AsymEig)*Asym)
println("")

# another way to find eigenvalues which returns them in a different format
# this version is not recommended
display(LinearAlgebra.eigen(Asym))
println("")

