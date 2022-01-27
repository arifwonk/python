# operasi dan manipulasi string se

# 1. menyambung string (concatenate)
nama_pertama = "mohamad"
nama_tengah = "arif"
nama_terakhir = "soleh"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_terakhir
print(nama_lengkap)

# 2. Menghitung panjang dari string

panjang = len(nama_lengkap)
print("panjang dari "+ nama_lengkap +" = " + str(panjang))

# 3. Operator untuk String

# menegecek aapakah ada komponen char atau string di string
d="d"
status = d in nama_lengkap
print(d + " ada di string " + nama_lengkap + " = " + str(status))

D="D"
status = D in nama_lengkap
print(D + " ada di string " + nama_lengkap + " = " + str(status))

D="D"
status = D not in nama_lengkap
print(D + " Tidak ada di string " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(15*"wk")

# indexing
print("Index ke 0 : " + nama_lengkap[0])
print("Index ke 7 : " + nama_lengkap[7])
print("Index ke 8 : " + nama_lengkap[8])
print("Index ke (-1) : " + nama_lengkap[-1])
print("Index ke (-2) : " + nama_lengkap[-2])
print("Index ke (0,6) : " + nama_lengkap[0:7])
print("Index ke (6,10) : " + nama_lengkap[6:11])
print("Index ke (0,2,4,6,8,10) : " + nama_lengkap[0:11:2])

# item paling kecil
print("item paling kecil :" + min(nama_lengkap))
# item paling besar
print("item paling besar :" + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("Char untuk ASCII 117 adalah " + chr(data))

# 4. Operator dalam bentuk method

data =" otong surotong pararotong"
jumlah = data.count("o")
print("Jumlah Huruf 'O' pada " + data + " = " + str(jumlah))