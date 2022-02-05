#  continue pass dan break
# pas dia berfungsi sebagi dummys, tidka di eksekusi

# angka = 0

# while angka < 5 :
#     angka += 1
#     if angka == 3:
#         pass        #ini tidak akan di eksekusi

#     print(angka)

# Continue 

angka = 0
print(f"angka sekarang ->  {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") #aksi 1
    
    if angka == 3:
        print("Nice..!")
        continue        # akan membuat Loop meloncat ke step selanjutnya

    print("Josss gandosSSS") #aksi 2

print("Finish")


