import csv

number = 10000000

with open('palindromes_file.csv', mode='w') as palindromes_file:
    palindromes_writer = csv.writer(palindromes_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for i in range(2, number + 1):
        n = 1
        results = []
        while n < 10 ** 25:
            if str(n) == str(n)[::-1]:
                results.append(n)
            n = n * i
        if len(results) > 1 and not (len(results) == 2 and results[1] == i): 
            # first criteria eliminates trivial answers of i^0 = 1 peing a palindrome
            # second criteria filters out answers of i^1 = i is a palindrome
            palindromes_writer.writerow([i, results])