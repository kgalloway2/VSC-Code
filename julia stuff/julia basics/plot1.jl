using Plots

x = -3:0.1:3
f(x) = x^2

y = f.(x)

gr()
display(plot(x, y, label="line"))
display(scatter!(x, y, label="points"))

readline()