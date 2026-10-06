aktif = True
ipk_memenuhi = True
administrasi_lengkap = True

#Model Logika
penerima = aktif and ipk_memenuhi and administrasi_lengkap

#Output hasil beasiswa
if penerima:
    print("Mahasiswa MENERIMA BEASISWA)"
else:
    print("Mahasiswa TIDAK MENERIMA BEASISWA")