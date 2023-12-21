
nim = ['2','3','1','0','3','1','0','8','5']
print(nim)

print("item indeks 0 (pertama)",nim[0])
print("item indeks 1 (kedua)",nim[1])

print(f"item indeks 0 (pertama){nim[0]}")
print(f"item indeks 1 (kedua) {nim[1]}")
print(f"item indeks terakhir {nim[len(nim)-1]}")
print(f"item indeks terakhir {nim[-1]}")
print(f"item indeks (pertama) {nim[-len(nim)]}")

data = ['nurasyah',2023,'Aktif']
nilai= [90,89,93,97]

print('nama: '+ data[0])
print('angkatan:', data[1])
print('status: '+ data[2])

 # >> nurasyah status Kuliah: Aktif
print(f'{data[0]} status Kuliah: {data[2]}')
# >> Data terbesar nilai adalah: 97
print(f'Data terbesar nilai adalah: {max(nilai)}')
# >> Data terkecil nilai adalah: 89
print(f'Data terkecil nilai adalah: {min(nilai)}')
# >> Rata-rata nilai adalah: 92.25
rataan = sum(nilai)/len(nilai)
print(f'Rata-rata nilai adalah: {rataan}')
# >> Jumlah nilai mahasiswa adalah: 4
print(f'Jumlah nilai {data[0]} adalah: {len(nilai)}')
print()

#tugas
data = [['nurasyah',2023,'Aktif'],
        [79,88,89,98,99],
        [20,22],
        ['S1-Reguler', 'Sistem Informasi B','Ganjil']]
print(data[0][0])
print(data[-1][0])
print(data[2][0:])
print()
matkul = ['matkul Agama islam',
          'matkul Pancasila',
          'matkul Bahasa Indonesia',
          'matkul Wawasan cinta IPTEK dan IMTAQ',
          'matkul Pengantar pemograman',]
sks = [2,3,2,3,3,]
matkul.append(('Pegantar teknologi informasi'))
matkul.append(('Kalkulus dasar 1'))
matkul.append(('sains terpadu'))
print(matkul)
sks.append((2))
sks.append((2))
sks.append((3))
print(sks)
print()
# Tambahkan matkul dan sks ke dalam data (pakai append)

# Daftar Mata kuliah
# Mata kuliah 1: Matkul1 dengan jumlah 2 sks
print(f'Mata kuliah1 : {matkul[0]} dengan jumlah {sks[0]} sks')
# Mata kuliah 2: Matkul2 dengan jumlah 3 sks
print(f'mata kuliah2 : {matkul[1]} dengan jumlah {sks[1]} sks')
# Mata kuliah 3: Matkul3 dengan jumlah 2 sks
print(f'mata kuliah3 : {matkul[2]} dengan jumlah {sks[2]} sks')
# Mata kuliah 4: Matkul4 dengan jumlah 3 sks
print(f'mata kuliah4 : {matkul[3]} dengan jumlah {sks[3]} sks')
# Mata kuliah 5: Matkul5 dengan jumlah 3 sks
print(f'mata kuliah5 : {matkul[4]} dengan jumlah {sks[4]} sks')
# Mata kuliah 6: Matkul6 dengan jumlah .. sks
print(f'mata kuliah6 : {matkul[5]} dengan jumlah {sks[5]} sks')
# Mata kuliah 7: Matkul7 dengan jumlah .. sks
print(f'mata kuliah7 : {matkul[6]} dengan jumlah {sks[6]} sks')
# Mata kuliah 8: Matkul8 dengan jumlah .. sks
print(f'mata kuliah8 : {matkul[7]} dengan jumlah {sks[7]} sks')
print()
# Tambah Nilai jadi 8 (pakai append)
print()
#nama mahasiswa: nurasyah
print(f'nama mahasiswa: {data[0][0]}')
#inisial nurasyah: n
print(f'inisial nurasyah: {data[0][0][0]}')
#NIM nurasyah: 231031085
nim_int = int(''.join(map(str, nim)))
print(f'nim {data[0][0]} nurasyah: {nim_int}')
#Program  nurasyah: S1-Reguler sistem informasi B 2023
print(f'Program  {data[0][0]} : {data[3][0]} {data[3][1]} {data[0][1]}')
#Angkatan nurasyah : Ganjil-2023
print(f'Angkatan nurasyah : {data[3][2]}-{data[0][1]}')
#total sks nurasyah: 8
print(f'total sks nurasyah adalah: {len(sks)}')
#Jumlah nilai nurasyah adalah: 5
print(f'Jumlah nilai {data[0][0]} adalah: {len(data[1])}')
#Data terbesar nurasyah adalah: 99
print(f'Data terbesar nurasyah adalah: {max(data[1])}')
#Data terkecil nurasyah adalah: 79
print(f'Data terkecil nurasyah adalah: {min(data[1])}')
# Rata-rata nilai nurasyah adalah: 90.6
print(f'Rata-rata nilai nurasyah adalah: {sum(data[1])/len(data[1])}')


