# Fungsi untuk menghitung tunjangan
def hitung_tunjangan(gaji):
    return gaji * 0.1

# Fungsi untuk menghitung total gaji
def hitung_total_gaji(gaji, tunjangan):
    return gaji + tunjangan

# Input data pegawai
id_pegawai = input("Masukkan ID Pegawai: ")
nama = input("Masukkan Nama Pegawai: ")
gaji = float(input("Masukkan Gaji Pegawai: "))

# Hitung tunjangan dan total gaji
tunjangan = hitung_tunjangan(gaji)
total_gaji = hitung_total_gaji(gaji, tunjangan)

# Tampilkan hasil
print("\n--- Informasi Gaji Pegawai ---")
print("ID Pegawai: {id_pegawai}")
print(f"Nama Pegawai: {nama}")
print(f"Gaji: Rp {gaji:.2f}")
print(f"Tunjangan: Rp {tunjangan:.2f}")
print(f"Total Gaji: Rp {total_gaji:.2f}")
