# Data karyawan yang tidak akan diubah
karyawan = (
    ("ID001", "Andi", "IT Support"),
    ("ID002", "Budi", "Finance"),
    ("ID003", "Citra", "Marketing"),
)

# Menampilkan data karyawan
for data in karyawan:
    print(f"ID: {data[0]}, Nama: {data[1]}, Departemen: {data[2]}")
# Data transaksi penjualan
transaksi = (
    ("TRX001", "PRD001", 2),
    ("TRX002", "PRD002", 5),
    ("TRX003", "PRD003", 1),
)

# Menampilkan data transaksi
for data in transaksi:
    print(f"ID Transaksi: {data[0]}, ID Produk: {data[1]}, Jumlah: {data[2]}")
