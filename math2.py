# returns True or False depending on the primality of n
def isPrime(n):
    if n == 1:
        return False
    else:
        return n==2 or not any(n%i==0 for i in range(2, (n//2)+1))

# returns the nth fibonacci number 
def fibonacci(n):
    n1, n2 = 0, 1
    
    for i in range(0, n):
        n1, n2 = n2, n1 + n2
        
    return n1

# returns the factorial of n (recursive implementation)
def factorial(n):
    if n < 0:
        raise ValueError(f'Value must be postive. You entered {n}') 
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) 

# returns product of numbers in a list
def product(L):
    n = 1
    for i in L:
        n *= i
    
    return n

# returns the mean (as a float) of the elements in an array
def mean(L):
    return sum(L) / len(L)

# returns nth pentagonal number as an int
def pentaNum(n):
    return n * (3 * n - 1) // 2

# computer the nth triangle number (using Gauss's formula)
def triangleNumber(n):
    return int(n / 2 * (n + 1))

# generator based on triangleNumber()
def triangleGen():
    i = 0
    while 1:
        yield triangleNumber(i)
    

# returns a list of factors of number n
def divisors(n):
    L = [i for i in range(1, n // 2 + 1) if n % i == 0]
    L.append(n)
    return L

# returns number of divisors of a number (including 1)
def divNum(n):
    count = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            count += 1
    
    return count + 1

# returns a list with all duplicates removed
def purify(L):
    outL = []
    for item in L:
        if item not in outL:
            outL.append(item)
    return outL

# returns a boolean value depending on whether a number is a palindrome or not
def isPalindrome(n):
    return str(n) == str(n)[::-1]

# sieve of eratosthenes
#
#def sieve(n):
#    L = [i for i in range(2, n + 1)]
#    P = [i for i in range(2, len(L) // 2) if isPrime(i)]
#    
#    for n in P:
#        for i in L:
#            if n != i and i % n == 0:
#                L.remove(i)
#    
#    return P

 # unfinished implementation

#def sieve(n):
#    L = [i for i in range(2, n + 1)]
#    done = False
#    while not done:
#        p = L[0]
#        for n in L[1:len(L)]:
#            if n % p == 0:
#                L.remove(n)
#    return L


def sieve(L):
    return [n for n in L if isPrime(n)]

# binary search implementation
def binarySearch(L, x):
    L = sorted(L)
    found = False
    low = 0
    high = len(L) - 1
    
    while not found:
        mid = (low + high) // 2
        if L[mid] == x:
            found = True
            
        elif L[mid] > x:
            high = mid
            
        elif L[mid] < x:
            low = mid
    
    return found

# returns length of a collatz chain
def collatz(n):
    length = 0
    done = False
    while not done:
        if n == 1:
            done = True
        if n % 2 == 0:
            n /= 2
            length += 1
        elif n % 2 != 0:
            n = (3*n) + 1
            length += 1
    return length


def merge(L):
    pass

# returns a list of lists containing pairs that add up to a specified n
def allSums(n):
    L = []
    a, b = n, 0
    while a != 0:
        L.append([a, b])
        a -= 1
        b += 1
    return L