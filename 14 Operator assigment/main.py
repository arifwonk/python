# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

a = 5 # adalah assigment
print("Nilai a =", a)

a += 1 # artinya adalah  a = a + 1
print("Nilai a += 1, nilai a menjadi", a)

a -= 2 # artinya adalah  a = a - 2
print("Nilai a -= 2, nilai a menjadi", a)

a *= 5 # artinya adalah  a = a * 5
print("Nilai a *= 5, nilai a menjadi", a)

a /= 2 # artinya adalah  a = a / 2
print("Nilai a /= 2, nilai a menjadi", a)

# modulus dan floor division
b = 10
print("\nNilai b =", b)

b %= 3
print("Nilai b %= 3, Nilai b menjadi", b)

b = 10
print("Nilai b =", b)

b //= 3
print("Nilai b //= 3, Nilai b menjadi", b)

# pangkat atau eksponen
a = 5
print("\nNilai a =", a)

a **= 3
print("Nilai a **= 3, Nilai a menjadi", a)

# Operasi Bitwise
# OR simbol |
print("\n", 10*"=","OR")
c = True
print("Nilai c =", c)
c |= False
print("Nilai c| = False, Nilai c menjadi", c)
c = False
print("Nilai c =", c)
c |= False
print("Nilai c| = False, Nilai c menjadi", c)

# AND Simbol &
print("\n", 10*"=","AND")
c = True
print("Nilai c =", c)
c &= False
print("Nilai c& = False, Nilai c menjadi", c)
c = True
print("Nilai c =", c)
c &= True
print("Nilai c& = True, Nilai c menjadi", c)

# XOR Simbol (^)
print("\n", 10*"=","XOR")
c = True
print("Nilai c =", c)
c ^= False
print("Nilai c^ = False, Nilai c menjadi", c)
c = True
print("Nilai c =", c)
c ^= True
print("Nilai c^ = True, Nilai c menjadi", c)

#  geser geser / shifting
d = 0b0100
print("\nNilai d =", format(d, '04b'))
d >>= 2
print("Nilai d>> = 2, Nilai d menjadi",format(d, '04b'))
d <<= 1
print("Nilai d<< = 1, Nilai d menjadi",format(d, '04b'))
