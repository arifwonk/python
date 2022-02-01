# Date & time Latihan

import datetime as dt

# # print hari dan jam
# hari_ini_jam = dt.datetime.today()
# print(hari_ini_jam)

# # print hari ini
# hari_ini = dt.date.today()
# print(hari_ini)
# print(f"Hari ini adalah hari: {hari_ini:%A}")
# ulang_tahun = dt.date(2022,3,10)
# print(f"Ulang Tahun: {ulang_tahun}")

print("Masukan Tanggal, \nBulan, dan tahun Lahir anda:\n")
tanggal= int(input("Masukan Tanggal\t:"))
bulan= int(input("Masukan Bulan\t:"))
tahun= int(input("Masukan Tahun\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal Lahir anda adalah: {tanggal_lahir}")


hari_ini = dt.date.today()
print(f"Hari ini Tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f"Umur anda adalah: {umur_tahun} Tahun, {umur_bulan_sisa} Bulan")
print(f"Harinya adalah: {tanggal_lahir:%A}\n")


print("\n"+15*"="+"Logic"+"="*15)
print(umur_hari)
a = 12381
b = 365
hasil = (a % b) //30 
print(f"hasil dari (12381 hari di % 365 hari)//30 :{hasil} Bulan\n")