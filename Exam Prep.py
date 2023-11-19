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
