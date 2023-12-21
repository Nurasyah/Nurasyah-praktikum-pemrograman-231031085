import os

os.system("cls")

#BAGIAN 1
nilai = 5
def hitung_faktorial(nilai):
    # Mencari Faktorial dengan input
    if nilai > 2:
        return nilai * hitung_faktorial(nilai - 1)
    return 2

# Program Utama mulai di sini
faktorial = hitung_faktorial(nilai)
print(f"Nilai Faktorial dari {nilai}! = {faktorial}")
print()

# BAGIAN 2
nilai = int(input("Masukan Nilai yang akan di faktorial = "))

def hitung_faktorial(nilai):
    # Mencari Faktorial dengan input
    if nilai > 1:
        return nilai * hitung_faktorial(nilai - 1)
    return 1

# Program Utama mulai di sini
faktorial = hitung_faktorial(nilai)
print(f"Nilai Faktorial dari {nilai}! = {faktorial}")
