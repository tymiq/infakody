# rekursja fibonacci n poczatkowych wyrazow wyswietl
# 0 1 1 2 3 5 8 13 ...

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def main():
    n = 10 # liczba pocz wyr
    # print(fib(n))
    for i in range(n):
        print(fib(i), end = " ")
main()