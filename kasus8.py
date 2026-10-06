tugas_individu = False
tugas_kelompok = True

#Model Logika
jenis_tugas = tugas_individu ^ tugas_kelompok

#Output hasil jenis tugas
if jenis_tugas:
    print("jenis tugas yang dipilih BERHASIL DITENTUKAN untuk mahasiswa")
else:
    print("jenis tugas yang dipilih BELUM DAPAT DITENTUKAN untuk mahasiswa")