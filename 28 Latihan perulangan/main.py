# Latihan perulangan membuat segitiga

sisi = 9

# 1. menggunakan For

# dummy variabel
print("Awal dari For")
count = 1

for i in range(sisi):
    print("*"*count)
    count += 1

print("Akhir dari For")

# 2. Menggunakan While
print("Awal dari While")

count = 1

while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print("Akhir dari While")

# 3. Menggunakan While print hanya ganjil saja
print("Awal dari While")

count = 1

while True:
    if (count % 2):
        # print jika ganjil
        print("*"*count)
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break

print("Akhir dari While")

# 4. Menggunakan While print hanya ganjil saja
print("Awal dari While Segitiga sama kaki")

count = 1
spasi = int(sisi/2)

while True:
    if (count % 2):
        # print jika ganjil
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    
    # akan break jika count melebihi sisi
    if count > sisi:
        break

print("Akhir dari While Segitiga sama kaki")


