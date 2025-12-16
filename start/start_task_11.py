def factorial(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    k = 1
    for i in range(1, n+1):
        k = k * i
    return k
s = int(input())
print(factorial(s))