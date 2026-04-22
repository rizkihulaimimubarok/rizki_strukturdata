nama = (input("masukan nama anda:"))

if nama== "rizki" :
    print("selamat datang rizki")
umur = int(input("masukan umur anda:"))

if umur >= 21 :
    print("ada cukup umur")
elif umur < 0 :
    print("anda blom lahir")
elif umur < 18 :
    print("anda blom cukup umur")
elif umur > 100 :
    print("anda sudah bau tanah")

    print("program selesai")