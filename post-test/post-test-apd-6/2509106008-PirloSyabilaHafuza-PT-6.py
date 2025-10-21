import os

pengguna = {"pirlo": "pirlo008"}  

kontak_pengguna = {"pirlo": {}}

pengguna_login = None

while True:
    if pengguna_login is None:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== SELAMAT DATANG ===")
        print("1. Login")
        print("2. Registrasi")
        print("3. Keluar")
        pilihan_awal = input("Pilih (1-3): ")

        if pilihan_awal == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== LOGIN ===")
            nama_pengguna = input("Username: ").strip()
            kata_sandi = input("Password: ").strip()

            if nama_pengguna in pengguna and pengguna[nama_pengguna] == kata_sandi:
                pengguna_login = nama_pengguna
                if nama_pengguna not in kontak_pengguna:
                    kontak_pengguna[nama_pengguna] = {}
                print("Login berhasil!")
                input("Tekan Enter untuk melanjutkan...")
            else:
                print("Username atau password salah!")
                input("Tekan Enter untuk kembali...")

        elif pilihan_awal == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== REGISTRASI AKUN ===")
            nama_pengguna = input("Masukkan username: ").strip()
            kata_sandi = input("Masukkan password: ").strip()

            if not nama_pengguna or not kata_sandi:
                print("Username dan password tidak boleh kosong!")
            elif nama_pengguna in pengguna:
                print("Username sudah digunakan!")
            else:
                pengguna[nama_pengguna] = kata_sandi
                kontak_pengguna[nama_pengguna] = {} 
                print("Akun berhasil dibuat! Silakan login.")
            input("Tekan Enter untuk kembali...")

        elif pilihan_awal == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Terima kasih! Sampai jumpa.")
            break

        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk kembali...")

    else:
        kontak = kontak_pengguna[pengguna_login]
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"=== MANAJEMEN KONTAK ({pengguna_login}) ===")
        print("1. Tambah Kontak")
        print("2. Lihat Semua Kontak")
        print("3. Ubah Kontak")
        print("4. Hapus Kontak")
        print("5. Logout")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== TAMBAH KONTAK ===")
            nama = input("Masukkan nama: ").strip()
            no_hp = input("Masukkan nomor HP: ").strip()

            if nama == "":
                print("Nama tidak boleh kosong!")
            elif no_hp == "":
                print("Nomor HP tidak boleh kosong!")
            elif not no_hp.isdigit():
                print("Nomor HP hanya boleh berisi angka (0-9)!")
            elif len(no_hp) < 10:
                print("Nomor HP minimal 10 digit!")
            else:
                if nama in kontak:
                    print(f"Peringatan: Kontak '{nama}' sudah ada dan akan ditimpa!")
                kontak[nama] = no_hp
                print("Kontak berhasil ditambahkan!")
            input("Tekan Enter untuk kembali...")

        elif pilihan == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== DAFTAR KONTAK ===")
            if not kontak:
                print("Belum ada kontak.")
            else:
                for i, (nama_kontak, nomor) in enumerate(kontak.items(), 1):
                    print(f"{i}. Nama: {nama_kontak}, No HP: {nomor}")
            input("Tekan Enter untuk kembali...")

        elif pilihan == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== UBAH KONTAK ===")
            if not kontak:
                print("Tidak ada kontak untuk diubah.")
                input("Tekan Enter untuk kembali...")
            else:
                daftar_nama = list(kontak.keys())
                for i, nama_kontak in enumerate(daftar_nama, 1):
                    print(f"{i}. Nama: {nama_kontak}, No HP: {kontak[nama_kontak]}")

                nomor_pilihan = input("Pilih nomor kontak yang ingin diubah: ")
                if not nomor_pilihan.isdigit():
                    print("Input harus berupa angka!")
                    input("Tekan Enter untuk kembali...")
                else:
                    indeks = int(nomor_pilihan) - 1
                    if not (0 <= indeks < len(daftar_nama)):
                        print("Nomor kontak tidak valid!")
                        input("Tekan Enter untuk kembali...")
                    else:
                        nama_lama = daftar_nama[indeks]
                        print(f"Mengubah kontak: {nama_lama} ({kontak[nama_lama]})")
                        nama_baru = input("Masukkan nama baru: ").strip()
                        no_hp_baru = input("Masukkan nomor HP baru: ").strip()

                        if nama_baru == "":
                            print("Nama tidak boleh kosong!")
                        elif no_hp_baru == "":
                            print("Nomor HP tidak boleh kosong!")
                        elif not no_hp_baru.isdigit():
                            print("Nomor HP hanya boleh berisi angka (0-9)!")
                        elif len(no_hp_baru) < 10:
                            print("Nomor HP minimal 10 digit!")
                        else:
                            del kontak[nama_lama]
                            kontak[nama_baru] = no_hp_baru
                            print("Kontak berhasil diubah!")
                        input("Tekan Enter untuk kembali...")

        elif pilihan == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== HAPUS KONTAK ===")
            if not kontak:
                print("Tidak ada kontak untuk dihapus.")
                input("Tekan Enter untuk kembali...")
            else:
                daftar_nama = list(kontak.keys())
                for i, nama_kontak in enumerate(daftar_nama, 1):
                    print(f"{i}. Nama: {nama_kontak}, No HP: {kontak[nama_kontak]}")

                nomor_pilihan = input("Pilih nomor kontak yang ingin dihapus: ")
                if not nomor_pilihan.isdigit():
                    print("Input harus berupa angka!")
                    input("Tekan Enter untuk kembali...")
                else:
                    indeks = int(nomor_pilihan) - 1
                    if 0 <= indeks < len(daftar_nama):
                        nama_hapus = daftar_nama[indeks]
                        del kontak[nama_hapus]
                        print("Kontak berhasil dihapus!")
                    else:
                        print("Nomor kontak tidak valid!")
                    input("Tekan Enter untuk kembali...")

        elif pilihan == "5":
            print("Anda telah logout.")
            pengguna_login = None
            input("Tekan Enter untuk kembali ke menu awal...")

        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk kembali...")