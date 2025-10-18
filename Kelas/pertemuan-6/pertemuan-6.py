# Membuat set
# buah = {"apel", "jeruk", "mangga", "apel"}
# for i in buah :
#     print(i)


#mengubah list menjadi set
# angka = [1, 1, 2, 5, 2, 3, 6]
# unik = set(angka)
# print(unik

# Daftar_buku = {
# "Buku1" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }

# print(Daftar_buku["Buku1"])

# Biodata = {
# "Nama" : "Ananda Daffa Harahap",
# "NIM" : 2409106050,
# "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Social Media" : {"Instagram" : "daffahrhap"
# }
# }

# for i, j in Biodata.items():
#     print(i)
#     print(j)

# print(f"nama saya adalah {Biodata['Nama']}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# print(f"nama saya adalah {Biodata.get('nama')}")
# print(Biodata.get('Nama'))

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# print(Film)
# Film.clear()
# print(Film)


# Musik = {
#     "The Chainsmoker": ["All we Know", "The Paris"],
#     "Alan Walker": ["Alone", "Lily"],
#     "Neffex": ["Best of Me",['tes','halo'], "Memories"],
#     'Paramore' : ["Misery Business", "Ain't It Fun", 
#                 ['All We Know Is Falling',['Here We Go Again', 'My Heart']],'This Is Why' ]
# }

# print(Musik['Paramore'][2][1][0])

# angka = {10,11,12}
# angka2 = {11,13,14}
# angka3 = angka | angka2
# print(angka3)


# Hapus = Film.pop('The Conjuring')
# print(Film)
# print(Hapus)
# Film["Zombieland"] = "Comedy"
# Film.update({"Upin Ipin" : "Comedy"})
# #Setelah Ditambah
# print(Film)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }

# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print(Nilai)