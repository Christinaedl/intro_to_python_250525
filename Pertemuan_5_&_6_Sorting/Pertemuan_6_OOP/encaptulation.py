class mobil  : 
    roda = 4 
    _warna = "default" #ini encaptulation
    __merek = "default"
    def __init__(self, brand:str = None,warna:str = None,merek:str= None): #ini disebutnya constructor
        self.__merek= merek
        self._brand = brand
        self._warna = warna
    #method
    def getDetail(self) :
        print(f"Nama brand : {self._brand}")
        print(f"Merek : {self.__merek}")
        print(f"Warna : {self.getWarna()}")
        print(f"Jumlah roda : {self.roda}")

#set and get
#set
#kalau ada kata awalan set ini sifatnya untuk merubah nilai private
    def setWarna(self,warna):
        self._warna = warna
#get
#kalau adakata awalan get ini sifatnya untuk mengambil nilai private
    def getWarna(self):
        return f"{self._warna} Metalik"


#cara memanggilnya
# gakJelas = mobil()
# gakJelas.getDetail()

toyota = mobil("toyota", "hitam", "supra")
toyota.roda = 2 #pemanggilan variabel atau object public
toyota.setWarna("merah")
toyota.getDetail()