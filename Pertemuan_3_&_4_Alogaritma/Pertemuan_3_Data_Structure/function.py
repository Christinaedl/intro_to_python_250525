employee = [
    {
    "nama" : "Christina",
    "pekerjaan" : "mahasiswa",
    "gaji" : 8000000
    },
    {
    "nama" : "Budi",
    "pekerjaan" : "Dosen",
    },
    {
    "nama" : "Anton",
    "pekerjaan" : "IT Trainer",
    },
]
print("===================Daftar Pekerja ========================")
def detail_pekerja(nama,pekerjaan, gaji= None):
    print(f"Nama : {nama}")
    print(f"pekerjaan : {pekerjaan}")
    print(f"Gaji : {gaji}")
    print(f"pekerja yang rajin")

detail_pekerja(employee[0]['nama'], employee[0]['pekerjaan'], employee[0]['gaji'])
detail_pekerja(employee[1]['nama'], employee[1]['pekerjaan'])
detail_pekerja(employee[2]['nama'], employee[2]['pekerjaan'])

def penjumlahan(a,b):
        return a + b 
    
hasil_penjumlahan = penjumlahan(10,12)
print(f"Hasil dari penjumlahan :{hasil_penjumlahan}")