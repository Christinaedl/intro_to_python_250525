from employe import employe

class Manager(employe):
    def __init__(self, nama, usia, pekerjaan, gaji,jumlah_tim = 0):
        super().__init__(nama, usia, pekerjaan, gaji)
        self._jumlah_tim = jumlah_tim

    def getDetail(self):
        if self._jumlah_tim == 0 :
            return super().getDetail()
        else:
            return super().getDetail() + f"\n jumlah tim : {self._jumlah_tim}"

    def getWork(self):
        if self._jumlah_tim == 0 :
            return super().getWork()
        else :
            return f"{self.nama} bekerja sebagai manager dengan jumlah tim {self._jumlah_tim}"



