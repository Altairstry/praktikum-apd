import os

kontak = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== MANAJEMEN DATA KONTAK ===")
    print("1. Tambah Kontak")
    print("2. Lihat Semua Kontak")
    print("3. Ubah Kontak")
    print("4. Hapus Kontak")
    print("5. Keluar")
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
            kontak.append([nama, no_hp])
            print("Kontak berhasil ditambahkan!")
        input("Tekan Enter untuk kembali...")

    elif pilihan == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== DAFTAR KONTAK ===")
        if not kontak:
            print("Belum ada kontak.")
        else:
            for i in range(len(kontak)):
                print(f"{i + 1}. Nama: {kontak[i][0]}, No HP: {kontak[i][1]}")
        input("Tekan Enter untuk kembali ke menu...")

    elif pilihan == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== UBAH KONTAK ===")
        if len(kontak) == 0:
            print("Tidak ada kontak untuk diubah.")
            input("Tekan Enter untuk kembali...")
            continue

        for i in range(len(kontak)):
            print(f"{i + 1}. Nama: {kontak[i][0]}, No HP: {kontak[i][1]}")
        nomor = input("Pilih nomor kontak yang ingin diubah: ")

        if not nomor.isdigit():
            print("Input harus berupa angka!")
            input("Tekan Enter untuk kembali...")
            continue

        index = int(nomor) - 1
        if not (0 <= index < len(kontak)):
            print("Nomor kontak tidak valid!")
            input("Tekan Enter untuk kembali...")
            continue

        nama = input("Masukkan nama baru: ").strip()
        no_hp = input("Masukkan nomor HP baru: ").strip()

        if nama == "":
            print("Nama tidak boleh kosong!")
        elif no_hp == "":
            print("Nomor HP tidak boleh kosong!")
        elif not no_hp.isdigit():
            print("Nomor HP hanya boleh berisi angka (0-9)!")
        elif len(no_hp) < 10:
            print("Nomor HP minimal 10 digit!")
        else:
            kontak[index][0] = nama
            kontak[index][1] = no_hp
            print("Kontak berhasil diubah!")
        input("Tekan Enter untuk kembali...")

    elif pilihan == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== HAPUS KONTAK ===")
        if not kontak:
            print("Tidak ada kontak untuk dihapus.")
            input("Tekan Enter untuk kembali...")
        else:
            for i in range(len(kontak)):
                print(f"{i + 1}. Nama: {kontak[i][0]}, No HP: {kontak[i][1]}")
            nomor = input("Pilih nomor kontak yang ingin dihapus: ")
            if nomor.isdigit():
                index = int(nomor) - 1
                if 0 <= index < len(kontak):
                    del kontak[index]
                    print("Kontak berhasil dihapus!")
                else:
                    print("Nomor kontak tidak valid!")
            else:
                print("Input harus berupa angka!")
            input("Tekan Enter untuk kembali...")

    elif pilihan == "5":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Terima kasih telah menggunakan program ini!")
        input("Tekan Enter untuk keluar...")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")