# Matriks A
A = [
    [11, 80, 21, 10],
    [23, 5, 12, 14],
    [21, 7, 21, 14],
    [13, 44, 32, 15]
]

# Matriks B
B = [
    [1, 0, 0, 1],
    [0, 1, 0, 0],
    [5, 0, 1, 5],
    [1, 0, 0, 1]
]

# Inisialisasi matriks hasil
result = [[0 for _ in range(4)] for _ in range(4)]

# Perkalian matriks secara manual
for i in range(4):  # Baris matriks A
    for j in range(4):  # Kolom matriks B
        for k in range(4):  # Elemen untuk dikalikan
            result[i][j] += A[i][k] * B[k][j]

# Output hasil
print("Hasil perkalian matriks A x B:")
for row in result:
    print(row)
