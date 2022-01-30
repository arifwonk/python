# Width & Multi Lines 

# Data

nama = "arif wonk"
umur = 17
tinggi = 170.1
no_sepatu = 42

# String standard
data_string = f"nama = {nama}, umur = {umur}, tinggi = {tinggi}, nomer sepatu = {no_sepatu}"
print(10*"="+"String Standard"+10*"=")
print(data_string)

# String Multiline (dengan menggunakan Enter, newline, \n)
data_string = f"nama = {nama} \numur = {umur} \ntinggi = {tinggi} \nnomer sepatu = {no_sepatu}"
print("\n"+10*"="+"String Multiline"+10*"=")
print(data_string)

# String Multiline (kutip triplets)
data_string = f"""nama  = {nama}
umur   = {umur}
tinggi = {tinggi}
nomer sepatu = {no_sepatu}
"""
print("\n"+10*"="+"String Multiline Kutip Triplets"+10*"=")
print(data_string)

# Mengatur Lebar
nama = "arif"
data_string = f"""
nama            = {nama:>5}
umur            = {umur:>5}
tinggi          = {tinggi:>5}
nomer sepatu    = {no_sepatu:>10}
"""
print("\n"+10*"="+"String Mengatur Lebar"+10*"=")
print(data_string)
