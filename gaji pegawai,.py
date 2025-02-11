def hitung_gajidari_bos(gaji):
    return gaji * 0.1

def hitung_total_gaji(gaji, tunjangan):
    return gaji + tunjangan

id_pegawai = input("Masukan ID Pegawai:")
nama = input("Masukkan Nama Pegawai: ")
gaji = float(input("Masukkan Gaji Pegawai: "))
tunjangan = hitung_gajidari_bos(gaji)
total_gaji = hitung_total_gaji(gaji, tunjangan)
print("ID Pegawai:", id_pegawai)
print("Nama Pegawai:", nama)
print("Gaji: Rp", gaji)
print("Tunjangan: Rp ", tunjangan)
print("Total Gaji: Rp ", total_gaji)
