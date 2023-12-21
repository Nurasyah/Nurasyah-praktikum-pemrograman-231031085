import os
import random as rd

os.system("cls")

angka = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
com   = rd.choice(angka)
a = True
limit = 3
i = 0

while a:
    i += 1
    pilih = input("MASUKAN ANGKA:")
    if pilih == com:
        print(f"SELAMAT")
        print(f"PILIHAN KAMU BENAR YAITU {pilih} :)")
        a = False
    else:
        if i < limit:
            print("TEBAKAN KAMU SALAH! COBA LAGI.")
            print(f"kesempatan anda tersisa {limit-i} kali!")
            a = True
        else:
            print("KESEMPATAN KAMU HABIS :(")
            print("jangan sedih, coba lagi lain kali")
            a = False

# tugas : buat program tebak angka 1 sampai 10 dengan batas
# kesempatan 3 kali. berikan pesan "kesempatan anda tersisah x kali"
