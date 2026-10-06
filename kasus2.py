username_benar = True
password_benar = True
akun_aktif = True

#Model Logika
login = username_benar and password_benar and akun_aktif

#Output hasil login
if login:
    print("LOGIN BERHASIL")
else:
    print("LOGIN GAGAL")