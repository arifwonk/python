#  LIST

# Kumpulan data numbers/angka
data_angka = [1,2,3,4,5,6,7,8,9,10]
print(data_angka)

# kumpulan data string
data_string = ["adi", "arif", "iin"]
print(data_string)

# kumpulan data boolean
data_boolean = [True, False, False, True]
print(data_boolean)

# kumpulan data campuran
data_campuran = [1,"adi", 2, "arif", 3,"iin","Ucup", True,"Odah", False]
print(data_campuran, "\n")

# cara alternatif membuat List
print(15*"=","Membuat List Alternatif")
data_range = range(0,10)
print(data_range) 
data_list = list(data_range)
print(data_list)

data_range = range(0,10,2) # Range  (start, stop, step)
data_list = list(data_range)
print(data_list)

# membuat List dengan for loop, List comprehension
print("\n",15*"=","List pakai for loop")
list_pake_for = [i for i in range(0,10)]
print(list_pake_for)

list_pake_for = [i**2 for i in range(0,10)]
print(list_pake_for)

# membuat list pake for dan pakai if
print("\n",15*"=","List pakai for dan pakai if")
list_pake_for_if = [i for i in range(0,10) if i !=4 and i !=6]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 ==0]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 !=0]
print(list_pake_for_if)

list_pake_for_if = [i**2 for i in range(0,10) if i%2 !=0]
print(list_pake_for_if)




