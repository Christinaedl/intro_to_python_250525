from person import person

class employe(person): 
    def __init__ (self, nama, usia, pekerjaan, gaji):
        super().__init__(nama, usia)
        self._pekerjaan = pekerjaan
        self.__Gaji = gaji

    def getDetail(self):
        return f"Nama Employee : {self.nama}\nUsia : {self.getUsia} \n Pekerjaan : {self._pekerjaan}\n Gaji : {self.__Gaji}"

    def getWork(self):
        return f"{self.nama} hanya seorang employe"