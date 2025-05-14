anos = 0
a = 80000
b = 200000

while a <= b:
    anos += 1
    a += a * 0.03
    b += b * 0.015
    print(f"População A: {a} habitantes")
    print(f"População B: {b} habitantes")
    print(f"{anos} anos")
print(anos)