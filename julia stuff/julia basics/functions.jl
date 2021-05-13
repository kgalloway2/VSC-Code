
#=
function sayhi(name)
    println("Hi $name, it's great to see you!")
end

sayhi("Keaton")

function f(x)
    x^2
end

println(f(3))


# single line declaration
sayhi2(name) = println("Hello $name, it's still great to see you!")

sayhi2("Keaton")

# lambda or anonymous functions

sayhi3 = name -> println("Hey $name, it's always great to see you")

sayhi3("Keaton")

sayhi(1243425)

A = rand(3, 3)
display(A)
display(f(A))
=#

# mutating functions return an altered version of their inputs. follow their name with a !
# non-mutating functions do not alter their inputs

v = [3, 5, 2]
display(sort(v))
display(v)

w = [4, 7, 1]
sort!(w)
display(w)

# broadcasting
function f(x)
    x^2
end

A = [i + 3*j for j in 0:2, i in 1:3]

display(A)

display(f(A))

display(f.(A))

display(f.(v))