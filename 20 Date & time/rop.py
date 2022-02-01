a = 12381
b = 365
hasil = (a % b) //30 
print(f"hasil dari (12381 hari di % 365 hari)//30 :{hasil} Bulan\n")

a = 12381
b = 365
hasil = (a % b) %30 
print(f"hasil dari (12381 hari di % 365 hari)//30 :{hasil} Hari\n")

hasil = a // b

print(hasil)