# Operasi

# Index   0(-3)        1(-2)        2(-1)
data = ["Soleh", "Budin", "Dadang"]

# Mengambil data dari List
data_0 = data[0]
print(f"data pertama (index 0) = {data_0} ")

data_terakhir = data[-1]
print(f"data Terakhir adalah = {data_terakhir} ")

# Mengambil info jumlah data dalam List
panjang_data = len(data)
print(f"Panjang data = {panjang_data} ")

# manipulasi data List

# menambahkan Item pada List Sesuai posisi
print(f"data sebelum ditambah =\n{data}")

data.insert(1, "Unang")
print(f"data sesudah ditambah =\n{data}")

# menambahkan data di akhir list
data.append("Jacky")
print(f"data ditambah diakhir =\n{data}")

data_baru = ["Udin", "Ucep", "Umar"]
data.extend(data_baru)
print(f"data Gabungan =\n{data}")

# Merubah data
# ubah data 2 menjadi Jojon
data [4] = "Jojon"
print(f"Ubah data Index 4 =\n{data}")

# Meremove data
data.remove("Ucep")
print(f"Hapus data Ucep =\n{data}")

# Meremove data paling belakang
data_akhir = data.pop()
print(f"Hapus data akhir =\n{data}")

print(data_akhir)