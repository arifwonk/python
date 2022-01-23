#  Operasi komparasi

# setiap hasil dari hasil komparasi adalah Boolean

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# Lebih besar dari >
print('============ Lebih besar dari (>)')
hasil = a > 3
print(a,'>',3,'=', hasil)
hasil = b > 3
print(b,'>',3,'=', hasil)
hasil = b > 2
print(b,'>',2,'=', hasil)

# kurang dari <
print('============ kurang dari (<)')
hasil = a < 3
print(a,'<',3,'=', hasil)
hasil = b < 3
print(b,'<',3,'=', hasil)
hasil = b < 2
print(b,'<',2,'=', hasil)

#  Lebih dari sama dengan >=
print('============ Lebih dari sama dengan(>=)')
hasil = a >= 3
print(a,'>=',3,'=', hasil)
hasil = b >= 3
print(b,'>=',3,'=', hasil)
hasil = b >= 2
print(b,'>=',2,'=', hasil)

#  kurang dari sama dengan <=
print('============ kurang dari sama dengan(<=)')
hasil = a <= 3
print(a,'<=',3,'=', hasil)
hasil = b <= 3
print(b,'<=',3,'=', hasil)
hasil = b <= 2
print(b,'<=',2,'=', hasil)

#  Sama dengan ==
print('============ sama dengan (==)')
hasil = a == 4
print(a,'==',4,'=', hasil)
hasil = b == 4
print(b,'==',4,'=', hasil)

#  Sama dengan !=
print('============ tidak sama dengan (!=)')
hasil = a != 4
print(a,'!=',4,'=', hasil)
hasil = b != 4
print(b,'!=',4,'=', hasil)

# 'is' Sebagai komparasi object
print('============ Object identity  (is)')
x = 5 # ini adalah assigment membuat object
y = 5 
print('Nilai x =',x,'id=', hex(id(x)))
print('Nilai y =',y,'id=', hex(id(y)))
hasil = x is y
print('x is y =', hasil)

print('============')
x = 5 # ini adalah assigment membuat object
y = 6 
print('Nilai x =',x,'id=', hex(id(x)))
print('Nilai y =',y,'id=', hex(id(y)))
hasil = x is y
print('x is y =', hasil)

# 'is not' Sebagai komparasi object
print('============ Object identity  (is not)')
x = 5 # ini adalah assigment membuat object
y = 5 
print('Nilai x =',x,'id=', hex(id(x)))
print('Nilai y =',y,'id=', hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)

print('============')
x = 5 # ini adalah assigment membuat object
y = 6 
print('Nilai x =',x,'id=', hex(id(x)))
print('Nilai y =',y,'id=', hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)



