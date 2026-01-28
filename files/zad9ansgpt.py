def ma_cyfre_parzysta(x):
    for c in str(x):
        if int(c) % 2 == 0:
            return True
    return False

def same_cyfry_nieparzyste(x):
    for c in str(x):
        if int(c) % 2 == 0:
            return False
    return True

n = int(input("Podaj n: "))

suma_a = 0
suma_b = 0

for i in range(0, n + 1):
    if ma_cyfre_parzysta(i):
        suma_a += i
    if same_cyfry_nieparzyste(i):
        suma_b += i

print("a) Suma liczb z co najmniej jedną cyfrą parzystą:", suma_a)
print("b) Suma liczb bez żadnej cyfry parzystej:", suma_b)
