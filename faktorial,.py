def faktorial(n):
    if n == 0 or n == 1:  
        return 1
    else:
        return n * faktorial(n - 1)  

print("Program Perhitungan Faktorial")
angka = int(input("Masukkan angka: "))

print("Hasil Faktorial:")
for i in range(angka + 1):
    print(f"{i}! = ",faktorial(i))


