# a = 10 , a adalah variabel dengan nilai 10
# macam-macam tipe data:  integer, float, string, boolean

# tipe data integer : angka satuan tidak ada koma
data_integer= 100
print("data :", data_integer, "bertipe :", type(data_integer))

# tipe data float : tipe data angka dengan koma
data_float= 1.5
print("data :", data_float)
print("-bertipe", type(data_float))

# tipe data string : kumpulan karakter (string)
data_string= "rafka"
print("data :", data_string)
print("-bertipe", type(data_string))

# tipe data boolean : Biner True/False
data_boolean= True
print("data :", data_boolean)
print("-bertipe", type(data_boolean))

# tipe data khusus

# bilangan kompleks
data_complex= complex(5,10)
print("data :", data_complex)
print("-bertipe", type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double

data_c_double= c_double(10.7)
print("data :", data_c_double)
print("-bertipe", type(data_c_double))