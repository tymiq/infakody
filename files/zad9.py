


even = [0,2,4,6,8]

def sum(n):
    if n <= 0:
        return 0
    else:
        return n + sum(n-1)


def wyswietl_z_min_1_parz(n):
    for i in range(n):
        cyfra_jest_parz = False
        suma = str(sum(i))
        for l in suma:
            if int(l) % 2 == 0:
                cyfra_jest_parz = True
        if cyfra_jest_parz:
            print("Suma: " + suma + " dla n = " + str(i))
            cyfra_jest_parz = False

def wyswietl_z_min_1_parz(n):
    for i in range(n):
        cyfra_jest_parz = False
        suma = str(sum(i))
        for l in suma:
            if int(l) % 2 == 0:
                cyfra_jest_parz = True
        if cyfra_jest_parz:
            print("Suma: " + suma + " dla n = " + str(i))
            cyfra_jest_parz = False

n = int(input("Podaj n: "))
print("a) Sumy liczb dla których co najmniej jedna cyfra jest parzysta: ")
wyswietl_z_min_1_parz(n)

def wyswietl_z_zadna_parz(n):
    for i in range(n):
        cyfra_jest_parz = False
        suma = str(sum(i))
        for l in suma:
            if int(l) % 2 == 0:
                cyfra_jest_parz = True
        if not cyfra_jest_parz:
            print("Suma: " + suma + " dla n = " + str(i))
        else:
            cyfra_jest_parz = False

print("b) Sumy liczb dla których żadna cyfra nie jest parzysta: ")
wyswietl_z_zadna_parz(n)