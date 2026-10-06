mahasiswa = True
dosen = False
anggota_umum = False

#Model Logika
peminjam = mahasiswa or dosen or anggota_umum

#Output hasil peminjam buku
if peminjam:
    print("buku perpustakaan DAPAT DIPINJAM oleh pengguna")
else:
    print("buku perpustakaan BELUM DAPAT DIPINJAM oleh pengguna")