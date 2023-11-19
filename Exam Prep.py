# Problem 1:
# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_of_multiples(limit):
    total = 0  # Initialize total sum to 0
    for i in range(limit):  # Iterate through numbers from 0 to limit-1
        if i % 3 == 0 or i % 5 == 0:  # Check if the number is divisible by 3 or 5
            total += i  # Add the number to the total sum if it is a multiple of 3 or 5
    return total  # Return the total sum

# Call the function with 1000 as the limit and print the result
result = sum_of_multiples(1000)
print(f"Problem 1 - The sum of multiples is: {result}")


# Problem 2:
# Find the sum of the even-valued terms in the Fibonacci sequence whose values do not exceed four million.

def sum_even_fibonacci(limit):
    a, b = 1, 2  # Initialize the first two terms of the Fibonacci sequence
    total = 0  # Initialize total sum to 0

    while a <= limit:  # Continue loop until the term exceeds the limit
        if a % 2 == 0:  # Check if the term is even
            total += a  # Add the term to the total sum if it is even
        a, b = b, a + b  # Update the terms to the next two in the sequence

    return total  # Return the total sum of even-valued terms

# Call the function with 4000000 as the limit and print the result
print(f"Problem 2 - The sum of even-valued Fibonacci terms is: {sum_even_fibonacci(4000000)}")


# Problem 3:
# Find the largest prime factor of the number 600851475143.

def largest_prime_factor(n):
    i = 2  # Initialize the divisor as the smallest prime number, which is 2
    while i * i <= n:  # While the square of the divisor is less than or equal to n
        if n % i:  # If n is not divisible by i
            i += 1  # Increment i to check the next number
        else:
            n //= i  # If n is divisible by i, divide n by i
    return n  # The remaining value of n is the largest prime factor

# Call the function with 600851475143 as the input and print the result
print(f"Problem 3 - The largest prime factor is: {largest_prime_factor(600851475143)}")


# Problem 4:
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    return str(n) == str(n)[::-1]  # Check if the number is a palindrome

def largest_3_digit_palindrome():
    largest_palindrome = 0  # Initialize the largest palindrome to 0
    for i in range(100, 1000):  # Iterate over all 3-digit numbers for the first factor
        for j in range(100, 1000):  # Iterate over all 3-digit numbers for the second factor
            product = i * j  # Calculate the product of the two 3-digit numbers
            if is_palindrome(product) and product > largest_palindrome:  # Check if the product is a palindrome and larger than the current largest
                largest_palindrome = product  # Update the largest palindrome
    return largest_palindrome  # Return the largest palindrome found

# Call the function and print the result
print(f"Problem 4 - The largest palindrome made from the product of two 3-digit numbers is: {largest_3_digit_palindrome()}")


# Problem 5:
# Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.

def gcd(a, b):
    while b:  # While b is not zero
        a, b = b, a % b  # Set a to b and b to the remainder of a divided by b
    return a  # Return the greatest common divisor

def lcm(a, b):
    return a * b // gcd(a, b)  # Return the least common multiple of a and b

def smallest_multiple(n):
    multiple = 1  # Start with 1 as the initial multiple
    for i in range(1, n + 1):  # Iterate over all numbers from 1 to n
        multiple = lcm(multiple, i)  # Update the multiple to the least common multiple of itself and i
    return multiple  # Return the smallest multiple that is evenly divisible by all numbers from 1 to n

# Call the function with 20 as the input and print the result
print(f"Problem 5 - The smallest number evenly divisible by all of the numbers from 1 to 20 is: {smallest_multiple(20)}")


# Problem 6:
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_squares(n):
    return sum(i**2 for i in range(1, n + 1))  # Calculate the sum of the squares of the first n natural numbers

def square_of_sum(n):
    return sum(range(1, n + 1)) ** 2  # Calculate the square of the sum of the first n natural numbers

def difference(n):
    return square_of_sum(n) - sum_of_squares(n)  # Calculate the difference between the square of the sum and the sum of the squares

# Call the function with 100 as the input and print the result
print(f"Problem 6 - The difference is: {difference(100)}")


# Problem 7:
# Find the 10,001st prime number.

def is_prime(n):
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    if n <= 3:  # 2 and 3 are prime numbers
        return True
    if n % 2 == 0 or n % 3 == 0:  # Eliminate multiples of 2 and 3
        return False
    i = 5
    while i * i <= n:  # Check only up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  # Increase i by 6, since we already checked multiples of 2 and 3
    return True

def find_nth_prime(n):
    count = 0  # Counter for the number of primes found
    prime = 1  # Start checking for primes from number 1

    while count < n:  # Continue until n primes are found
        prime += 1  # Check the next number
        if is_prime(prime):
            count += 1  # Increment the count if a prime is found

    return prime  # Return the nth prime number

# Call the function with 10001 as the input and print the result
print(f"Problem 7 - The 10001st prime number is: {find_nth_prime(10001)}")



# Problem 8:
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.

# The 1000-digit number
number = (
    "73167176531330624919225119674426574742355349194934"
    "96983520312774506326239578318016984801869478851843"
    "85861560789112949495459501737958331952853208805511"
    "12540698747158523863050715693290963295227443043557"
    "66896648950445244523161731856403098711121722383113"
    "62229893423380308135336276614282806444486645238749"
    "30358907296290491560440772390713810515859307960866"
    "70172427121883998797908792274921901699720888093776"
    "65727333001053367881220235421809751254540594752243"
    "52584907711670556013604839586446706324415722155397"
    "53697817977846174064955149290862569321978468622482"
    "83972241375657056057490261407972968652414535100474"
    "82166370484403199890008895243450658541227588666881"
    "16427171479924442928230863465674813919123162824586"
    "17866458359124566529476545682848912883142607690042"
    "24219022671055626321111109370544217506941658960408"
    "07198403850962455444362981230987879927244284909188"
    "84580156166097919133875499200524063689912560717606"
    "05886116467109405077541002256983155200055935729725"
    "71636269561882670428252483600823257530420752963450"
)

def greatest_product(num, length):
    max_product = 0  # Initialize the maximum product to 0
    for i in range(len(num) - length + 1):  # Iterate over the number, considering groups of 'length' digits
        product = 1  # Initialize product for the current group of digits
        for j in range(length):  # Iterate over each digit in the group
            product *= int(num[i + j])  # Multiply the digits together
        max_product = max(max_product, product)  # Update the maximum product if the current product is greater
    return max_product  # Return the greatest product found

# Call the function with the 1000-digit number and 13 as the length and print the result
print(f"Problem 8 - The greatest product of thirteen adjacent digits is: {greatest_product(number, 13)}")



# Problem 9:
# Find the product abc of the Pythagorean triplet for which a + b + c = 1000.

def find_pythagorean_triplet(sum_value):
    for a in range(1, sum_value):
        for b in range(a, sum_value - a):
            c = sum_value - a - b  # Calculate c based on the condition a + b + c = sum_value
            if a*a + b*b == c*c:  # Check if a, b, c form a Pythagorean triplet
                return a * b * c  # Return the product of a, b, and c

# Call the function with 1000 as the sum value and print the result
print(f"Problem 9 - The product of the Pythagorean triplet is: {find_pythagorean_triplet(1000)}")


# Problem 10:
# Find the sum of all the primes below two million.

def is_prime(n):
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    if n <= 3:  # 2 and 3 are prime numbers
        return True
    if n % 2 == 0 or n % 3 == 0:  # Eliminate multiples of 2 and 3
        return False
    i = 5
    while i * i <= n:  # Check only up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  # Increase i by 6, since we already checked multiples of 2 and 3
    return True

def sum_of_primes_below(limit):
    total = 0  # Initialize the sum of primes to 0
    for i in range(2, limit):  # Iterate over all numbers from 2 to limit-1
        if is_prime(i):
            total += i  # Add the number to the total sum if it is prime
    return total  # Return the sum of primes

# Call the function with 2000000 as the limit and print the result
print(f"Problem 10 - The sum of all primes below two million is: {sum_of_primes_below(2000000)}")


# Problem 12:
# Find the value of the first triangle number to have over five hundred divisors.

def count_divisors(n):
    divisors = 0  # Initialize the count of divisors
    for i in range(1, int(n**0.5) + 1):  # Only need to check up to the square root of n
        if n % i == 0:
            divisors += 2 if i != n // i else 1  # If the divisor is not a square, add 2, otherwise add 1
    return divisors

def find_triangle_number(divisor_limit):
    n = 1  # Initialize the term in the sequence
    triangle_number = 1  # Initialize the first triangle number

    while count_divisors(triangle_number) <= divisor_limit:
        n += 1  # Increment the term
        triangle_number += n  # Add the next term to get the next triangle number

    return triangle_number  # Return the first triangle number with over 'divisor_limit' divisors

# Call the function with 500 as the divisor limit and print the result
print(f"Problem 12 - The first triangle number to have over five hundred divisors is: {find_triangle_number(500)}")


# Problem 14:
# Find the starting number, under one million, that produces the longest Collatz sequence chain.

def collatz_sequence_length(n):
    length = 1  # Start with a length of 1 for the initial number
    while n != 1:
        if n % 2 == 0:
            n = n // 2  # If n is even, divide it by 2
        else:
            n = 3 * n + 1  # If n is odd, multiply by 3 and add 1
        length += 1  # Increment the length of the sequence
    return length

def longest_collatz_sequence(limit):
    max_length = 0  # Initialize the maximum length
    number = 0  # Initialize the number with the longest sequence

    for i in range(1, limit):
        length = collatz_sequence_length(i)  # Get the length of the Collatz sequence for i
        if length > max_length:
            max_length = length  # Update the maximum length
            number = i  # Update the number with the longest sequence

    return number  # Return the number with the longest Collatz sequence

# Call the function with 1000000 as the limit and print the result
print(f"Problem 14 - The starting number under one million that produces the longest chain is: {longest_collatz_sequence(1000000)}")


# Problem 15:
# Calculate the number of routes through a 20x20 grid, moving only to the right and down.

import math

def calculate_routes(grid_size):
    # The number of movements is equal to grid_size * 2 (right and down movements)
    total_movements = grid_size * 2

    # The number of routes is the binomial coefficient of total_movements choose grid_size
    # This is because we choose grid_size movements from total_movements (either right or down)
    routes = math.comb(total_movements, grid_size)

    return routes

# Calculate the number of routes for a 20x20 grid and print the result
print(f"Problem 15 - The number of routes through a 20x20 grid is: {calculate_routes(20)}")


# Problem 16:
# Calculate the sum of the digits of the number 2^1000.

def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))  # Sum the digits of the number

# Calculate 2^1000
number = 2**1000

# Calculate and print the sum of the digits of 2^1000
print(f"Problem 16 - The sum of the digits of the number 2^1000 is: {sum_of_digits(number)}")


# Problem 17:
# Calculate the number of letters used if all the numbers from 1 to 1000 are written out in words.

def number_to_words(n):
    # Define word representations for numbers
    num_words = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
        16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
        30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
        80: 'eighty', 90: 'ninety'
    }

    if n <= 20:
        return num_words[n]
    elif n < 100:
        tens, below_ten = divmod(n, 10)
        return num_words[tens * 10] + ('' if below_ten == 0 else num_words[below_ten])
    elif n < 1000:
        hundreds, below_hundred = divmod(n, 100)
        return num_words[hundreds] + 'hundred' + ('' if below_hundred == 0 else 'and' + number_to_words(below_hundred))
    elif n == 1000:
        return 'onethousand'

def count_letters_in_words(limit):
    return sum(len(number_to_words(i).replace(' ', '').replace('-', '')) for i in range(1, limit + 1))

# Calculate the total number of letters for numbers from 1 to 1000
total_letters = count_letters_in_words(1000)

# Print the total number of letters
print(f"Problem 17 - The total number of letters used is: {total_letters}")


# Problem 19:
# Count how many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000).

import datetime

def count_sundays(start_year, end_year):
    sunday_count = 0  # Initialize the count of Sundays on the first of the month

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            if datetime.date(year, month, 1).weekday() == 6:  # Check if the first of the month is a Sunday (weekday 6)
                sunday_count += 1  # Increment the count

    return sunday_count

# Count the number of Sundays on the first of the month from 1901 to 2000
sundays = count_sundays(1901, 2000)

# Print the result
print(f"Problem 19 - The number of Sundays on the first of the month during the 20th century is: {sundays}")


# Problem 20:
# Calculate the sum of the digits in the number 100!

def factorial(n):
    # Calculate the factorial of n
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sum_of_digits(number):
    # Sum the digits of the given number
    return sum(int(digit) for digit in str(number))

# Calculate 100!
factorial_100 = factorial(100)

# Calculate and print the sum of the digits of 100!
print(f"Problem 20 - The sum of the digits in the number 100! is: {sum_of_digits(factorial_100)}")


# Problem 21:
# Evaluate the sum of all the amicable numbers under 10000.

def sum_of_divisors(n):
    # Calculate the sum of proper divisors of n
    divisors = [1]  # Start with 1, as it is a divisor of every number
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)

def find_amicable_numbers(limit):
    amicable_numbers = set()  # Use a set to avoid duplicates

    for a in range(2, limit):
        b = sum_of_divisors(a)
        if b != a and sum_of_divisors(b) == a:
            amicable_numbers.add(a)
            amicable_numbers.add(b)

    return sum(amicable_numbers)

# Calculate the sum of all the amicable numbers under 10000
sum_amicable_numbers = find_amicable_numbers(10000)

# Print the result
print(f"Problem 21 - The sum of all the amicable numbers under 10000 is: {sum_amicable_numbers}")



# Problem 23:
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def sum_of_divisors(n):
    # Calculate the sum of proper divisors of n
    divisors = [1]  # Start with 1, as it is a divisor of every number
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)

def is_abundant(n):
    # Check if a number is abundant
    return sum_of_divisors(n) > n

def find_non_abundant_sums(limit):
    abundant_numbers = set()
    for i in range(1, limit + 1):
        if is_abundant(i):
            abundant_numbers.add(i)

    non_abundant_sums = set(range(1, limit + 1))

    for a in abundant_numbers:
        for b in abundant_numbers:
            if a + b <= limit:
                non_abundant_sums.discard(a + b)

    return sum(non_abundant_sums)

# Calculate the sum of all positive integers which cannot be written as the sum of two abundant numbers
sum_non_abundant_sums = find_non_abundant_sums(28123)

# Print the result
print(f"Problem 23 - The sum of all the positive integers which cannot be written as the sum of two abundant numbers is: {sum_non_abundant_sums}")



# Problem 24:
# Find the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9.

import itertools

def find_millionth_permutation(digits):
    # Generate all lexicographic permutations of the given digits
    permutations = itertools.permutations(digits)

    # Find the millionth permutation (indexing starts at 0, so we need the 999999th element)
    millionth_permutation = next(itertools.islice(permutations, 999999, None))

    return ''.join(map(str, millionth_permutation))

# Calculate the millionth lexicographic permutation
millionth_permutation = find_millionth_permutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Print the result
print(f"Problem 24 - The millionth lexicographic permutation of the digits is: {millionth_permutation}")



# Problem 25:
# Find the index of the first term in the Fibonacci sequence to contain 1000 digits.

def find_fibonacci_index(digit_count):
    a, b = 1, 1  # Initialize the first two terms of the Fibonacci sequence
    index = 2  # Start from the second term

    while len(str(b)) < digit_count:
        a, b = b, a + b  # Update the terms to the next in the sequence
        index += 1  # Increment the index

    return index

# Calculate the index of the first Fibonacci number with 1000 digits
fibonacci_index_1000 = find_fibonacci_index(1000)

# Print the result
print(f"Problem 25 - The index of the first term in the Fibonacci sequence to contain 1000 digits is: {fibonacci_index_1000}")



# Problem 26:
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def find_longest_recurring_cycle(limit):
    longest_length = 0  # Initialize the longest cycle length
    d_with_longest_cycle = 0  # Initialize the denominator with the longest cycle

    for d in range(2, limit):
        remainders = {}  # Store remainders and their positions
        value, position = 1, 0

        while value != 0:
            value %= d
            if value in remainders:
                # Found a repeating cycle
                cycle_length = position - remainders[value]
                if cycle_length > longest_length:
                    longest_length, d_with_longest_cycle = cycle_length, d
                break
            remainders[value] = position
            value *= 10
            position += 1

    return d_with_longest_cycle

# Calculate the denominator with the longest recurring cycle in its decimal fraction part for d < 1000
d_with_longest_cycle = find_longest_recurring_cycle(1000)

# Print the result
print(f"Problem 26 - The value of d < 1000 with the longest recurring cycle in its decimal fraction part is: {d_with_longest_cycle}")


# Problem 27:
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_max_prime_generating_quadratic(limit):
    max_n = 0  # Initialize the maximum number of consecutive primes generated
    product = 0  # Initialize the product of coefficients a and b

    for a in range(-limit + 1, limit):
        for b in range(-limit, limit + 1):
            n = 0
            while is_prime(n * n + a * n + b):
                n += 1
            if n > max_n:
                max_n, product = n, a * b

    return product

# Calculate the product of the coefficients for the quadratic expression
product_of_coefficients = find_max_prime_generating_quadratic(1000)

# Print the result
print(f"Problem 27 - The product of the coefficients is: {product_of_coefficients}")



# Problem 28:
# Calculate the sum of the numbers on the diagonals in a 1001 by 1001 spiral.

def sum_spiral_diagonals(size):
    total_sum = 1  # Start with the center value, 1
    current_number = 1  # Initialize the current number in the spiral

    for layer in range(1, (size // 2) + 1):
        step = layer * 2  # Calculate the step size for the current layer
        for _ in range(4):  # Each layer has four corners
            current_number += step  # Calculate the number at the next corner
            total_sum += current_number  # Add the corner number to the total sum

    return total_sum

# Calculate the sum of the diagonals in a 1001 by 1001 spiral
spiral_sum = sum_spiral_diagonals(1001)

# Print the result
print(f"Problem 28 - The sum of the numbers on the diagonals in a 1001 by 1001 spiral is: {spiral_sum}")


# Problem 29:
# Calculate how many distinct terms are in the sequence generated by a^b for 2 <= a <= 100 and 2 <= b <= 100.

def distinct_powers(a_range, b_range):
    # Use a set to store distinct terms, as sets automatically handle duplicates
    terms = set()

    for a in range(a_range[0], a_range[1] + 1):
        for b in range(b_range[0], b_range[1] + 1):
            terms.add(a**b)  # Add each term a^b to the set

    return len(terms)  # The number of distinct terms is the size of the set

# Calculate the number of distinct terms for the given ranges
num_distinct_terms = distinct_powers((2, 100), (2, 100))

# Print the result
print(f"Problem 29 - The number of distinct terms in the sequence is: {num_distinct_terms}")



# Problem 30:
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def is_sum_of_fifth_powers(n):
    # Check if the number can be written as the sum of fifth powers of its digits
    return n == sum(int(digit)**5 for digit in str(n))

def sum_of_fifth_power_numbers():
    # A reasonable upper limit can be found by considering that for a d-digit number,
    # the maximum sum of fifth powers of its digits is d * 9^5. We stop when this maximum
    # is smaller than the smallest d-digit number (10^(d-1)). For 9^5 = 59049, this happens around 6 digits.
    upper_limit = 6 * 9**5

    total_sum = 0
    for i in range(2, upper_limit):
        if is_sum_of_fifth_powers(i):
            total_sum += i

    return total_sum

# Calculate the sum of all numbers that can be written as the sum of fifth powers of their digits
sum_fifth_powers = sum_of_fifth_power_numbers()

# Print the result
print(f"Problem 30 - The sum of all the numbers that can be written as the sum of fifth powers of their digits is: {sum_fifth_powers}")
