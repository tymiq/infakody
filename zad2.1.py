name1 = "Dane 25/symbole.txt"
name2 = "wyniki2.txt"

def get_palindromes(data):
    palindromes = []
    for e in data:
        n = len(e)-1
        mid = len(e) // 2  # 5 -> 3, 4 -> 2         a b c d (e) -> dwa razy -> i = 0, i = 1 -> mid = 2
        palindrome = True
        for i in range(mid):
            if e[i] != e[n - i]:
                palindrome = False
        if palindrome:
            palindromes.append(e)
    return palindromes

# def get_squares(data):
#     for string in data:
#         n = len(string)
#         if n == 9:
#             symbol = string[0]
#             same_chars = True
#             for c in string:
#                 if c != symbol:
#                     same_chars = False




with open(name1) as f:
    data = [line.strip("\n").split(" ") for line in f]
    palindromes = get_palindromes(data)
    # squares = get_squares(data)

with open(name2, "a+") as f2:
    for line in palindromes:
        f2.write(line + "\n")