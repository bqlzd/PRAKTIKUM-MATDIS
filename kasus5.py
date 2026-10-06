belajar_di_kelas = False
belajar_di_perpus = True
belajar_di_cafe = False

#Model Logika
tempat_belajar = belajar_di_kelas or belajar_di_perpus or belajar_di_cafe

#Output hasil pemilihan tempat
if tempat_belajar:
    print("tempat BELAJAR TERSEDIA untuk digunakan mahasiswa")
else:
    print("tempat BELAJAR TIDAK TERSEDIA untuk mahasiswa")