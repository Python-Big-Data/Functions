# Buatlah function isPythagoras(a, b, c) yang digunakan untuk menentukan apakah pasangan a, b, c yang merupakan sisi-
# sisi sebuah segitiga merupakan triple Pythagoras atau bukan.Function tersebut menghasilkan nilai boolean: True apabila
# a, b, c merupakan triple Pyhagoras dan False jika ketiganya bukan triple Pythogoras. Keterangan: c merupakan sisi
# miring segitiga. Untuk mengecek benar tidaknya functions yang Anda buat, ujilah dengan beberapa pasangan nilai a, b, c
# berikut ini.

# a = 3, b = 4, c = 5  --> True
# a = 5, b = 9, c = 12 --> False
# a = 8, b = 6, c = 1- --> True
# a = 7, b = 8, c = 11 --> False

def isPythagoras(a, b, c):
    if (a**2 + b**2 == c**2):
        return True
    else:
        return False

print(isPythagoras(3,4,5))