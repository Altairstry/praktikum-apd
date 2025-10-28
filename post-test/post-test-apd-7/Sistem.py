import os

pengguna = {"Pirlo": "pirlo008"}
kontak_pengguna = {"Pirlo": {}}
pengguna_login = None

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_kontak(kontak_dict):
    if not kontak_dict:
        print("Belum ada kontak.")
    else:
        for i, (nama, nomor) in enumerate(kontak_dict.items(), 1):
            print(f"{i}. Nama: {nama}, No HP: {nomor}")

def menu_login():
    clear()
    print("=== SELAMAT DATANG ===")
    print("1. Login")
    print("2. Registrasi")
    print("3. Keluar")
    return input("Pilih (1-3): ")

def proses_login():
    clear()
    print("=== LOGIN ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in pengguna and pengguna[username] == password:
        print("Login berhasil!")
        if username not in kontak_pengguna:
            kontak_pengguna[username] = {}
        return username
    else:
        print("Username atau password salah!")
        return None

def proses_registrasi():
    clear()
    print("=== REGISTRASI AKUN ===")
    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()

    if not username or not password:
        print("Username dan password tidak boleh kosong!")
        return False
    if username in pengguna:
        print("Username sudah digunakan!")
        return False

    pengguna[username] = password
    kontak_pengguna[username] = {}
    print("Akun berhasil dibuat! Silakan login.")
    return True

def tampilkan_menu_utama(username):
    clear()
    print(f"=== MANAJEMEN KONTAK ({username}) ===")
    print("1. Tambah Kontak")
    print("2. Lihat Semua Kontak")
    print("3. Ubah Kontak")
    print("4. Hapus Kontak")
    print("5. Logout")
    return input("Pilih menu (1-5): ")

def tambah_kontak(kontak_dict):
    clear()
    print("=== TAMBAH KONTAK ===")
    nama = input("Masukkan nama: ").strip()
    no_hp = input("Masukkan nomor HP: ").strip()

    if nama == "":
        print("Nama tidak boleh kosong!")
    elif no_hp == "" or not no_hp.isdigit() or len(no_hp) < 10:
        print("Nomor HP harus angka dan minimal 10 digit!")
    else:
        if nama in kontak_dict:
            print(f"Peringatan: Kontak '{nama}' sudah ada dan akan ditimpa!")
        kontak_dict[nama] = no_hp
        print("Kontak berhasil ditambahkan!")
    input("Tekan Enter untuk kembali...")

def lihat_kontak(kontak_dict):
    clear()
    print("=== DAFTAR KONTAK ===")
    tampilkan_kontak(kontak_dict)
    input("Tekan Enter untuk kembali...")

def ubah_kontak(kontak_dict):
    clear()
    print("=== UBAH KONTAK ===")
    if not kontak_dict:
        print("Tidak ada kontak untuk diubah.")
        input("Tekan Enter untuk kembali...")
        return

    tampilkan_kontak(kontak_dict)
    try:
        pilihan = int(input("Pilih nomor kontak yang ingin diubah: ")) - 1
        daftar_nama = list(kontak_dict.keys())
        if 0 <= pilihan < len(daftar_nama):
            nama_lama = daftar_nama[pilihan]
            nama_baru = input("Nama baru: ").strip()
            no_hp_baru = input("Nomor HP baru: ").strip()

            if nama_baru == "":
                print("Nama tidak boleh kosong!")
            elif no_hp_baru == "" or not no_hp_baru.isdigit() or len(no_hp_baru) < 10:
                print("Nomor HP tidak valid!")
            else:
                del kontak_dict[nama_lama]
                kontak_dict[nama_baru] = no_hp_baru
                print("Kontak berhasil diubah!")
        else:
            print("Nomor kontak tidak valid!")
    except ValueError:
        print("Input harus berupa angka!")
    input("Tekan Enter untuk kembali...")

def hapus_kontak(kontak_dict):
    clear()
    print("=== HAPUS KONTAK ===")
    if not kontak_dict:
        print("Tidak ada kontak untuk dihapus.")
        input("Tekan Enter untuk kembali...")
        return

    tampilkan_kontak(kontak_dict)
    try:
        pilihan = int(input("Pilih nomor kontak yang ingin dihapus: ")) - 1
        daftar_nama = list(kontak_dict.keys())
        if 0 <= pilihan < len(daftar_nama):
            nama_dihapus = daftar_nama[pilihan]
            del kontak_dict[nama_dihapus]
            print(f"Kontak '{nama_dihapus}' berhasil dihapus!")
        else:
            print("Nomor kontak tidak valid!")
    except ValueError:
        print("Input harus berupa angka!")
    input("Tekan Enter untuk kembali...")