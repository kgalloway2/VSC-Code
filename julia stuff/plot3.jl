using Plots

x = -10:10

gr()

p1 = plot(x,x)
p2 = plot(x, x.^2)
p3 = plot(x, x.^3)
p4 = plot(x, x.^4)

display(plot(p1, p2, p3, p4, layout=(2,2), legend=false))

readline()