# rekursja fibonacci n poczatkowych wyrazow wyswietl
# 1 1 2 3 5 8 13 ...


def fibonacci(n):
    lista = []
    a1 = 0
    a2 = 1
    for i in range(n):
        a3 = a1+a2
        print(a1, a2, end=" ")
        a1 = a2
        a2 = a3

    # for i in range(1,n+1):
    #     prev = prev + i
    #     print()


def main():
    n = 10
    fibonacci(n)

main()