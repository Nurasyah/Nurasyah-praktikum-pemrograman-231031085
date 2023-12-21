import os

os.system("clear")

#jawaban nomor 1 ganjil
# Langkah a: Input bilangan A
bilangan = int(input("Masukkan bilangan: "))

# Langkah b: Cek apakah bilangan adalah kelipatan tiga
if bilangan % 3 == 0:
    # Langkah c: Cetak pesan jika bilangan adalah kelipatan tiga
    print(f"{bilangan} adalah bilangan Kelipatan 3")
else:
    # Langkah c: Cetak pesan jika bilangan bukan kelipatan tiga
    print(f"{bilangan} adalah bilangan Bukan Kelipatan 3")

# Langkah d: Selesai
 
#jawaban nomor 2
#bagian A program penjumlahan waktu
 # Fungsi untuk menjumlahkan waktu
def tambah_waktu(waktu_awal, jam_tambahan, menit_tambahan):
    # Memecah waktu awal menjadi jam dan menit
    jam_awal, menit_awal = map(int, waktu_awal.split(':'))
    
    # Menambahkan jam dan menit tambahan
    jam_hasil = jam_awal + jam_tambahan
    menit_hasil = menit_awal + menit_tambahan
    
    # Menangani penambahan yang melebihi 60 menit
    if menit_hasil >= 60:
        jam_hasil += 1
        menit_hasil -= 60
    
    # Menangani penambahan yang melebihi 24 jam
    jam_hasil = jam_hasil % 24
    
    return f'Waktu sekarang menunjukkan Pukul {jam_hasil:02}:{menit_hasil:02}'

# Input waktu awal
waktu_awal = input('Masukkan waktu awal (HH:MM): ')
jam_tambahan = int(input('Masukkan jumlah jam tambahan: '))
menit_tambahan = int(input('Masukkan jumlah menit tambahan: '))

# Menampilkan hasil penjumlahan waktu
hasil_penjumlahan = tambah_waktu(waktu_awal, jam_tambahan, menit_tambahan)
print(hasil_penjumlahan)

#bagian B program selisih waktu
# Fungsi untuk menghitung selisih waktu
def selisih_waktu(waktu_awal, jam_kurang, menit_kurang):
    # Memecah waktu awal menjadi jam dan menit
    jam_awal, menit_awal = map(int, waktu_awal.split('.'))
    
    # Mengurangkan jam dan menit yang ditentukan
    jam_hasil = jam_awal - jam_kurang
    menit_hasil = menit_awal - menit_kurang
    
    # Menangani pengurangan yang melebihi 60 menit
    if menit_hasil < 0:
        jam_hasil -= 1
        menit_hasil += 60
    
    # Menangani pengurangan yang melebihi 24 jam
    jam_hasil = (jam_hasil + 24) % 24
    
    return f'Waktu sekarang menunjukkan Pukul {jam_hasil:02}:{menit_hasil:02}'

# Input waktu awal
waktu_awal = input('Masukkan waktu awal (HH.MM): ')
jam_kurang = int(input('Masukkan jumlah jam yang dikurangkan: '))
menit_kurang = int(input('Masukkan jumlah menit yang dikurangkan: '))

# Menampilkan hasil selisih waktu
hasil_selisih = selisih_waktu(waktu_awal, jam_kurang, menit_kurang)
print(hasil_selisih)



