# Berdasarkan function yang didapatkan dari Kasus 2 dan Proyek Latihan nomor 1 tersebut, gunakan keduanya untuk
# membentuk formasi bintang seperti berikut.
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *


def staircaseascending(n):
    for i in range(1, 1 + n):
        for j in range(i):
            print("* ", end='')
        print("\n")

def staircasedescending(x):
    for i in range (x):
        for j in range(x - i):
            print("* ", end='')
        print("\n")

print(staircaseascending(4))
print(staircasedescending(4))
