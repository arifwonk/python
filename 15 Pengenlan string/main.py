data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string
'''
    1. dengan menggunakan single Quote '....'
    2. dengan menggunakan Double Quote "...."

'''

data  = 'menggunakan single quote '
print(data)

data  = "menggunakan double quote "
print(data)

print('"Halo, apa kabar Cuy?"')
print("ini adalah hari jum'at")

# 2. Menggunalan tanda \

# membuat tanda  ' menjadi string
print('ayo shlolat jum\'at')
print('g\'day, isn\'t it?')

# backslah
print("C:\\user\\rafka")

# Tab 
print("ucup\t\t semakin jauh")

# backspace
print("ucup \botong, jadi deketan")

# new Line
print("baris pertama.\nbaris kedua.") # LF -> Line feed -> Unix, Linux
print("baris pertama.\rbaris kedua.") # CR -> carriage rturn -> Commodore, acorn, Lisp
print("baris pertama.\r\nbaris kedua.") # CRLF -> Line fedd carriage return -> dipakai oleh windows

# 3. String literal atau raw

# hati hati
print('C:\new folder') # ini akan salah pathnya

# menggunkan raw string
print(r'C:\new folder')

# multi line Literal string
print("""
    nama  : ucup
    kelas : 3 SD
""")

# multi line literal string dan raw string
print(r"""
    nama  : ucup
    kelas : 3 SD\new normal
    website : wwww.ucup.com/newBorn
""")

