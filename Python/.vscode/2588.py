a = input()
b = input()
a = int(a)
b = list(b)

print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
c = int(b[0]) * 100 + int(b[1]) * 10 + int(b[2])
print(a*c)