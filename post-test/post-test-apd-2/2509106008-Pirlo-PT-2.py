#input data pasien
namaPasien = input("Nama Pasien: ")
tinggiBadan = int(input("Tinggi Badan(cm): "))
beratBadan = int(input("Berat Badan(kg): "))

#cek status
beratIdeal = tinggiBadan - 100
isKelebihan = beratBadan > beratIdeal
statusList = ["Normal", "Kelebihan Berat Badan"]
status = statusList[int(isKelebihan)]

#hasil dari input
print("-" * 81)
print(f"|{"HASIL CEK BERAT BADAN":^79}|")
print("-" * 81)
print(f"| Nama Pasien       : {namaPasien:<58}|")
print(f"| Tinggi Badan      : {tinggiBadan:<4}cm{'':<52}|")
print(f"| Berat Badan       : {beratBadan:<4}kg{'':<52}|")
print(f"| Beran Ideal       : {beratIdeal:<4}kg{'':<52}|")
print(f"| Status            : {status:<58}|")
print("-" *  81)