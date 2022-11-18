# Buatlah function isPrime(x) yang digunakan untuk menentukan apakah x suatu bilangan prima atau tidak. Function
# mengembalikan nilai True jika x adalah bilangan prima dan False jika bukan. Bilangan prima adalah bilangan bulat
# positif lebih besar dari 1 yang hanya tidak memiliki pembagi habis selain 1 dan bilangan itu sendiri.

def isPrime(x):
    if x / x == 1 and x > 1:
        x = True
    else:
        x = False
    return x

print(isPrime(1))
print(isPrime(2))
print(isPrime(3))
print(isPrime(5))
print(isPrime(7))
print(isPrime(11))
print(isPrime(13))