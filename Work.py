# Coding interview ustions


# 🔹 Basic Level
# Reverse a string without using slicing.
string = "hello"
print(string[::-1])

# Find the factorial of a number.
fact = 5
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(fact))

# Check if a number is prime.
def prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(prime(8))
    


# Find the largest number in a list.
li = [1,5,2,67,3]
li.sort()
print(li[-1])


# Count vowels and consonants in a string.
vowels=['A','E','I','O','U']
vo = "hello"
count = 0
for i in vo.upper():
    if i in vowels:
        count += 1
print("count",count)

# Check if a string is a palindrome.
def palindrome(pa):
    if pa[::-1] == pa:
        return True
    return False
print(palindrome("madam"))
         

# Sum all elements in a list without using sum().

val = [1,2,3,4,5,6]
def summ(val):
    count = 0
    for i in range(len(val)):
        count += val[i]
    return count
print(summ(val))

# Find the length of a string without using len().

def stwithlen(val):
    count = 0
    for i in val:
        count += 1
    return count
print(stwithlen("surendran"))
    


# Swap two variables without using a third variable.
a= 2
b= 3
a,b = b, a
print("a = ",a,"b = ",b)


# Print the Fibonacci sequence up to n terms.
def fib(n):
    a , b = 0,1
    for _ in range(n):
        print(a ,end="")
        a , b=b, a+b
fib(7)
print()

# 🔹 Intermediate Level
# Find the second largest number in a list.
def secountlag(va):
    val.sort()
    print(val)
    print(val[-2])
secountlag(val)
# Count the frequency of characters in a string.

# Find all pairs in an array with a given sum.

# Remove duplicates from a list without using set().

# Merge two sorted lists into one sorted list.

# Find the intersection of two lists.

# Find the most frequent element in a list.

# Check if two strings are anagrams.

# Rotate a list by k positions.

# Find the GCD of two numbers.

# 🔹 Advanced Level
# Implement a decorator to measure function execution time.

# Merge two dictionaries.

# Find all permutations of a string.

# Flatten a nested list.

# Implement binary search.

# Implement bubble sort.

# Find the longest word in a sentence.

# Generate all subsets of a given set.

# Reverse words in a sentence.

# Find duplicate elements in a list.

# Implement a stack using a list.

# Implement a queue using collections.deque.

# Check if a linked list has a cycle.

# Find the first non-repeating character in a string.

# Serialize and deserialize a Python object.

# Read a file and count the number of lines.

# Implement a class for a Bank Account.

# Implement a simple calculator using OOP.

# Find the longest common prefix among strings.

# Implement a custom iterator.
