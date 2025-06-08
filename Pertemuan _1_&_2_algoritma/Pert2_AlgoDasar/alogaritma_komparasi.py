x = 3
y = 3

# besar dari
hasil = (x > y)
print(f"Apakah nilai {x} besar dari (>) {y} adalah {hasil}")
# besar dari
hasil = (x >= y)
print(f"Apakah nilai {x} besar dari sama denngan (>=) {y} adalah {hasil}")
# kecil dari
hasil = (x < y)
print(f"Apakah nilai {x} kecil dari (<) {y} adalah {hasil}")
# kecil dari
hasil = (x >= y)
print(f"Apakah nilai {x} kecil dari sama dengan (<=) {y} adalah {hasil}") 

kondisi = True
hasil = kondisi != False # ! not ini adalah kondisi yang dibalikkan
print(f"Apa yang akan terjadi dari kondisi diatas : {hasil}")

x = "1"
y = 1
hasil = x == str(y)
#kalau jumlah sama dengan 3 (===) program akan check keakuratan tipe data 
print(f"hasil dari {x} apakah sama dengan {y} adalah {hasil}")