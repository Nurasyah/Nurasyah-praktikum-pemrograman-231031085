print ('nama  : nurasyah')
print ('nim   : 231031085')
print ('prodi : sistem informasi')
print ('tanggal lahir :13-12-2004')

a=85
print ('Nilai a =',a )
a=85
a +=1
print ('Nilai a +=1 akan menjadi' ,a)


a=85
a-=1
print ('Nilai a -=1 akan menjadi',a)

a=85
a*=2
print ('Nilai a *=2 akan menjadi',a)
a=85
a/=2
print ('Nilai a /=2 akan menjadi',a)

a=85
a//=2
print ('Nilai a %=2 akan menjadi',a)

a=85
a**=2
print ('Nilai a %=2 akan menjadi',a)

#OR

b=True
print ('Nilai b =',b )

b|=False
print('Nilai b|= False akan menjadi',b )

b=False
print ('Nilai b =',b )

b=False
print ('Nilai b|= False akan menjadi',b )


#AND

b=True
print ('Nilai b =',b )
b&= False
print ('Nilai b&= False akan menjadi',b )
b=False
print ('Nilai b =',b )
b&= False
print ('Nilai b&= False akan menjadi',b )

#XOR

b= True
print ('Nilai b =',b )
b ^= False
print ('Nilai b^= False akan menjadi',b )
       
b = False
print ('Nilai b =',b )
b ^= False
print ('Nilai b^= False akan menjadi',b )

#Shifting

c=0b0100
print ('Nilai c =',format (c, '04b') )
c>>=1
print ('Nilai c > >=1 akan menjadi',format (c , '04b') )
c=0b0100
c<<=1
print ('Nilai c < <=1 akan menjadi',format (c , '04b') )


# operator perbandingan

a=5
b=10
print (' ================== Besar dari 10 ')
hasil  = a>10
print (a ,'> 10 adalah ',hasil )
hasil = b>10
print (b ,'> 10 adalah ',hasil )


a=5
b=10
print (' ================== Kecil dari 10 ')
hasil = a<10
print (a ,'< 10 adalah ', hasil )
hasil = b>10
print (b ,'< 10 adalah ', hasil )


print (' ================== Besar atau sama dari 10')
hasil = a>=10
print (a ,'>= 10 adalah',hasil )
hasil = b>=10
print (b ,'>= 10 adalah',hasil )

print (' ================== Besar atau sama dari 10')
hasil = a<=10
print (a ,'<= 10 adalah',hasil )
hasil = b<=10
print (b ,'<= 10 adalah',hasil )

print ('================== Sama dengan 10')
hasil = a==10
print (a ,' == 10 adalah',hasil )
hasil = b==10
print (b ,'== 10 adalah',hasil )

print ('================== Tidal sama dengan 10')
hasil = a!=10
print (a ,' != 10 adalah',hasil )
hasil = b!=10
print (b ,'!= 10 adalah',hasil )

#OPERATOR LOGIKA

print ('============= NOT =============')
a = True
c = not a

print ('a adalah',a )
print ('------c = not a- - - -- - - NOT')
print ('c adalah',c )


print ('============= OR =============')
a = True
b = True
c = a or b
print (a ,'OR',b ,'menjadi ',c )

a = True
b = False
c = a or b
print (a ,'OR ',b ,'menjadi ',c )

a = False
b = True
c = a or b
print (a ,'OR ',b ,'menjadi ',c )
a = False
b = False
c = a or b
print (a ,'OR ',b ,'menjadi ',c )

print (' ============= AND ============= ')
a = True
b = True
c = a and b
print (a ,'AND ',b ,'menjadi ',c )

a = True
b = False
c = a and b
print (a ,'AND ',b ,'menjadi ',c )

a = False
b = True
c = a and b
print (a ,'AND ',b ,'menjadi ',c )

a=False
b = False
c = a and b
print (a ,'AND ',b ,'menjadi ',c )

print (' ============= XOR ============= ')
a = True
b = True
c = a ^ b
print (a ,'^',b ,'menjadi ',c )

a = True
b = False
c = a ^ b
print (a ,'^',b ,'menjadi ',c )


a = False
b = True
c = a ^ b
print (a ,'^',b ,'menjadi ',c )

a = False
b = False
c = a ^ b
print (a ,'^',b ,'menjadi ',c )

#TUGAS

print ('============= NAND =============')
a= True
b = True
c = not (a and b)
print(a,"NAND",b,"menjadi",c)

a= True
b = False
c = not (a and b)
print(a,"NAND",b,"menjadi",c)

a= False
b = True
c = not (a and b)
print(a,"NAND",b,"menjadi",c)

a= False
b = False
c = not (a and b)
print(a,"NAND",b,"menjadi",c)

print ('============= NOR =============')
a= True
b = True
c = not (a or b)
print(a,"NOR",b,"menjadi",c)

a= True
b = False
c = not (a or b)
print(a,"NOR",b,"menjadi",c)

a= False
b = True
c = not (a or b)
print(a,"NOR",b,"menjadi",c)

a= False
b = False
c = not (a or b)
print(a,"NOR",b,"menjadi",c)

print ('============= NXOR =============')
a= True
b = True
c = not (a ^ b)
print(a,"NXOR",b,"menjadi",c)

a= True
b = False
c = not (a ^ b)
print(a,"^",b,"menjadi",c)

a= False
b = True
c = not (a ^ b)
print(a,"NXOR",b,"menjadi",c)

a= False
b = False
c = not (a ^ b)
print(a,"NXOR",b,"menjadi",c)

#OPERATOR IDENTITAS
print (' ============== IS ')
a =5
b =5
print ('Nilai a =',a ,'Identitas =',hex (id( a ) ) )
print ('Nilai b =',b ,'Identitas =',hex (id( b ) ) )
hasil = a is b
print ('a is b = ', hasil )

a=5
b=6
print ('Nilai a =',a ,'Identitas =',hex (id( a ) ) )
print ('Nilai b =',b ,'Identitas =',hex (id( b ) ) )
hasil = a is b
print ('a is b = ', hasil )

print (' ============== IS NOT ')
a =5
b =5
print ('Nilai a =',a ,'Identitas =',hex (id( a ) ) )
print ('Nilai b =',b ,'Identitas =',hex (id( b ) ) )
hasil = a is not b
print ('a is not b = ', hasil )

a =5
b =6
print ('Nilai a =',a ,'Identitas =',hex (id( a ) ) )
print ('Nilai b =',b ,'Identitas =',hex (id( b ) ) )
hasil = a is not b
print ('a is not b = ', hasil )

#OPERATOR MEMBERSHIP

print (" ======================= IN ")

nama_lengkap = "Bacharuddin Jusuf Habibie"
test ="a"
cek = test in nama_lengkap
print (test +"terdapat di" +nama_lengkap+" adalah"+ str(cek))

test ="rud"
cek = test in nama_lengkap
print (test+" terdapat di "+ nama_lengkap +" adalah "+ str(cek))

test = "bac"
cek = test in nama_lengkap
print (test +" terdapat di "+ nama_lengkap +" adalah "+ str(cek))

print (" ======================= NOT IN ")
nama_lengkap = "Bacharuddin Jusuf Habibie"
test = "a"
cek = test not in nama_lengkap
print (test +" tidak terdapat di "+ nama_lengkap +" adalah "+str (cek))

test = "rud"
cek = test not in nama_lengkap
print (test +" tidak terdapat di "+ nama_lengkap +" adalah "+str (cek))

test = "bac"
cek = test not in nama_lengkap
print (test +"tidak terdapat di "+ nama_lengkap +" adalah "+str (cek))

#TUGAS

print ("============= IN =============")
nama = "Nurasyah"
test  = " rs "
cek   = test in nama
print(test,"ada di" ,nama," adalah=",str (cek))
test  = " sr "
cek    = test in nama
print(test,"ada di",nama ," adalah=",str (cek))

test3="a"
test4="i"
test5="u"
test6="e"
test7="o"
cek = test3 in nama
print(test3,"ada di",nama ," adalah=",cek)
cek = test4 in nama
print(test4,"ada di",nama ," adalah=",cek)
cek = test5 in nama
print(test5,"ada di",nama ," adalah=",cek)
cek = test6 in nama
print(test6,"ada di",nama ," adalah=",cek)
cek = test7 in nama
print(test7,"ada di",nama ," adalah=",cek)

print ("============= NOT IN =============")
nama = "Nurasyah"
test  = " ah "
cek   = test not in nama
print(test,"tidak di" ,nama," adalah=",cek)
test  = " ha "
cek    = test not in nama
print(test,"tidak di",nama ," adalah=",cek)

test3="a"
test4="i"
test5="u"
test6="e"
test7="o"
cek    = test3 not in nama
print(test3,"tidak di",nama ," adalah=",cek)
cek    = test4 not in nama
print(test4,"tidak di",nama ," adalah=",cek)
cek    = test5 not in nama
print(test5,"tidak di",nama ," adalah=",cek)
cek    = test6 not in nama
print(test6,"tidak di",nama ," adalah=",cek)
cek    = test7 not in nama
print(test7,"tidak di",nama ," adalah=",cek)


#OPERATOR BITWISE

a=13
a +=60
b=12
b+=90

print (" ============================= OR ")
print ("Nilai",a ,"dalam biner =",format(a,"08b"))
print ("Nilai",b ,"dalam biner =",format(b,"08b"))
print ("----------------------------(|)")

hasil=a|b
print ("Nilai",a,"|",b,"dalam biner =",format (hasil,"08b"))

print (" ============================= AND ")
print ("Nilai",a ,"dalam biner =",format(a,"08b"))
print ("Nilai",b ,"dalam biner =",format(b,"08b"))
print ("----------------------------(&)")

hasil=a&b
print ("Nilai",a,"&",b,"dalam biner =",format (hasil,"08b"))

print (" ============================= XOR ")
print ("Nilai",a ,"dalam biner =",format(a,"08b"))
print ("Nilai",b ,"dalam biner =",format(b,"08b"))
print ("----------------------------(^)")

hasil=a^b
print ("Nilai",a,"^",b,"dalam biner =",format (hasil,"08b"))

print (" ============================= NOT ")
print ("Nilai",a ,"dalam biner =",format(a,"08b"))
print ("----------------------------(~a)")

hasil= ~a
print ("Nilai ~",a,"dalam biner =" ,format (hasil,"08b"))

print ("Nilai",b ,"dalam biner =",format(a,"08b"))
print ("----------------------------(~b)")

hasil= ~b
print ("Nilai ~",b,"dalam biner =" ,format (hasil,"08b"))

print (" ============================= >> ")
print ("Nilai",a ,"dalam biner =",format(a,"08b"))
print ("----------------------------(>>2)")

hasil= a >>2
print ("Nilai ~",a,">>2 dalam biner =" ,format (hasil,"08b"))

print ("Nilai",b ,"dalam biner =",format(b,"08b"))
print ("----------------------------(>>2)")

hasil= b >>2
print ("Nilai ~",b,">>2 dalam biner =" ,format (hasil,"08b"))


print (" ============================= << ")
print ("Nilai",a ,"dalam biner =",format(a,"08b"))
print ("----------------------------(>>2)")

hasil= a <<2
print ("Nilai ~",a,"<<2 dalam biner =" ,format (hasil,"08b"))

print ("Nilai",b ,"dalam biner =",format(b,"08b"))
print ("----------------------------(<<2)")

hasil= b <<2
print ("Nilai ~",b,"<<2 dalam biner =" ,format (hasil,"08b"))

#TUGAS

a=24
a +=40
b=66
b+=60

print ("=============================NOT AND")
print ("Nilai",a ,"dalam biner =",format(a,"08b"))
print ("Nilai",b ,"dalam biner =",format(b,"08b"))
print ("----------------------------(&)")
hasil=a&b
print ("Nilai",a,"&",b,"dalam biner =",format (hasil,"08b"))

print ("=============================NOT OR")
print ("Nilai",a,"dalam biner =",format(a,"08b"))
print ("Nilai",b,"dalam biner =",format(b,"08b"))
print ("----------------------------(|)")
hasil=a|b
print ("Nilai",a,"|",b,"dalam biner =",format (hasil,"08b"))

print (" =============================NOT XOR ")
print ("Nilai",a ,"dalam biner =",format(a,"08b"))
print ("Nilai",b ,"dalam biner =",format(b,"08b"))
print ("----------------------------(^)")
hasil=a^b
print ("Nilai",a,"^",b,"dalam biner =",format (hasil,"08b"))

print (" ============================= NOT XOR")
print ("Nilai",a ,"dalam biner =",format(a,"08b"))
print ("----------------------------(~a)")
hasil= ~a
print ("Nilai ~",a,"dalam biner =" ,format (hasil,"08b"))

print ("Nilai",b,"dalam biner =",format(a,"08b"))
print ("----------------------------(~b)")
hasil= ~b
print ("Nilai ~",b,"dalam biner =" ,format (hasil,"08b"))

print (" =============================NOT (>>2) ")
print ("Nilai",a ,"dalam biner =",format(a,"08b"))
print ("----------------------------(>>2)")
hasil= a >>2
print ("Nilai ~",a,">>2 dalam biner =" ,format (hasil,"08b"))

print ("Nilai",b ,"dalam biner =",format(b,"08b"))
print ("----------------------------(>>2)")
hasil= b >>2
print ("Nilai ~",b,">>2 dalam biner =" ,format (hasil,"08b"))

print (" =============================NOT (<<2) ")
print ("Nilai",a ,"dalam biner =",format(a,"08b"))
print ("----------------------------(>>2)")
hasil= a <<2
print ("Nilai ~",a,"<<2 dalam biner =" ,format (hasil,"08b"))

print ("Nilai",b ,"dalam biner =",format(b,"08b"))
print ("----------------------------(<<2)")
hasil= b <<2
print ("Nilai ~",b,"<<2 dalam biner =" ,format (hasil,"08b"))






