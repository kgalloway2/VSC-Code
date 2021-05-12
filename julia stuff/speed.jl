using BenchmarkTools

# this one needed c installed so skipping the c part

a = rand(10^7)

j_benchmark = @benchmark sum($a)

display(j_benchmark)

println(" fastest was $(minimum(j_benchmark.times) / 1e6) msec")

time_dict = Dict()
time_dict["Julia"] = (minimum(j_benchmark.times) / 1e6)

using Plots
using Statistics
gr()

t = j_benchmark.times / 1e6
m, sig = minimum(t), Statistics.std(t)

# display(histogram(t, bins=500,
#     xlim=(m - 0.01, m + sig),
#     xlabel="milliseconds", ylabel="count"))

# readline()


using PyCall

apy_list = PyCall.array2py(a)

pysum = pybuiltin("sum")

display(pysum(a))
# wow that was slow

py_bench = @benchmark $pysum($apy_list)

display(py_bench)

tp = j_benchmark.times / 1e6
mp, sigp = minimum(tp), Statistics.std(tp)

display(histogram(tp, bins=500,
    xlim=(mp - 0.01, mp + sigp),
    xlabel="milliseconds", ylabel="count"))

readline()

# going to skip the numpy one and the handwritten python
# too becuase it takes so long to do this
# since I'm working in a file and not directly in a julia terminal
