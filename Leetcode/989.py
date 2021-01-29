A = [1, 2, 0, 0]
K = 34

K_int = list(map(int, str(K)))
print(A[:len(K_int)] + list(map(lambda x, y: x + y, A[len(K_int):], K_int)))


