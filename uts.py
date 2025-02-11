print("\nMasukan Matrix A:")
baris_a = int(input("Masukan jumlah baris untuk Matrix A : "))

matrix_a = []
for i in range(baris_a):
    element = int(input(f"Masukan elemen baris ke [{i}] : "))
    matrix_a.append(element)

kolom_a = int(input("Masukan jumlah kolom untuk Matrix A : "))
for j in range(kolom_a):
    element = int(input(f"Masukan elemen kolom ke [{j}] : "))
    matrix_a.append(element)


print("\nInput Matrix B:")
baris_b = int(input("Masukan jumlah baris untuk Matrix B : "))

matrix_b = []
for i in range(baris_b):
    element = int(input(f"Masukan elemen baris ke [{i}] : "))
    matrix_b.append(element)

kolom_b = int(input("Masukan jumlah kolom untuk Matrix B : "))
for j in range(kolom_b):
    element = int(input(f"Masukan elemen kolom ke [{j}] : "))
    matrix_b.append(element)


if len(matrix_a) == len(matrix_b):
    hasil_penjumlahan = []
    for i in range(len(matrix_a)):
        hasil_penjumlahan.append(matrix_a[i] + matrix_b[i])
    print("\nHasil Penjumlahan Matrix A dan B")
    penjumlahan_formatted = [hasil_penjumlahan[:kolom_a], hasil_penjumlahan[kolom_a:]]
    for row in penjumlahan_formatted:
        print(row)
else:
    print("\nPenjumlahan tidak dapat dilakukan: Ukuran matrix tidak sama")


if len(matrix_a) == len(matrix_b):
    hasil_pengurangan = []
    for i in range(len(matrix_a)):
        hasil_pengurangan.append(matrix_a[i] - matrix_b[i])
    print("\nHasil Pengurangan Matrix A dan B")
    pengurangan_formatted = [hasil_pengurangan[:kolom_a], hasil_pengurangan[kolom_a:]]
    for row in pengurangan_formatted:
        print(row)
else:
    print("\nPengurangan tidak dapat dilakukan: Ukuran matrix tidak sama")


if len(matrix_a) == len(matrix_b):
    hasil_perkalian = []
    for i in range(len(matrix_a)):
        hasil_perkalian.append(matrix_a[i] * matrix_b[i])
    print("\nHasil Perkalian Matrix A dan B")
    perkalian_formatted = [hasil_perkalian[:kolom_a], hasil_perkalian[kolom_a:]]
    for row in perkalian_formatted:
        print(row)
else:
    print("\nPerkalian tidak dapat dilakukan: Ukuran matrix tidak sama")