days = 365

days_float = convert(Float64, days)

@assert days_float == 365.0

println(days_float)