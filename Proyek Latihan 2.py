# Buatlah function untuk  mencetak output berupa formasi bintang berikut ini:
# * * * *
# * * *
# * *
# *

def staircasedescending(n):
    for i in range(n):
        for j in range(n - i):
            print('* ', end='')
        print("\n")

print(staircasedescending(4))