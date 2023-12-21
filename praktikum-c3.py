import os
os.system('clear')

print (" praktikum 3")

nama= "nurasyah"
nim = "231031085"
meet = "prakktikum c (string)"
prodi = "sistem informasi c"
email = "asyahtasya70@gmail.com"
ttl = "13-12-2004"
alamat = "jl.bakaru"
asal  = "pinrang"
hobi = "rebahan"
tinggi = "152cm"

sp = 60      
print ('-'*sp)
print (nama.upper().center (sp))
print (nim.center(sp))
print ('\n'*2)
print (meet.rjust(sp))
print (prodi.rjust(sp))
print (email.lower().rjust(sp))
print ('-'*sp)

print (f'''\thalo,nama saya {nama} dengan nim {nim} dari prodi {prodi}  ini adalah file {meet}.terima kasih.
\n''')

print (f'''biodata saya,
nama\t:{nama.upper()}
nim \t:{nim}
prodi\t:{prodi}
ttl\t:{ttl}
alamat\t:{alamat}
asal\t:{asal}
hobi\t: {hobi}
tinggi\t:{tinggi}
         ''')

#tugas

stat1  = "duFort Frankel Sir Issac"
# Issac duFort Frankel Sir
a      = stat1.split()
stat1 =" ".join( [a[-1],a[0],a[1],a[2]])
print(stat1)
print()


state2 = "duFort Frankel Sir Issac"
a = "duFort Frankel Sir Issac"
# d F S Issac
print  ("duFort"[0], "Frankel"[0], "Sir"[0], "Issac")
print()

stat3 = "duFort Frankel Sir Issac"
# duFort F S I
a = "duFort Frankel Sir Issac"
print ("duFort", "Frankel"[0], "Sir"[0], "Issac"[0])
print()


stat4 = "duFort Frankel Sir Issac"
# I duFort Frankel Sir
a = stat4.split()
stat4 = " ".join([a[-1][0], a[0], a[1], a[2]],)
print(stat4)
print()
                 
stat5 = "duFort Frankel Sir Issac"
# Issac d F S
a  = stat5.split()
stat5 = " ".join([a[-1], a[0][0],a[1][0],a[2][0]])
print(stat5)
print()

stat6 = 'duFort Frankel Sir Issac'
# ISSAC D F S
a = stat6.split()
stat6 = " ".join([a[-1], a[0][0], a[1][0], a[2][0]]).upper()
print(stat6)
print()

stat7 = "#duFort Frankel Sir Issac$"
# duFort Frankel Sir Issac
a = stat7.strip("#,$")
print (a)
print()

stat8 = '#duFort-Frankel-Sir-Issac$'
# duFort Frankel Sir Issac
b = a.strip("#,$")
print(b)
print()
      
stat9 = "#duFort@ ^Frankel* (Sir( (Issac$"
# duFort Frankel Sir Issac
b = a.strip("#,@,$")
print (b)
print()

stat10 = '#duFort@-^Frankel*-(Sir(-(Issac$'
# DUFORT FRANKEL SIR ISSAC
b = a.strip("#,@,$").upper()
print(b)
print()

