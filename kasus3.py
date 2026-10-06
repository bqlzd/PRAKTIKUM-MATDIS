pendaftaran_lengkap = True
mengikuti_wawancara = True
memenuhi_syarat = True

#Model Logika
diterima = pendaftaran_lengkap and mengikuti_wawancara and memenuhi_syarat

#Output hasil seleksi anggota
if diterima:
    print("Calon anggota organisasi DINYATAKAN LULUS seleksi")
else:
    print("Calon anggota organisasi DINYATAKAN TIDAK LULUS seleksi")
