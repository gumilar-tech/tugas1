# Menyimpan data karyawan dengan input user

# List untuk menampung tuple karyawan
karyawan = []

# Jumlah data yang ingin dimasukkan
jumlah_karyawan = int(input("Berapa jumlah karyawan yang ingin didata? "))

# Input data karyawan
for i in range(jumlah_karyawan):
    print(f"\nData karyawan ke-{i+1}")
    id_karyawan = input("Masukkan ID Karyawan: ")
    nama = input("Masukkan Nama: ")
    departemen = input("Masukkan Departemen: ")
    karyawan.append((id_karyawan, nama, departemen))

# Menampilkan data karyawan
print("\n=== Data Karyawan ===")
for data in karyawan:
    print(f"ID: {data[0]}, Nama: {data[1]}, Departemen: {data[2]}")
# Menyimpan data transaksi dengan input user

# List untuk menampung tuple transaksi
transaksi = []

# Jumlah transaksi yang ingin dicatat
jumlah_transaksi = int(input("\nBerapa jumlah transaksi yang ingin dicatat? "))

# Input data transaksi
for i in range(jumlah_transaksi):
    print(f"\nData transaksi ke-{i+1}")
    id_transaksi = input("Masukkan ID Transaksi: ")
    id_produk = input("Masukkan ID Produk: ")
    jumlah = int(input("Masukkan Jumlah Produk: "))
    transaksi.append((id_transaksi, id_produk, jumlah))

# Menampilkan data transaksi
print("\n=== Data Transaksi ===")
for data in transaksi:
    print(f"ID Transaksi: {data[0]}, ID Produk: {data[1]}, Jumlah: {data[2]}")
