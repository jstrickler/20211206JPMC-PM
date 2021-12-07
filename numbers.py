
# we care:  int float
# we don't care: bool complex

i1 = 1234
i2 = 1000
i3 = 39208520398203958203958203958209358209358209358209358209385
i4 = 1_293_493
i5 = 12_38_73
print(i4, i5)

i6 = 0b10011001
i7 = 0xDeadBeef
i8 = 0xBadDad
print(i6, i7, i8)

f0 = 123.456
f1 = 123.
f2 = .139093
f3 = 1.938e17

a = 19
b = 5
print(a + b, a - b, a * b)
print(a / b, a // b, a // -b, a % b)
print(a ** b)
print(a ** .5)

x = 10
x *= 5  # x = x * 5
x += 25
x /= 3
print(x)

# not implemented
# x++ ++x x-- --x


# / normal division   // floored division   % modulus
print()

a = 123
b = "456"
print(a + int(b))
print(str(a) + b)

#  int str float
#  bool tuple list set bytes frozenset dict

x = "DeadBeef"
print(int(x, 16) + 5)




