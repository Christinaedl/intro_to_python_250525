from abc import ABC, abstractclassmethod
class kendaraan:
    def menyalakanMesin(self):
        pass

class Motor(kendaraan) :
    def menyalakanMesin(self):
        print("status motor : Mogok")

class Mobil(kendaraan) :
    def menyalakanMesin(self):
        print("status mobil : Habis bensin")

class Pesawat(kendaraan) :
    def menyalakanMesin(self):
        print("status pesawat : kurang oil")

class kereta(kendaraan) :
    def menyalakanMesin(self):
        print("status kerreta : batu bara tidak ada yang jual !!!!!")

#polymopisme
def menyalakanMesin(kendaraan):
    kendaraan.menyalakanMesin()

bebek = Motor()
supra = Mobil()
boing = Pesawat()
kai = kereta()

menyalakanMesin(bebek)
menyalakanMesin(supra)
menyalakanMesin(boing)
menyalakanMesin(kai)

