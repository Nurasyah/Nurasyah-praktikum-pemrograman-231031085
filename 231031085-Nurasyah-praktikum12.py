import os

os.system("cls")

# BAGIAN 1
# Fungsi Rekursif factorial dengan perulangan
def faktorial(nilai):
    if nilai <= 1:
        return 1
    else:
        return nilai * faktorial(nilai - 1)


# Program Utama
for i in range(11):
    print("%2d ! = %d" % (i, faktorial(i)))
print()

#BAGIAN 2
# Fungsi Rekursif factorial dengan perulangan
def faktorial(nilai):
    if nilai <= 1:
        return 1
    else:
        return nilai * faktorial(nilai - 1)

# input nilai
nilai = int(input("masukan nilai:"))

# Program Utama
print(f" Hasil Faktorial dari 0 sampai {nilai}:")
for i in range(nilai + 1):
    print(f"{i}! = {faktorial(i)}")
