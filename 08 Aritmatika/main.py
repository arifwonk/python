#  Operasi aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b
print (a,'+',b,'=',hasil)

# operasi tambah -
hasil = a - b
print (a,'-',b,'=',hasil)

# operasi tambah *
hasil = a * b
print (a,'*',b,'=',hasil)

# operasi tambah /
hasil = a / b
print (a,'/',b,'=',hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print (a,'**',b,'=',hasil)

# operasi modulus (sisa pembagian) %
hasil = a % b
print (a,'%',b,'=',hasil)

# operasi floor division (pembulatan pembagian kebawah) //
hasil = a // b
print (a,'//',b,'=',hasil)

# prioritas operasi
'''
    1. ()
    2. eksponen (pangkat) **
    3. perkalian dan teman-teman * / % //
    4. Pertambahan, pengurangan + -
'''

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print (x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z
print (x,'+',y,'*',z,'=',hasil)

# () kurung akan di eksekusi pertama
hasil = (x + y) * z
print ('(',x,'+',y,') *',z,'=',hasil)
