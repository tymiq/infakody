

def arr(A, i, n):
    if i == n*n:
        return 0
    w = i // n + 1
    k = i % n + 1
    return A[:w][:k] + arr(A,i+1,n)               # A[1,1] => A[;

print(arr([[2,1],[5,3]],0,2))