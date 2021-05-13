using DelimitedFiles

training = []

training_input = []
training_target = []

open("data.txt") do file
    for ln in eachline(file)
        push!(training, ln)
    end
end

training_input = training[1]
training_target = training[2]

for i in 1:5
    println(training_input[i])
    println(training_target[i])
end