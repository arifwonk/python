# latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# +++++3-------10+++++

InputUser = float(input('masukan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n:'))

# +++++3---------
# memerikas angka kurang dari 3
isKurangDari =  (InputUser < 3 )
print("Kurang dari 3=",isKurangDari)

# -------10++++++
# memeriksa angka lebih dari 10
isLebihDari = (InputUser > 10 )
print("Lebih dari 10",isLebihDari)

isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan adalah=", isCorrect)

# ------3+++++10------
# kasus irisan 
print("\n", 10*"=","\n")
InputUser = float(input('masukan angka yang bernilai\nLebih besar dari 3\ndan\nkurang dari 10\n:'))


# -----3+++++
isLebihDari = InputUser > 3
print("Lebih dari 3 =", isLebihDari)

# ++++10-----
isKurangDari = InputUser < 10
print("Kurang dari 10=",isKurangDari)

# ------3+++++10------
isCorrect = isLebihDari and isKurangDari
print("angka yang anda masukan adalah=", isCorrect)

# PR
# 1. -----0++++5----8++++11---- (a and b or c and d)
# 2. +++++0----5++++8----11++++ (a or b and c or d)

# Jawab no 1
print("\n", 10*"=","\n")
InputUser = float(input('masukan angka yang bernilai\nLebih dari 0\nkurang dari 5\natau\nLebih dari 8\nKurang dari 11\n:'))

# ----0++++
# memerikas angka Lebih dari 0
a =  (InputUser > 0 )
print("Lebih dari 0 =",a)

# ++++5-----
# memeriksa angka Kurang dari 5
b = (InputUser < 5 )
print("Kurang dari 5 =",b)

# ----8++++
# memerikas angka Lebih dari 8
c =  (InputUser > 8 )
print("Lebih dari 8 =",c)

# ++++11-----
# memeriksa angka Kurang dari 11
d = (InputUser < 11 )
print("Kurang dari 11 =",d)

# -----0++++5----8++++11---- (AND)
isCorrect = a and b or c and d
print("angka yang anda masukan adalah=", isCorrect)


# Jawab no 2
print("\n", 10*"=","\n")
InputUser = float(input('masukan angka yang bernilai\nkurang dari 0\nlebih besar dari 5\ndan\nkurang dari 8\nLebih besar dari 11\n:'))

# +++++0---------
# memerikas angka kurang dari 0
a =  (InputUser < 0 )
print("Kurang dari 0 =",a)

# -------5++++++
# memeriksa angka lebih dari 5
b = (InputUser > 5 )
print("Lebih dari 5 =",b)

# +++++8---------
# memerikas angka kurang dari 8
c =  (InputUser < 8 )
print("Kurang dari 8 =",c)

# -------11++++++
# memeriksa angka lebih dari 11
d = (InputUser > 11 )
print("Lebih dari 11 =",d)

#  +++++0----5++++8----11++++ (a or b and c or d)
isCorrect = a or b and c or d

print("angka yang anda masukan adalah=", isCorrect)





