# Latihan

# Kalkulator sederhana

print(53*"=")
print("Kalkulator sederhana")
print(53*"=" + "\n")

angka_1 = float(input("Masukan Angka 1\t\t="))
operator = input("Operator(+, -, x, /)\t=")
angka_2 = float(input("Masukan Angka 2\t\t="))

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah\t\t= {hasil}\n")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah\t\t= {hasil}")
elif operator == "*" or operator =="x":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah\t\t= {hasil}\n")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah\t\t= {hasil}\n")
else:
    print(f"Unknown operator...!!vMasukin yang bener Dongs..!!!\n")
print(12*"=" + "Ini adalah akhir dari program." + 12*"=")


