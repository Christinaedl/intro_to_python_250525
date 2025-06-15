from manager import Manager

def main():
    list_data = [
        {
            "nama_lengkap" : "Christina Eunike",
            "usia" : 22,
            "pekerjaan" : "Mahasiswa",
            "Gaji" : 0,
            "Jumlah_tim" : 2
        },
        {
           "nama_lengkap" : "Bayu",
            "usia" : 26,
            "pekerjaan" : "Data analyst",
            "Gaji" : 8000000,
            "Jumlah_tim" : 6 
        },{
            "nama_lengkap" : "Dani",
            "usia" : 30,
            "pekerjaan" : "Web Developer",
            "Gaji" : 8000000,
            "Jumlah_tim" :7
        },{
            "nama_lengkap" : "Bayu",
            "usia" : 23,
            "pekerjaan" : "Data analyst",
            "Gaji" : 1400,
            "Jumlah_tim" : 6 
        }
    ]
    print("========== Detail Karyawan =========")
    for person in list_data:
        employe = Manager(person['nama_lengkap'],person['usia'], person['pekerjaan'], person['Gaji'], person['Jumlah_tim'])
        print(employe.getDetail())
        print('======= detail pekerjaan ======')
        print(employe.getWork())

if __name__ == "__main__":
    main()