#factorial iterative solution

def athroisma(n):
    result = 0
    for i in range(1, n+1):
        result = result + i
    return result

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

n = input('Give me a number: ')
n = int(n)
print('To athroisma einai ' + str(athroisma(n)))
print('To paragontiko einai ' + str(factorial(n)))


#factorial recursive solution

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return 1 * factorial_recursive(n-1)


#fibonacci iterative solution

def fibonacci(n):
    if n<= 0:
        return -1
    if n == 1 or n == 2:
        return 1
    last = 1
    current = 1
    for i in range(3, n+1):
        next = current + last
        last = current
        current = next
    return current

    #fibonacci recursive solution

    def fibonacci_rec(n):
    if n <= 2:
        return 2
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)