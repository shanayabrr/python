def input_matrix(name):
    rows = int(input(f"Masukkan jumlah baris untuk Matriks {name}: "))
    cols = int(input(f"Masukkan jumlah kolom untuk Matriks {name}: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Masukkan elemen Matriks {name} baris {i+1}, kolom {j+1}: "))
            row.append(element)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiply_matrices(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

def main():
    print("Operasi Matriks:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    
    choice = int(input("Pilih operasi (1/2/3): "))
    
    print("\nMasukkan Matriks A:")
    A = input_matrix("A")
    
    print("\nMasukkan Matriks B:")
    B = input_matrix("B")
    
    if choice == 1:
        if len(A) == len(B) and len(A[0]) == len(B[0]):
            print("\nHasil Penjumlahan Matriks A dan B:")
            result = add_matrices(A, B)
            print_matrix(result)
        else:
            print("Matriks harus memiliki ukuran yang sama untuk penjumlahan!")
    elif choice == 2:
        if len(A) == len(B) and len(A[0]) == len(B[0]):
            print("\nHasil Pengurangan Matriks A dan B:")
            result = subtract_matrices(A, B)
            print_matrix(result)
        else:
            print("Matriks harus memiliki ukuran yang sama untuk pengurangan!")
    elif choice == 3:
        if len(A[0]) == len(B):
            print("\nHasil Perkalian Matriks A dan B:")
            result = multiply_matrices(A, B)
            print_matrix(result)
        else:
            print("Jumlah kolom Matriks A harus sama dengan jumlah baris Matriks B untuk perkalian!")
    else:
        print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()

