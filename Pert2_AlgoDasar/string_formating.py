import datetime

nama_PT = "Pt.Bintang Jaya"
alamat = "JL.Kedoya 30 No 1, Jakarta Timur"
waktu_dibuat = datetime.datetime.now()

#position argumen
print("=======Posisional Argument=======")
print("\t\t\t{0}\nKepada,\n HRD Manager {1}\n {2}".format(nama_PT,alamat,waktu_dibuat))
print("Keyword Argumen")
print("\t\t\t{waktu}\nKepada,\nHRD Manager{nama_PT}\n{alamat}".format(nama_PT = nama_PT,alamat = alamat,waktu= waktu_dibuat))
print("=======Cara Singkat======")
print(f"\t\t\t{waktu_dibuat}\nKepada,\nHRD Manager{nama_PT}\n{alamat}")
#\t ini untuk tab, sama dengan 4nkali spasi(identasi) atau sebutannya unique simbol
#\n ini untuk newline atau enter