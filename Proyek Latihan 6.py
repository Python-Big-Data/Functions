# Buatlah sebuah file Python dengan nama statistik.py yang hanya berisi function-function berikut ini:
# a. Buatlah function sum(a, b, c, d, ...) dengan jumlah parameter tidak terbatas, yang digunakan untuk mencari jumlah
# total seluruh nilai parameter yang berupa bilangan. Misalnya: sum(3, 5, 6, 7) akan menghasilkan nilai 21,
# sum(1, 0, 0, 2, 4) akan menghasilkan nilai 7.

# b. Buatlah function average(a,b, c, d, ...) dengan jumlah parameter tidak terbatas, yang digunakan untuk mencari
# rata-rata dari seluruh nilai parameternya berupa bilangan. Manfaatkan function sum(a, b, c, d, ...) untuk
# menghitung jumlah total data dalam proses perhitungan rata-ratanya.

# c. Buatlah function maks(a, b, c, d, e, ...) dengan jumlah parameter tidak terbatas, yang digunakan untuk mencari
# nilai maksimum dari seluruh parameternya.

# d. Buat pula function min(a, b, c, d, ...) dengan jumlah parameter tidak terbatas, yang digunakan untuk mencari nilai
# minimum dari seluruh nilai parameternya.

# a
# Soal berikut mirip seperti Simple array sum
def sum(*myData):
    sum = 0
    for i in myData:
        sum = sum + i
    return sum

print(sum(1, 0, 0, 2, 4))

# b
def average(masukan):
        Array = len(masukan)
        ratarata = sum() / Array
    return ratarata

print(average(1, 0, 0, 2, 4))

# c
