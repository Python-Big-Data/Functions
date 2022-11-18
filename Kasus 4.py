# Buatlah function power(a, n) yang digunakan untuk menentukan nilai dari a^n, di mana a adalah bilangan riil dan n
# adalah bilangan bulat non negatif. Petunjuk: gunakan konsep rekursif!

# Menggunakan konsep rekursif artinya memanggil variabel sendiri
def power(a, n):
    x = a ** n
    return x

print(power(2, 4))