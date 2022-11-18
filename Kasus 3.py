# Buatlah function findRange(data) yang digunakan untuk menentukan nilai range dari beberapa data berupa bilangan
# (numbers) yang diberikan pada argumennya. Di mana nilai range adalah nilai maksimum data dikurangi nilai minimum data.
# Misalnya findRange(10, 11, 14, 20), maka function ini akan mengembalikan nilai 10 yang merupakan nilai range data.
# Nilai ini diperoleh dari pengurangan nilai maksimumnya yaitu 20 terhadap nilai minimumnya yaitu 10.


def findRange(*myData):
    # Kita inisiasi atau deklarasikan dari tempat penampungan argumen yang akan di inputkan
    maks = myData[0]
    min = myData[0]
    # Perulangan berikut ini akan mencari nilai maksimum dan minimum dari argumen yang nantinya akan diinputkan
    for data in myData:
        if data > maks:
            maks = data
        if data < min:
            min = data
    # Kita kembalikan nilai agar nilai yang ingin kita cari didapatkan
    return maks-min


print(findRange(5, 1, 4, 6, 10, 33, 12, 6, 9, 13))
