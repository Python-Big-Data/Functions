# Buatlah function power(a, n) yang digunakan untuk menentukan nilai dari a^n, di mana a adalah bilangan riil dan n
# adalah bilangan bulat non negatif. Petunjuk: gunakan konsep rekursif!

# Menggunakan konsep rekursif artinya memanggil variabel sendiri

def power1(a, n):
    # argumen yang diinputkan haruslah integer
    if (n == 0):
        return 1
    else:
        return a * power(a, n-1)

# Jawaban sahal
def power(a, n):
    x = a ** n
    return x


print(power1(2, 7))
print(power(2, 7))