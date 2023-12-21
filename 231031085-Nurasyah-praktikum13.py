import os

os.system("cls")

# BAGIAN  1

# Fungsi Rekursif Fibonacci
def fibonacci(n):
    if n < 0:
        print("Tidak ada bilangan yang bernilai negatif")
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Program Utama
nilai = 20
hasil = fibonacci(20)
print("Finobacci(%d)=%d" % (nilai, hasil))
print()

# BAGIAN 2

# Fungsi Rekursif Fibonacci
def fibonacci(n):
    if n < 0:
        print("Tidak ada bilangan yang bernilai negatif")
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# input nilai
nilai = int(input("masukan sebuah bilangan: "))

# Program Utama
hasil = fibonacci(nilai)
print("Finobacci(%d)=%d" % (nilai, hasil))
