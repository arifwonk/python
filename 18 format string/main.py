# Format string

# Contoh Generic

# stirng
nama = "ucup"
format_str = f"Hello {nama}"
print(format_str)

Boolean = True
format_str = f"Boolean = {Boolean}"
print(format_str) 

# Versi concatenate
a = 2004.4
f = "angka =" + str(a)  
print(f)

# Angka
angka = 2005.5
format_str = f"Angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"Bilangan bulat= {angka:d}"
print(format_str)

# Bilangan Ribuan dengan ordo ribuan
angka = 2000000
format_str = f"Ribuan = {angka:,}"
print(format_str)

# Bilangan desimal
angka = 2005.4321
format_str = f"Desimal = {angka:.2f}"
print(format_str)

# Menampilkan Leading Zero
angka = 2005.5432
format_str = f"Desimal = {angka:09.2f}"
print(format_str)

# Menampilkan tanda + atau -
angka_minus = -10
angka_plus0 = 10
angka_plus = 10.5433
format_minus = f"Minus = {angka_minus:+d}"
format_plus0 = f"Plus = {angka_plus0:+d}"
format_plus = f"Plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus0)
print(format_plus)

# Memformat persen %
persen = 0.045
format_persen = f"Persen = {persen:.1%} "
print(format_persen)

# melakukan Operasi aritmatika didalm Place holder {}
harga = 20000
jumlah = 5

format_string = f"Total = Rp. {harga*jumlah:,}"
print(format_string)

# Format angka Lain (binary, octal, hexadecimal)
angka = 255
f_binary = f"Binary = {bin(angka)}"
f_octal = f"Octal = {oct(angka)}"
f_hex = f"Hexadecimal = {hex(angka)}"

print(f_binary)
print(f_octal)
print(f_hex)