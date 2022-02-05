# Perulangan (loop)

# for kondisi:
#     aksi

# ini dengan List
from ast import Try


angka_list = [2,4,6,8,10] #List
print(angka_list)

for i in angka_list:
    print(f"i sekarang -> {i}")

print("Akhir dari program 1\n")

# ini dengan range
angka_range = range(5) # Range

for i in angka_range:
    print(f"i sekarang -> {i}")

print("Akhir dari program 2\n")

angka_range = range(1, 5)

for i in angka_range:
    print(f"i sekarang -> {i}")
    # print("saya ganteng")

print("Akhir dari program 3\n")

# menggunakan string
data_str = "Rival Ganteng abiiezz" #string

for huruf in data_str:
    print(huruf)

print("Akhir dari program 4\n")
