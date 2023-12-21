import os
import random as rd
os.system("clear")

warna = ['merah','putih','hitam']
com = rd.choice(warna)
a = True

while a:
    pilih = input('masukan pilihan [merah,putih,hitam]:')
    if pilih == com:
        print(f'pilihan anda benar yaitu {pilih}')
        a = False
    else:
        print('tebakan anda salah! coba lagi.')


