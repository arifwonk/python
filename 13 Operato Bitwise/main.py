# Operator bitwise = operasi masing masing bit
# operator bitwi, operasi biner, binary

a = 9
b = 5

# Bitwise OR (|)
c = a | b
print('\n======OR======')
print('nilai :', a,'binary :',format(a,'08b'))
print('nilai :', b,'binary :',format(b,'08b'))
print('------------ ----------------(|)')
print('nilai :', c,'binary:',format(c,'08b'))

# Bitwise AND (&)
c = a & b
print('\n======AND======')
print('nilai :', a,'binary :',format(a,'08b'))
print('nilai :', b,'binary :',format(b,'08b'))
print('------------ ----------------(&)')
print('nilai :', c,'binary :',format(c,'08b'))

# Bitwise XOR (^)
c = a ^ b
print('\n======XOR======')
print('nilai :', a,'binary :',format(a,'08b'))
print('nilai :', b,'binary :',format(b,'08b'))
print('------------ ----------------(^)')
print('nilai :', c,'binary:',format(c,'08b'))

# Bitwise NOT (~)
c = ~a
print('\n======NOT======')
print('nilai :', a,'binary :',format(a,'08b'))
print('------------ ----------------(~)')
print('nilai :', c,'binary:',format(c,'08b'))
print('------------ ----------------(^)')
d = 0b0000001001
e = 0b1111111111
print('nilai :',d^e,'binary:',format(d^e,'08b'))

# Shifting

# shift right (>>)
c = a >> 2
print('\n======>>======')
print('nilai :', a,'binary :',format(a,'08b'))
print('------------ ----------------(>>)')
print('nilai :', c,'binary :',format(c,'08b'))

# shift right (<<)
c = a << 2
print('\n======<<======')
print('nilai :', a,'binary :',format(a,'08b'))
print('------------ ----------------(<<)')
print('nilai :', c,'binary :',format(c,'08b'))
