class mobil  : #mobil disebut nama kelas
    #instansiasi
    #mempersiapkan objek apa yang akan di save oleh komputer
    roda = 4 #roda ddisebutnya object yang memiliki property public
    #property publik adalah nilai yang bisa di ubah dari luar kelas semaunya
    _warna = "default" #warna memiliki property private 
    #property private adalah nilai yang hanya bisa diubah jika diizinkan
    __merek = "default"# merk memiliki property protected(_ _)
    #property protected adalah nilai yang tidak bisa diganti di luar kelas apapun

    def __init__(self, brand:str = None,warna:str = None,merek:str= None): #ini disebutnya constructor
        self.__merek= merek
        self._brand = brand
        self._warna = warna
    #method
    def getDetail(self) :
        print(f"Nama brand : {self._brand}")
        print(f"Merek : {self.__merek}")
        print(f"Warna : {self._warna}")
        print(f"Jumlah roda : {self.roda}")


#cara memanggilnya
gakJelas = mobil()
gakJelas.getDetail()

toyota = mobil("toyota", "supra", "hitam")
toyota.roda = 2 #pemanggilan variabel atau object public
toyota.getDetail()