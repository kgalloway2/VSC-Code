x, y = 3, 10

if x < y
    println("$x is smaller than $y")
elseif x > y
    println("$x is larger than $y")
else
    println("$x is equal to $y")
end

if x > y
    x
else
    y
end

# a ? b : c means if a then b, else c
println(x > y ? x : y)

(x > y) && println("$x is larger than $y")
(x < y) && println("$x is smaller than $y")