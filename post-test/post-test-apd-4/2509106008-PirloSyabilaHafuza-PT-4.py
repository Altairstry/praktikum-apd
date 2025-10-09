import os
produk_1, harga_1 = "Laptop", 8500000
produk_2, harga_2 = "Headset Gaming", 350000
produk_3, harga_3 = "Keyboard Mechanical", 750000

while True:
    os.system("cls")
    print("=== SELAMAT DATANG DI TOKO ELEKTRONIK ===")
    member = input("Apakah Anda member? (y/n): ")

    login = False
    if member == "y":
        percobaan = 3
        while percobaan > 0:
            Username = input("Masukkan username: ")
            Password = input("Masukkan password: ")
            
            if Username == "" or Password == "":
                percobaan -= 1
                print(f"Username/password tidak boleh kosong! Sisa percobaan: {percobaan}")
            elif Username == "Pirlo" and Password == "008":
                login = True
                print("Login berhasil! Selamat berbelanja")
                break
            else:
                percobaan -= 1
                print(f"Login gagal! Sisa percobaan: {percobaan}")
        
        if percobaan == 0:
            print("Login gagal 3x! Anda masuk sebagai Non-Member.")
    else:
        print("Masuk sebagai Non-Member. Selamat berbelanja.\n")
    
    keranjang = ""
    total_belanja = 0
    
    while True:
        print("\n=== MENU PRODUK ===")
        print(f"1. {produk_1} - Rp{harga_1:,}")
        print(f"2. {produk_2} - Rp{harga_2:,}")
        print(f"3. {produk_3} - Rp{harga_3:,}")
        print("4. Checkout")
        
        pilih = input("Pilih produk (nomor): ")
        if pilih == "4":
            break
        
        if pilih == "1":
            nama_produk = produk_1
            harga = harga_1
        elif pilih == "2":
            nama_produk = produk_2
            harga = harga_2
        elif pilih == "3":
            nama_produk = produk_3
            harga = harga_3
        else:
            print("Pilihan tidak tersedia!")
            continue
        
        jumlah = int(input("Masukkan jumlah: "))
        
        keranjang += f"{nama_produk} x{jumlah}\n"
        total_belanja += harga * jumlah
        print(f"{nama_produk} berhasil ditambahkan. Total sementara: Rp{total_belanja:,}")
    
    print("\n=== STRUK BELANJA ===")
    print(keranjang)
    if login:
        diskon = total_belanja * 0.15
        total_setelah_diskon = total_belanja - diskon
        print(f"Total sebelum diskon : Rp{total_belanja:,}")
        print(f"Diskon (15%)         : Rp{diskon:,}")
        print(f"Total yang harus dibayar : Rp{total_setelah_diskon:,}")
    else:
        print(f"Total yang harus dibayar : Rp{total_belanja:,}")
    
    ulang = input("\nApakah ingin memulai transaksi baru? (y/n): ")
    if ulang != "y":
        print("\n=== Terima kasih telah berbelanja! ===\n")
        break