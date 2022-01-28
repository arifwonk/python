# Operator dalam bentuk method 

# # merubah case dari string

# Merubah semuanya ke Uppercase
salam ="cuy"
print("normal = " + salam)
salam = salam.upper()
print("Upper = " + salam)

# Merubah ke lower case 
alay = "aKu KeCE ABiiieeEEZZZ"
print("normal = " + alay)
alay = alay.lower()
print("Lower = " + alay)

# pengecekan dengan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya boolean
print(salam + " is Lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya boolean
print(salam + " is Upper = " + str(apakah_upper))

salam = "Kuy".islower()
print( "apakah 'Kuy' Lower = " + str (salam))

# isalpha () <--- untuk mengecek semuanya huruf
# isalnum () <--- Huruf dan angka
# isdecimal () <--- angka saja
# isspace () <--- spasi, tab, new line \n
# istitle () <--- semua kata diawali dengan huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul + " is Title = " + str(cek_judul))

## ngecek komponen startswith() endswith() <--- Josss
cek_start = "Seo Hyun Oppa".startswith("Seo")
print("start = " + str(cek_start))

cek_end = "Hanjieen Oppak".endswith("Oppak")
print("end = " + str(cek_end))

# penggabungan komponen join () dan split()
pisah =['aku','sayang','ibu']
gabung = ','.join(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = ' ehm '.join(pisah)
print(gabung)

gabung = "akuehmsayangehmibu"
print(gabung.split('ehm'))

# alokasi karakter rjust(), ljust(), center()
print(5*"=", "data", "="*5, "Ribet")

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10)
print("'"+tengah+"'")

tengah = "tengah".center(20,":")
print("'"+tengah+"'")

# kebelikanya --> strip
tengah = "tengah".strip(":") # menghilangkan tanda :
print("'"+tengah+"'")

kanan = "kanan".strip() #menghilangkan tanda spasi
print("'"+kanan+"'")