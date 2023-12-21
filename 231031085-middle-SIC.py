'''UTS
1. Buat variabel jenis list berikut.
    
    BIO =  ['Nama Lengkap',
            'NIM',
            'Tanggal-Bulan-Tahun Lahir'
            'Sistem Informasi C',
            '2023-2024',
            'S1',
            'aktif',
            'ganjil',
            'Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu rencana studi mahasiswa']

#(NOTED: sesuaikan dengan data anda)
            
2. Buat variabel jenis nested list berikut.

MK =   [['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216',],
        ['Matkul1','Matkul2','Matkul3','Matkul4','Matkul5','Matkul6','Matkul7','Matkul8'],
        [2,3,3,2,3,3,3,2],
        ['Selasa','Senin','Rabu','Senin','Kamis','Kamis','Kamis','Kamis'],
        ['07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10']]

#(NOTED: Ubah Nama Matakuliah, Jumlah SKS, waktu kuliah, dan jadwal)
        
3. Susun Kode dengan hasil runing seperti berikut.
           
            
             INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE
                             JURUSAN SAINS
                    KARTU RENCANA STUDI MAHASISWA
                           GANJIL 2023/2024

                    
Nama Lengkap    : NAMA LENGKAP
NIM             : 60022010
Program/prodi   : S1/Sistem Informasi C
Tahun Masuk     : 2023 Ganjil
Status          : Aktif
|--|--  10  --|--           26         --|--5--|-- 8  --|
---------------------------------------------------------
No. Kode      |      Mata Kuliah         | SKS |  Hari  |
---------------------------------------------------------
1   22A1209   | Matkul1                  |  2  | Senin  |
2   22A1210   | Matkul2                  |  3  | Selasa |
3   22A1211   | Matkul3                  |  3  | Rabu   |
4   22A1212   | Matkul4                  |  2  | Senin  |
5   22A1213   | Matkul5                  |  3  | Kamis  |
6   22A1214   | Matkul6                  |  3  | Kamis  |
7   22A1215   | Matkul7                  |  3  | Kamis  |
8   22A1216   | Matkul8                  |  2  | Kamis  |
---------------------------------------------------------
                        TOTAL SKS           21           
---------------------------------------------------------
|---------------------------57---------------------------|
Summary:
Jumlah Mata Kuliah       : 8
Jumlah Mata Kuliah 2 SKS : 3 Mata Kuliah
Jumlah Mata Kuliah 3 SKS : 5 Mata kuliah
Mata Kuliah hari Senin   : 2 Mata Kuliah
Mata Kuliah hari Selasa  : 1 Mata Kuliah
Mata Kuliah hari Rabu    : 1 Mata Kuliah
Mata Kuliah hari Kamis   : 1 Mata Kuliah
Mata Kuliah hari Jumat   : 0 Mata Kuliah
                                              Parepare, 25 Oktober 2023



                                                     NAMA LENGKAP      
                                                     ------------
'''



# Tulis Kode Jawaban di bawah!

bio = [     'Nurasyah',
            '231031085',
            '13-12-2004',
            'Sistem Informasi C',
            '2023-2024',
            'S1',
            'aktif',
            'ganjil',
            'Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu rencana studi mahasiswa']

mk = [['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216',],
        ['kalkulus dasar','pancasila','pti','bahasa','cinta dan iptek','sainster','agama ','pengantar pemprograman'],
        [3,2,3,2,2,3,2,3],
        ['Selasa','jumat','jumat','jumat','Kamis','rabu','jumat','selasa'],
        ['07.30-09.10','13.30-15.10','15.20-17.00','09.20-11.00','09.20-11.00','15.10-17.00','07.10-09.10','13.30-15.10']]

print(bio[-4].upper().center(71))
print(bio[-2].upper().center(71))
print(bio[-1].upper().center(71))
strr = bio[-5]+' '+bio[4].replace('-','/')
print(strr.upper().center(71))

print(f'''
Nama Lengkap    : {bio[0].upper()}
NIM             : {bio[1]}
Program/prodi   : {bio[5]}/{bio[3]}
Tahun Masuk     : {bio[4].title()}
Status          : {bio[6]}''')

print('|--|--  10  --|--           26         --|--5--|-- 8  --|')
print('-'*57)
print('No.'+'|'+'Kode'.ljust(10)+'|'+'mata kuliah'.center(26)+'|'+'SKS'.center(5)+'|'+'Hari'.center(8)+'|')
print('-'*57)
print('1. '+'|'+'22A1209'.ljust(10)+'|'+'kalkulus dasar'.center(26)+'|'+'3'.center(5)+'|'+'selasa'.center(8)+'|')
print('2. '+'|'+'22A1210'.ljust(10)+'|'+'pti'.center(26)+'|'+'2'.center(5)+'|'+'jumat'.center(8)+'|')
print('3. '+'|'+'22A1211'.ljust(10)+'|'+'bahasa'.center(26)+'|'+'3'.center(5)+'|'+'jumat'.center(8)+'|')
print('4. '+'|'+'22A1212'.ljust(10)+'|'+'cinta dan iptek'.center(26)+'|'+'22'.center(5)+'|'+'kamis'.center(8)+'|')
print('5. '+'|'+'22A1213'.ljust(10)+'|'+'sainster'.center(26)+'|'+'2'.center(5)+'|'+'rabu'.center(8)+'|')
print('6. '+'|'+'22A1214'.ljust(10)+'|'+'agama '.center(26)+'|'+'3'.center(5)+'|'+'jumat'.center(8)+'|')
print('7. '+'|'+'22A1215'.ljust(10)+'|'+'pemprograman'.center(26)+'|'+'2'.center(5)+'|'+'selasa'.center(8)+'|')
print('8. '+'|'+'22A1216'.ljust(10)+'|'+'pancasila'.center(26)+'|'+'3'.center(5)+'|'+'jumat'.center(8)+'|')
print('-'*57)


print(f"                      TOTAL SKS               {20}  ")

print("--------------------------57-------------------------------")
print
print(f'Summary:')
print(f'Jumlah Mata Kuliah       : {len(mk[1])}')
#Jumlah Mata Kuliah 2 SKS : 4 Mata Kuliah
print(f"Jumlah Mata Kuliah 2 SKS : {mk[2].count(2)} Mata Kuliah")
#Jumlah Mata Kuliah 3 SKS : 4 Mata kuliah
print(f"Jumlah Mata Kuliah 3 SKS : {mk[2].count(3)} Mata Kuliah")
#Mata Kuliah hari Senin   : 0 Mata Kuliah
print(f"Mata Kuliah hari Senin   : {mk[3].count('senin')} Mata Kuliah")
#Mata Kuliah hari Selasa  : 2 Mata Kuliah
print(f"Mata Kuliah hari selasa  : {mk[3].count('selasa')} Mata Kuliah")
#Mata Kuliah hari Rabu    : 1 Mata Kuliah
print(f"Mata Kuliah hari rabu    : {mk[3].count('rabu')} Mata Kuliah")
#Mata Kuliah hari Kamis   :2  Mata Kuliah
print(f"Mata Kuliah hari kamis   : {mk[3].count('Kamis')} Mata Kuliah")
#Mata Kuliah hari Jumat   :4 Mata Kuliah
print(f"Mata Kuliah hari Jumat   : {mk[3].count('jumat')} Mata Kuliah")

print('                                                                 Parepare, 25 Oktober 2023\n\n\n')
print('                                                                           Nurasyah')
print('                                                                           -------')
print('...')
