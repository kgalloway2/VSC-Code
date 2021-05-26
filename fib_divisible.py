fibs = [1, 1]

# this function creates the list of fibonacci numbers up to the desired length
def fib(n):
    if n < len(fibs):
        return fibs[n]
    else:
        fibs.append(fib(n - 1) + fib(n - 2))
        return fibs[n]

# run the function to generate a list of the first 500 fibonacci numbers
fib(500)


results = []

# this function checks whether a fibonacci number is divisible by its index
# for example: 2 is the 2nd fibonacci number (indexing from 0) and is 
# divisible by 2, so it is added to the results
def finder():
    for i in range(2,500):
        if fibs[i] % i == 0:
            results.append(fibs[i])
        else:
            pass

finder()
print(results)