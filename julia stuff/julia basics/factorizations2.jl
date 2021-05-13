using LinearAlgebra

A = randn(3, 3)

Aqr1 = LinearAlgebra.qrfactPivotedUnblocked!(A)
Aqr2 = LinearAlgebra.qrfactUnblocked!(A)

display(Aqr1)
println("")
display(Aqr2)
println("")
display(Aqr2.Q)
println("")

x = ones(3)
b = A*x

display(Aqr1\b)
println("")
display(Aqr2\b)
println("")