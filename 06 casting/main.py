# belajar casting
# merubah dari satu tipe ke tipe lain
# tipe data = int, float, string, boolean

print("====INTEGER====")
# INTEGER
data_int = 5;
print("data =", data_int, ", Type =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_boolean = bool(data_int) #akan false jika nilai int = 0
print("data =", data_float, ", Type =", type(data_float))
print("data =", data_str, ", Type =", type(data_str))
print("data =", data_boolean, ", Type =", type(data_boolean))

print("====FLOAT====")
# float
data_float = 7.8;
print("data =", data_float, ", Type =", type(data_float))

data_int = int(data_float) # data akan dibulatkan kebawah
data_str = str(data_float)
data_boolean = bool(data_float) # akan false jika nilai voolean = 0
print("data =", data_int, ", Type =", type(data_int))
print("data =", data_str, ", Type =", type(data_str))
print("data =", data_boolean, ", Type =", type(data_boolean))

print("====Boolean====")
# Boolean
data_boolean = False;
print("data =", data_boolean, ", Type =", type(data_boolean))

data_int = int(data_boolean) 
data_str = str(data_boolean)
data_float = float(data_boolean) 
print("data =", data_int, ", Type =", type(data_int))
print("data =", data_str, ", Type =", type(data_str))
print("data =", data_float, ", Type =", type(data_float))

print("====STRING====")
# STRING
data_str = "10";
print("data =", data_str, ", Type =", type(data_str))

# data_int = int(data_str) # string harus angka 
# data_float = float(data_str) # string harus angka 
data_boolean = bool(data_str) # flase jika string kosong
# print("data =", data_int, ", Type =", type(data_int))
# print("data =", data_float, ", Type =", type(data_float))
print("data =", data_boolean, ", Type =", type(data_boolean))