import os

os.system("clear")

a = True

while a:
    pilih = input("apakah ingin melanjutkan? [y/n]")
    if pilih == "y":
        print("terimah kasih:")
        a = False
    elif pilih == "n":
        print("sampai jumpa lagi :)")
        a = False
    else:
        print("jangan aneh deh   :(")
