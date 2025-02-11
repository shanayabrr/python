tahun = int(input("Masukan Tahun: "))


if tahun % 400 == 0:
    print(f"{tahun} Tahun Kabisat")
elif tahun % 100 == 0:
    print(f"{tahun} Bukan Tahun Kabisat")
elif tahun % 4 == 0:
    print(f"{tahun} Tahun Kabisat")
else:
    print(f"{tahun} Bukan Tahun Kabisat")
