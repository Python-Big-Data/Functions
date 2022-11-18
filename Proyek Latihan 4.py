# Buatlah function factorial(n) yang digunakan untuk menghitung nilai n faktorial. Output dari function ini adalah
# sebuah bilangan yang merupakan nilai dari n faktorial tersebut.

# Gunakan function tersebut untuk menghitung nilai dari:
# a. C( 5, 3)
# b. P (10, 7)

def factorial(n, fact):
    for i in range (1, n+1):
        fact = fact * i
    return fact

print(factorial(5, 3))
print(factorial(10, 7))