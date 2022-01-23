# Operasi Logika atau Boolean

# not, or, and, xor

# not
print('====NOT====')
a = False
c = not a

print('data =',a)
print('--------------NOT')
print('data =',c)

# OR Jika salah satu True, maka hasilnya adalah True (sama seperti ditambah)
print('====OR====')
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,' =',c)
a = True
b = False
c = a or b
print(a,'OR',b,' =',c)
a = True
b = True
c = a or b
print(a,'OR',b,'  =',c)

# AND Jika dua buah nilai True maka hasil true (sama seperti dikali)
print('====AND====')
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,' =',c)
a = True
b = False
c = a and b
print(a,'AND',b,' =',c)
a = True
b = True
c = a and b
print(a,'AND',b,'  =',c)

# XOR (akan true jika salah satu true, sisanya harus false)
print('====XOR====')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c)
a = True
b = False
c = a ^ b
print(a,'XOR',b,' =',c)
a = True
b = True
c = a ^ b
print(a,'XOR',b,'  =',c)