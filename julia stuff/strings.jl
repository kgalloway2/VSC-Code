string1 = "This is a string!"
string2 = """This is also a string!"""
string3 = "This is a \"string\" with quotes."
string4 = """This is also a "string" with quotes."""

println(string1)
println(string2)
println(string3)
println(string4)

x = 4
y = 5

println("We can insert vriables with \$.")
println("$x + $y = $(x + y)")

println("we can also concatenate strings.")
println("first part ", "second part ", "third part")

s1 = "first part "
s2 = "second part"
println(s1*s2)
println("$s1$s2")