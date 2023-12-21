import os

def judul():
    os.system("cls")
    print("PROGRAM MENGHITUNG VOLUME DAN LUAS PERMUKAAN BALOK")
    print("BANGUN RUANG BALOK")
    print()

def inputan():
    p = float(input("masukan panjang: "))
    l = float(input("masukan lebar:   "))
    t = float(input("masukan tinggi:  "))
    return p, l, t

def perhitungan(p, l, t):
    vol = p * l * t
    luas = 2 * (p * l + p * t + l * t)
    luas_non_tutup = luas - p * l
    return vol, luas, luas_non_tutup

def tampilkan(jenis, nilai):
    print(f"nilai dari {jenis} adalah: {nilai}")

def pilihan():
    pilih = input("apakah lanjutkan? [y/n]")
    if pilih == "y":
        a = True
    else:
        a = False
        print("sampai jumpa lagi")
    return a

def main():
    judul()                                             # judul
    p, l, t = inputan()                               # inputan
    vol, luas, luas_non_tutup = perhitungan(p, l, t)  # pnerhitunga
    # tampilkan
    tampilkan("volume:", vol)
    tampilkan("luas permukaan:", luas)
    tampilkan("luas permukaan tanpa tutup:", luas_non_tutup)
    a = pilihan()  # pilihan

a = True
while a:
    main()