# Break

#  Break 1
angka = 0

while angka < 5:         
    angka += 1
    print(f"angka sekarang = {angka}")

    if angka == 3:
        print("Nice...!")
        break

    print("Wassupp!")

print("Cukup Finish!\n")


# Break 2
data_int = int(input("Hitung sampai = "))

angka = 0

while True:         #bisa pakai (while data_int:)
    angka += 1
    print(f"Count = {angka}")

    if angka == data_int:
        print("Nice...!")
        break

    print("Wassupp!")

print("Cukup Finish!")
