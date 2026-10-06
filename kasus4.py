jadwal_pagi = False
jadwal_siang = True
jadwal_sore = False

#Model Logika
jadwal = jadwal_pagi or jadwal_siang or jadwal_sore

#Output hasil jadwal kuliah
if jadwal:
    print("jadwal kuliah yang dipilih TERSEDIA untuk mahasiswa")
else:
    print("jadwal kuliah yang dipilih BELUM TERSEDIA untuk mahasiswa")