#inisialisasi
# teknik program menyediakan memory yang akan di pakai
makanan = ["Nasi","sayur","ayam"]

#read
print(f"List makanan :  {makanan}")

#read spesifik
print(f"index of 1 : {makanan[1]}")
print(f"index of -1 : {makanan[-1]}")

#update(U)
makanan[1] = "daging"
print(f"List makanan :  {makanan}")

#tambah data append (a)
makanan.append("sayur")
print(f"List makanan :  {makanan}")

makanan.remove("Nasi")
print(f"List makanan :  {makanan}")

buah = ["Semangka", "Melon", "Nanas"]
makanan += buah
print(f"List makanan :  {makanan}")

