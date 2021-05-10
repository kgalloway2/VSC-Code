mydictionary = Dict('A' => 1, 'B' => 2, 'C' => 3)
println(mydictionary)

mydictionary['D'] = 4
println(mydictionary)

println(mydictionary['A'])

pop!(mydictionary, 'D') # deletes and returns the value associated with the key
println(mydictionary)


someanimals = ("dog", "cat", "mouse")
println(someanimals[1])

#someanimals[1] = "otter" 
#tuples are immutable. this won't work

somepeople = ["Ted", "Robyn", "Barney", "Lily", "Marshall"]
println(somepeople)

fib = [1, 1, 2, 3, 5, 8, 13]
println(typeof(fib))
println(fib)

mixedarray = [1, "one", 2, "two"]
println(mixedarray)

println(somepeople[3])
println(fib[5])
somepeople[3] = "Swarley"
println(somepeople[3])

# add items to an array with the push function
# take them away with the pop function
push!(fib, 21)
pop!(mixedarray)

println(fib)
println(mixedarray)

# we can also make arrays of arrays
notamatrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
println(notamatrix)

# creates a 2 row array with 3 entries in each row
a = rand(2, 3)
println(a)

# creates a 3d array (num dims, order of first array, order of second array, etc)
b = rand(4, 3, 2)
println(b)