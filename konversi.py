print("---Program konversi bilangan")
print("1 -> desimal ke binary")
print("2 -> binary ke desimal")
print("3 -> exit program")
print("\n")
def nomer():
    while True:
        nomor = int(input("pilihlah menu yang diinginkan :"))
        if nomor == 1:
            #desimal ke binary
            binary = int(input("Masukkan bilangan :"))
            if binary == 0:
                print (0)
            else:
                bitstring = ""
                while binary > 0: 
                    sisa = binary % 2
                    binary = binary //2 
                    bitstring = str(sisa) + bitstring
            print("Angka biner adalah :", bitstring)
        elif nomor == 2:
            #binary ke desimal 
            bits = str(input("Masukkan bit :"))
            nomorbit = 0
            eksponen = len(bits) - 1
            for digit in bits:
                nomorbit = nomorbit + int(digit)*2**eksponen
                eksponen = eksponen - 1
            print("Nilai desimal dari nomor tersebut adalah", nomorbit)
        else:
            print("Terima kasih sudah memakai")
            break
nomer()
input()
