# Buatlah function starFormation(n) yang dgunakan untuk mencetak output berupa formasi bintang berikut ini:
# *
# * *
# * * *
# * * * *

#Berikut ini adalah sintaksnya: (n) adalah parameternya
def starFormation(n):
    for i in range(1, n + 1):
        for j in range(i):
            print('*', end='')
        print()

def starFormationDescending(x):
    for i in range(x + 1):
        for j in range(x - i):
            print('*', end='')
        print()


# (5) adalah argumennya
print(starFormation(5))
print(starFormationDescending(5))
