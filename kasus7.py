bayar_tunai = True
bayar_transfer = False

#Model Logika
metode_bayar = bayar_tunai ^ bayar_transfer

#Output hasil metode pembayaran
if metode_bayar:
    print("metode pembayaran yang dipilih BERHASIL DIGUNAKAN untuk transaksi")
else:
    print("metode pembayaran yang dipilih TIDAK DAPAT DIGUNAKAN untuk transaksi")