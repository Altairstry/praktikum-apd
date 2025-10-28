import sistem as s

def main():
    while True:
        if s.pengguna_login is None:
            pilihan = s.menu_login()

            if pilihan == "1":
                s.pengguna_login = s.proses_login()
                input("Tekan Enter untuk kembali...")

            elif pilihan == "2":
                s.proses_registrasi()
                input("Tekan Enter untuk kembali...")

            elif pilihan == "3":
                s.clear()
                print("Terima kasih! Sampai jumpa.")
                break

            else:
                print("Pilihan tidak valid!")
                input("Tekan Enter untuk kembali...")

        else:
            pilihan = s.tampilkan_menu_utama(s.pengguna_login)
            kontak = s.kontak_pengguna[s.pengguna_login]

            if pilihan == "1":
                s.tambah_kontak(kontak)
            elif pilihan == "2":
                s.lihat_kontak(kontak)
            elif pilihan == "3":
                s.ubah_kontak(kontak)
            elif pilihan == "4":
                s.hapus_kontak(kontak)
            elif pilihan == "5":
                print("Anda telah logout.")
                s.pengguna_login = None
                input("Tekan Enter untuk kembali...")
            else:
                print("Pilihan tidak valid!")
                input("Tekan Enter untuk kembali...")

if __name__ == "__main__":
    main()