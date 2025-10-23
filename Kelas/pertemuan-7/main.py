# def perkenalan(nama):
#     print(f"Perkenalkan nama saya {nama}")

# perkenalan("Pirlo")

# def perkalian():
#     x = 5 * 3
#     print(x) 

# perkalian()

# def perkenalan():
#     x = 5 * 5
#     y = 5 + 10
#     print(x + y)

# perkenalan()

# def luaspersegi(panjang, lebar):
#     luas = panjang * lebar
#     print(f"luas dari persegi panjang adalah {luas}")

# luaspersegi(14,12)

# def luaspersegijawa(sisi):
#     luas = sisi * sisi
#     return luas

# print("luas persegi :", (luaspersegijawa(8)))

# def volume_persegi(sisi):
#     volume = luaspersegijawa(sisi) * sisi
#     print("volume persegi =", volume)

# luaspersegijawa(4)
# volume_persegi(8)

# def faktorial(n):
# Basis (Base Case): Kondisi berhenti
    # if n == 1 or n == 0:
        # return 1
# Rekursi (Recursive Case): Fungsi memanggil dirinya sendiri
    # else:
        # return n * faktorial(n - 1)
# Memanggil fungsi

# hasil = faktorial(7)
# print(f"Hasil dari 7! adalah: {hasil}")

# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
#     menu = input("PILIH MENU> ")
#     print ("\n")
#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     elif menu == "5":
#         exit()
#     else:
#         print ("Salah pilih!")

# # Fungsi untuk menampilkan semua data
# Film = []
# def show_data():
#     if len(Film) <= 0:
#         print("Belum Ada data")
#     else:
#         print("ID | Judul Film")
#     for indeks in range(len(Film)):
#         print(indeks, "|", Film[indeks])

# # Fungsi untuk menambah data
# def insert_data():
#     film_baru = input("Judul Film: ")
#     Film.append(film_baru)
#     print("Film berhasil ditambahkan!")

# # Fungsi untuk mengedit data
# def edit_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(Film) or indeks < 0:
#         print("ID salah")
#     else:
#         judul_baru = input("Judul baru: ")
#     Film[indeks] = judul_baru
#     print("Film berhasil diupdate!")

# # Fungsi untuk menghapus data
# def delete_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(Film) or indeks < 0:
#         print("ID salah")
#     else:
#         Film.remove(Film[indeks])
#     print("Film berhasil dihapus!")

# # fungsi untuk menampilkan menu
# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
#     menu = input("PILIH MENU> ")
#     print ("\n")
#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     elif menu == "5":
#         exit()
#     else:
#         print("salah pilih")
#     while True:
#         show_menu()

# try: 
#     angka = int(input("Masukkan harga\t: "))
# except ValueError:
#     print("inputan bukan berupa angka")
# else:
#     print(angka)
# finally:
#     print("Yoga")

# try:
#     usn = input('Username yang diinginkan : ')
#     if len(usn) < 5:
#         raise ValueError('Nama Minimal Memiliki 5 karakter')
# except ValueError as e:
#     print(e)
# else:
#     print(usn)

# try:
#     usn = input("Masukkan Username :")
#     if not usn.strip == " ":
#         raise ValueError("Nama tidak boleh kosong")
# except ValueError as e:
#     print(e)
# else:
#     print(usn)