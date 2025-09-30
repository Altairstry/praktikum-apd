# Produk yang ada
produk_1, harga_1 = "Laptop", 8500000
produk_2, harga_2 = "Headset Gaming", 350000
produk_3, harga_3 = "Keyboard Mechanical", 750000

#Login member
print("=== SELAMAT DATANG DI TOKO ELEKTRONIK ===")
member = input("Apakah Anda member? (y/n): ")

login = (input("Masukkan username: ") == "Pirlo" and input("Masukkan password: ") == "008") if member == "y" else print("\nAnda masuk sebagai Non-Member. Selamat berbelanja.\n")

if member == "y" and login:
    print("Login berhasil! Selamat berbelanja")
elif member == "y" and not login:
    print("Login gagal! Silahkan mulai ulang")
    exit()

#Memilih produk
print("=== MENU PRODUK ===")
print(f"1. {produk_1} - Rp{harga_1:,}")
print(f"2. {produk_2} - Rp{harga_2:,}")
print(f"3. {produk_3} - Rp{harga_3:,}")

pilih = int(input("Pilih produk (nomor): "))
jumlah = int(input("Masukkan jumlah: "))

if pilih == 1:
    nama_produk = produk_1
    harga = harga_1
elif pilih == 2:
    nama_produk = produk_2
    harga = harga_2
elif pilih == 3:
    nama_produk = produk_3
    harga = harga_3
else:
    print("Produk tidak tersedia!")
    exit()
total_belanja = harga * jumlah

#Print struk(kalau member akan mendapatkan diskon 15%)
if login:
    diskon = total_belanja * 0.15
    total_setelah_diskon = total_belanja - diskon
    print("\n=== STRUK BELANJA MEMBER ===")
    print(f"Produk               : {nama_produk}")
    print(f"Jumlah               : {jumlah}")
    print(f"Total sebelum diskon : Rp{total_belanja:,}")
    print(f"Diskon (15%)         : Rp{diskon:,}")
    print(f"Total setelah diskon : Rp{total_setelah_diskon:,}")
else:
    print("\n=== STRUK BELANJA NON-MEMBER ===")
    print(f"Produk        : {nama_produk}")
    print(f"Jumlah        : {jumlah}")
    print(f"Total belanja : Rp{total_belanja:,}")