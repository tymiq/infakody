
fn1 = "wyniki.txt"
fn2 = "liczby1.txt"
fn3 = "liczby2.txt"


with open(fn2, "r") as file2:
    for line in file2.readlines():
        line = line.rstrip("\\n")
        print(line)

# with open(fn1, "a") as file1:
    # file1.write("111 1 1 1 1 1  1")



