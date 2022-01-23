# mengambil input data dari user

# data yang dimasukan pasti string
data = input("Masukan nama")
print("data =",data,", type =",type(data))

# jika ingin mengambil int, maka :
angka = int(input("masukan angka :"))
# angka = float(input("masukan angka :"))

print("data =",angka,", type =",type(angka))

#  bagaimana dengan boolean
biner = bool(int(input("Masukan angka: ")))
print("data =",biner,", type =",type(biner))
