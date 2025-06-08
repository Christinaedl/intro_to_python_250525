profile = {
    "nama" : "Christina",
    "kelas": 12,
    "jurusan" : ["IPA", "IPS"]
}

print(f"Dictionary data : {profile}")
print(f"Nama : {profile['nama']}")
print(f"Cara mengambil jurusan IPS : {profile['jurusan'][1]}")

profile['kelas'] = 10
print(f"Dictionary data : {profile}")
profile['ketua_kelas'] = "Budi"
print(f"Dictionary data : {profile}")

del profile["ketua_kelas"]
print(f"Dictionary data : {profile}")
