# latihan2
    # percabangan if
inp = input("Masukkan suatu input: ")
if len(inp) != 3:
    print("Panjang string ", len(inp), "tidak sama dengan 3 ")
else:
    print("Panjang input sesuai yang diinginkan")

    # percabangan elif
    nilai = int(input("Masukkan nilai: "))
if nilai >= 95:
    print("Nilai huruf: A")
elif nilai > 80:
    print("Nilai huruf: B")
elif nilai > 60:
    print("Nilai huruf: C")
else:
    print("Nilai huruf: D")
