class Ibu :
    panggilan = "Iya, ada apa ?"
    _sifat = "lembut"

    def setSifat(self,sifat):
        self._sifat = sifat

    def getSifat(self):
        return f"Sifat dari tokoh : {self._sifat}"
    
    def getpanggilan(self):
        return f"{self.panggilan}"
    
class Anak(Ibu): # ini yang disebut encapsulation
        def disuruh(self):
            return f"Nanti dulu deh !!!!!"
        
#cara memanggil
Toni = Anak()
Toni.panggilan = "Ton Ton"
Toni.setSifat("pemarah")
print(Toni.getpanggilan())
print(Toni.getSifat())